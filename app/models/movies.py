from sqlalchemy import Column, Float, Integer, String
from app.db.base_class import Base


class Movies_Ranked(Base):
    id = Column(Integer, primary_key=True, index=True)
    original_title = Column(String(255), nullable=False)
    vote_count = Column(Float, nullable=False)
    vote_average = Column(Float, nullable=False)
    weighted_average = Column(Float, nullable=False)
    popularity = Column(Float, nullable=False)
    overview = Column(String(1000), nullable=False)
