from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Projects(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    description: str
    cover_image: str
    inspiration_image: str
    status: str
    created_at: datetime.time
    updated_at: datetime.time
    is_public: bool
    share_code: str


class ReadProjects(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    description: str
    cover_image: str
    inspiration_image: str
    status: str
    created_at: datetime.time
    updated_at: datetime.time
    is_public: bool
    share_code: str
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    title: str
    description: str
    is_complete: bool
    order_index: int
    created_at: datetime.time
    updated_at: datetime.time


class ReadTasks(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    title: str
    description: str
    is_complete: bool
    order_index: int
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True


class Materials(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    quantity: float
    unit: str
    price: float
    purchased: bool
    created_at: datetime.time
    updated_at: datetime.time


class ReadMaterials(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    name: str
    quantity: float
    unit: str
    price: float
    purchased: bool
    created_at: datetime.time
    updated_at: datetime.time
    class Config:
        from_attributes = True


class Photos(BaseModel):
    id: uuid.UUID
    task_id: uuid.UUID
    url: str
    caption: str
    created_at: datetime.time


class ReadPhotos(BaseModel):
    id: uuid.UUID
    task_id: uuid.UUID
    url: str
    caption: str
    created_at: datetime.time
    class Config:
        from_attributes = True


class Collaborators(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    user_id: uuid.UUID
    role: str
    created_at: datetime.time


class ReadCollaborators(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    user_id: uuid.UUID
    role: str
    created_at: datetime.time
    class Config:
        from_attributes = True




class PostCollaborators(BaseModel):
    id: Any
    project_id: Any
    user_id: Any
    role: str
    created_at: Any

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    id: Any
    project_id: Any
    title: str
    description: str
    is_complete: bool
    order_index: int
    created_at: Any
    updated_at: Any

    class Config:
        from_attributes = True



class PostMaterials(BaseModel):
    id: Any
    project_id: Any
    name: str
    quantity: Any
    unit: str
    price: Any
    purchased: bool
    created_at: Any
    updated_at: Any

    class Config:
        from_attributes = True



class PostPhotos(BaseModel):
    id: Any
    task_id: Any
    url: str
    caption: str
    created_at: Any

    class Config:
        from_attributes = True

