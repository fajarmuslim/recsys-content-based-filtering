from fastapi import APIRouter, Depends

from app.schemas.recommender import (
    RecommenderRequest,
    RecommenderResponse,
)
from app.logic.recommender import RecommenderPredictor
from fastapi.security.api_key import APIKey
from app.middleware.auth import get_api_key
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.utils.response_builder import create_standard_response

router = APIRouter(tags=["Recommender"])
recommender_predictor = RecommenderPredictor()


@router.get(
    "/popular",
    response_model=RecommenderResponse,
    name="recommender most popular",
)
def most_popular_movies(
    db: Session = Depends(get_db), api_key: APIKey = Depends(get_api_key)
):
    return create_standard_response(
        status="OK",
        message="OK",
        data=recommender_predictor.get_most_popular_movies(db),
    )


@router.get(
    "/weighted-average",
    response_model=RecommenderResponse,
    name="recommender most weighted average",
)
def most_weighted_average_movies(
    db: Session = Depends(get_db),
    api_key: APIKey = Depends(get_api_key),
):
    return create_standard_response(
        status="OK",
        message="OK",
        data=recommender_predictor.get_most_weighted_average_movies(db),
    )


@router.post(
    "/relevant",
    response_model=RecommenderResponse,
    name="recommender with most relevant movies",
)
def most_relevant_movies(
    request: RecommenderRequest,
    db: Session = Depends(get_db),
    api_key: APIKey = Depends(get_api_key),
):
    return create_standard_response(
        status="OK",
        message="OK",
        data=recommender_predictor.get_most_suitable_movies(
            feature=request, db=db
        ),
    )
