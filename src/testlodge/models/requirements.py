from typing import TypedDict

from testlodge._types import DateTimeStr
from testlodge._types import Pagination


class RequirementDocumentJSON(TypedDict):

    id: int
    title: str
    should_version: bool
    project_id: int
    created_at: DateTimeStr
    updated_at: DateTimeStr


class RequirementDocumentListJSON(TypedDict):

    pagination: Pagination
    requirement_documents: list[RequirementDocumentJSON]
