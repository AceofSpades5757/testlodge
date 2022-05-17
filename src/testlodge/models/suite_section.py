from __future__ import __annotations__

from typing import List
from typing import TypedDict
from typing import Union

from testlodge._types import DateTimeStr
from testlodge._types import Pagination


AnySuiteSection = Union[SuiteSection, LazySuiteSection]


class SuiteSectionJSON(TypedDict):

    id: int
    title: str
    suite_id: int
    created_at: DateTimeStr
    updated_at: DateTimeStr


class SuiteSectionListJSON(TypedDict):

    pagination: Pagination
    suite_sections: List[SuiteSectionJSON]


class SuiteSection:
    # TODO
    ...


class LazySuiteSection:
    """Create a suite section when needed, given a client."""

    def __init__(self, id, client):

        self.id = id
        self.client = client

    def gather(self) -> SuiteSection:
        if self.client is None:
            raise AttributeError("Client has not been set.")
        return self.client.suite_section(self.id)
