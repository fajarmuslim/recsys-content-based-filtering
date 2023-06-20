set -a
. .env
alembic revision --autogenerate -m "feature store"
alembic upgrade head
set +a
