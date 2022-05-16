from typing import List
from typing import Optional
from typing import TypedDict

from testlodge._types import DateTimeStr
from testlodge._types import Pagination
from testlodge.models.custom_field import CustomFieldJSON
from testlodge.models.requirements import RequirementDocumentJSON
from testlodge.models.user import UserJSON


class CaseJSON(TypedDict):

    id: int
    project_id: int
    suite_section_id: int
    position: int
    last_saved_by_id: int
    last_saved_by: UserJSON
    created_at: DateTimeStr
    updated_at: DateTimeStr
    custom_fields: list[CustomFieldJSON]
    requirements: list[RequirementDocumentJSON]
    step_number: str
    title: str
    description: Optional[str]
    test_steps: Optional[str]
    expected_result: Optional[str]


class CaseListJSON(TypedDict):

    pagination: Pagination
    steps: List[CaseJSON]
