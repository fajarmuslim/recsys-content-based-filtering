import pytz
from datetime import datetime
from app.config import get_settings

tz = pytz.timezone(get_settings().sqlalchemy_database_connect_timezone)


def indo_now():
    return datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(tz)
