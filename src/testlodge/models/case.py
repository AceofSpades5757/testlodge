from __future__ import __annotations__

from datetime import datetime
from typing import List
from typing import TypedDict

from testlodge._types import DateTimeStr
from testlodge._types import Pagination
from testlodge.client import Client
from testlodge.models.base import BaseModel
from testlodge.models.case import Case
from testlodge.models.custom_field import CustomField
from testlodge.models.custom_field import CustomFieldJSON
from testlodge.models.project import AnyProject
from testlodge.models.project import LazyProject
from testlodge.models.requirement import Requirement
from testlodge.models.requirement_document import RequirementDocumentJSON
from testlodge.models.suite_section import AnySuiteSection
from testlodge.models.suite_section import LazySuiteSection
from testlodge.models.suite_section import SuiteSection
from testlodge.models.user import User
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


class Case(BaseModel):
    """Represents a TestLodge test case."""

    def __init__(
        self,
        id: int,
        step_number: str,
        title: str,
        description: str,
        steps: str,
        expected_results: str,
        position: int,
        project: AnyProject,
        suite_section: AnySuiteSection,
        last_saved_by: User,
        created_at: datetime,
        updated_at: datetime,
        custom_fields: List[CustomField],
        requirements: List[RequirementDocument],
        client: Client = None,
    ):
        self._id = id
        self._step_number = step_number
        self.title = title
        self.description = description
        self.steps = steps
        self.expected_results = expected_results
        self._position = position
        self._project = project
        self._suite_section = suite_section
        self._last_saved_by = last_saved_by
        self._created_at = created_at
        self._updated_at = updated_at
        self.custom_fields = custom_fields
        self._requirements = requirements

        self._client = client

    @property
    def id(self):
        return self._id

    @property
    def step_number(self):
        return self._step_number

    @property
    def position(self):
        return self._position

    @property
    def project(self):
        return self._project

    @property
    def suite_section(self):
        return self._suite_section

    @property
    def last_saved_by(self):
        return self._last_saved_by

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def requirements(self):
        return self._requirements

    @classmethod
    def from_json(cls, json: CaseJSON, client: Client = None) -> Case:

        # custom_fields: List[CustomFieldJSON]
        # NOT Document
        # requirements: List[RequirementJSON]

        custom_fields: List[CustomField] = [
            CustomField.from_json(cf_json) for cf_json in json['custom_fields']
        ]
        requirements: List[Requirement] = [
            CustomField.from_json(cf_json) for cf_json in json['requirements']
        ]

        project = LazyProject(id=json['project_id'], client=client)
        suite_section = LazySuiteSection(
            id=json['suite_section_id'], client=client
        )
        # last_saved_by_id: int
        last_saved_by = User.from_json(json['last_saved_by'])

        created_at = cls.str_to_datetime(json['created_at'])
        updated_at = cls.str_to_datetime(json['updated_at'])

        return cls(
            id=json['id'],
            position=json['position'],
            step_number=json['step_number'],
            title=json['title'],
            description=json['description'],
            steps=json['test_steps'],
            expected_results=json['expected_result'],
            project=project,
            suite_section=suite_section,
            last_saved_by=last_saved_by,
            created_at=created_at,
            updated_at=updated_at,
            client=client,
            custom_fields=custom_fields,
            requirements=requirements,
        )
