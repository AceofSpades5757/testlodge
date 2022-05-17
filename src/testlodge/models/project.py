from __future__ import __annotations__

from typing import List
from typing import TypedDict
from typing import Union

from testlodge._types import DateTimeStr
from testlodge._types import Pagination


AnyProject = Union[Project, LazyProject]


class ProjectJSON(TypedDict):

    id: int
    name: str
    description: str
    issue_tracker_credential_id: int
    issue_tracker_project_id: str
    created_at: DateTimeStr
    updated_at: DateTimeStr


class ProjectListJSON(TypedDict):

    pagination: Pagination
    steps: List[ProjectJSON]


class Project:
    # TODO
    ...


class LazyProject:
    """Create a project when needed, given a client."""

    def __init__(self, id, client):

        self.id = id
        self.client = client

    def gather(self) -> Project:
        if self.client is None:
            raise AttributeError("Client has not been set.")
        return self.client.project(self.id)
