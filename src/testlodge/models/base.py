from abc import ABC
from datetime import datetime

from testlodge._constants import DATETIME_FORMAT
from testlodge._constants import TIMEZONE
from testlodge._types import DateTimeStr


class BaseModel(ABC):
    @staticmethod
    def str_to_datetime(datetimestr: DateTimeStr) -> datetime:
        """Convert a UTC datetime string to a local datetime object."""
        return datetime.strptime(datetimestr, DATETIME_FORMAT).astimezone()

    @staticmethod
    def datetime_to_str(local_datetime: datetime) -> DateTimeStr:
        """Convert a local datetime to a UTC datetime string."""
        return local_datetime.astimezone(TIMEZONE).strftime(DATETIME_FORMAT)
