import pandas as pd
from app.db.session import SessionLocal
from app.models.movies import Movies_Ranked

db = SessionLocal()
credits = pd.read_csv("dataset/tmdb_5000_credits.csv")
movies_incomplete = pd.read_csv("dataset/tmdb_5000_movies.csv")

# Credit to Ibtesam Ahmed for her kernel:
# https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system

credits_renamed = credits.rename(index=str, columns={"movie_id": "id"})
movies_dirty = movies_incomplete.merge(credits_renamed, on="id")
movies_dirty.head()

movies_clean = movies_dirty.drop(
    columns=[
        "homepage",
        "title_x",
        "title_y",
        "status",
        "production_countries",
    ]
)
movies_clean.head()

V = movies_clean["vote_count"]
R = movies_clean["vote_average"]
C = movies_clean["vote_average"].mean()
m = movies_clean["vote_count"].quantile(0.70)

movies_clean["weighted_average"] = (V / (V + m) * R) + (m / (m + V) * C)

movies_ranked = movies_clean.sort_values("weighted_average", ascending=False)
for idx, row in movies_ranked.iterrows():
    iris_instance = Movies_Ranked(
        id=idx,
        original_title=row["original_title"],
        vote_count=row["vote_count"],
        vote_average=row["vote_average"],
        weighted_average=row["weighted_average"],
        popularity=row["popularity"],
        overview=row["overview"],
    )
    db.add(iris_instance)
    db.commit()

print(f"Done inserting {len(movies_ranked)} instances")
db.close()
