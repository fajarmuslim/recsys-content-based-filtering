from app.crud.recommender import movies_ranked
import pickle


class RecommenderPredictor:
    def __init__(self) -> None:
        sig_object = open("app/ml_model/sig_object", "rb")
        self.sig = pickle.load(sig_object)
        sig_object.close()

        indices_object = open("app/ml_model/indices_object", "rb")
        self.indices = pickle.load(indices_object)
        indices_object.close()

    def get_most_popular_movies(self, db):
        return movies_ranked.read_most_popular(db=db)

    def get_most_weighted_average_movies(self, db):
        return movies_ranked.read_most_high_score(db=db)

    def get_most_suitable_movies(self, db, feature):
        # Get the index corresponding to original_title
        idx = self.indices[feature.query]

        # Get the pairwsie similarity scores
        sig_scores = list(enumerate(self.sig[idx]))

        # Sort the movies
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        # Scores of the 10 most similar movies
        sig_scores = sig_scores[1:11]

        # Movie indices
        movie_indices = [i[0] for i in sig_scores]

        # Top 10 most similar movies
        return movies_ranked.read_relevant_movies(db=db, ids=movie_indices)
