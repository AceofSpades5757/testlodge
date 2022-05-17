from typing import List
from typing import Optional
from typing import TypedDict

from testlodge._types import DateTimeStr
from testlodge._types import Pagination
from testlodge.models.custom_field import CustomFieldJSON
from testlodge.models.user import UserJSON


class PathJSON(TypedDict):
    name: str
    geometry: Optional[str]
    url: str


class PathsJSON(TypedDict):
    original: PathJSON
    thumbnail: PathJSON


class UploadJSON(TypedDict):

    id: int
    file_name: str
    # MIME Type
    content_type: str
    paths: PathsJSON


class RequirementJSON(TypedDict):

    id: int
    requirement_number: str
    title: str
    description: str
    position: int
    requirement_document_id: int
    last_saved_by_id: int
    last_saved_by: UserJSON
    requirement_uploads: List[UploadJSON]
    custom_fields: List[CustomFieldJSON]
    created_at: DateTimeStr
    updated_at: DateTimeStr


class RequirementListJSON(TypedDict):

    pagination: Pagination
    requirements: List[RequirementJSON]


class Requirement:
    # TODO
    ...
