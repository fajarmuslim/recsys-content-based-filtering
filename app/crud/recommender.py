from app.models.movies import Movies_Ranked

from app.crud.base import CRUDBase
from sqlalchemy.orm import Session
from typing import Optional


class CRUDMoviesRanked(CRUDBase[Movies_Ranked]):
    def read_most_popular(self, db: Session) -> Optional[Movies_Ranked]:
        return (
            db.query(Movies_Ranked)
            .order_by(Movies_Ranked.popularity.desc())
            .limit(10)
            .all()
        )

    def read_most_high_score(self, db: Session) -> Optional[Movies_Ranked]:
        return (
            db.query(Movies_Ranked)
            .order_by(Movies_Ranked.weighted_average.desc())
            .limit(10)
            .all()
        )

    def read_relevant_movies(
        self, db: Session, ids
    ) -> Optional[Movies_Ranked]:
        return db.query(Movies_Ranked).filter(Movies_Ranked.id.in_(ids)).all()


movies_ranked = CRUDMoviesRanked(Movies_Ranked)
