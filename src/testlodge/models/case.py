from datetime import datetime
from typing import List
from typing import TypedDict

from testlodge._types import DateTimeStr
from testlodge._types import Pagination
from testlodge.models.custom_field import CustomFieldJSON
from testlodge.models.requirement_document import RequirementDocumentJSON
from testlodge.models.user import UserJSON
from testlodge.models.project import Project
from testlodge.models.suite_section import SuiteSection
from testlodge.models.user import User
from testlodge.models.custom_field import CustomField
from testlodge.models.requirements import RequirementDocument


class CaseJSON(TypedDict):

    id: int
    project_id: int
    suite_section_id: int
    position: int
    last_saved_by_id: int
    last_saved_by: UserJSON
    created_at: DateTimeStr
    updated_at: DateTimeStr
    custom_fields: List[CustomFieldJSON]
    requirements: List[RequirementDocumentJSON]
    step_number: str
    title: str
    description: str
    test_steps: str
    expected_result: str


class CaseListJSON(TypedDict):

    pagination: Pagination
    steps: List[CaseJSON]


class Case:
    """ Represents a TestLodge test case. """

    def __init__(
        self,

        id: int,
        step_number: str,
        title: str,
        description: str,
        steps: str,
        expected_results: str,
        position: int,

        project: Project,
        suite_section: SuiteSection,

        last_saved_by: User,

        created_at: datetime,
        updated_at: datetime,

        custom_fields: List[CustomField],
        requirements: List[RequirementDocument],

    ):
        self._id = id
        self._step_number = step_number
        self._title = title
        self._description = description
        self._steps = steps
        self._expected_results = expected_results
        self._position = position
        self._project = project
        self._suite_section = suite_section
        self._last_saved_by = last_saved_by
        self._created_at = created_at
        self._updated_at = updated_at
        self._custom_fields = custom_fields
        self._requirements = requirements

    @classmethod
    def from_json(cls, json: CaseJSON) -> Case:
        id: int
        project_id: int
        suite_section_id: int
        position: int
        last_saved_by_id: int
        last_saved_by: UserJSON
        created_at: DateTimeStr
        updated_at: DateTimeStr
        custom_fields: List[CustomFieldJSON]
        requirements: List[RequirementDocumentJSON]
        step_number: str
        title: str
        description: str
        test_steps: str
        expected_result: str

        project = Project.from_json(project_id)

        return cls(
            id=json['id'],
