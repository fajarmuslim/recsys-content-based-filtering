from pydantic import BaseModel
from app.schemas.base import BaseResponse


class RecommenderRequest(BaseModel):
    query: str

    class Config:
        orm_mode = True


class SingleMovies(BaseResponse):
    original_title: str
    vote_count: float
    weighted_average: float
    vote_average: float
    popularity: float
    overview: str


class RecommenderResponse(BaseResponse):
    pass
