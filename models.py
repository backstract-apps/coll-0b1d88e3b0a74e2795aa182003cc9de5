from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Projects(Base):
    __tablename__ = 'projects'
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, primary_key=False)
    title = Column(String, primary_key=False)
    description = Column(String, primary_key=False)
    cover_image = Column(String, primary_key=False)
    inspiration_image = Column(String, primary_key=False)
    status = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)
    is_public = Column(Boolean, primary_key=False)
    share_code = Column(String, primary_key=False)


class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(UUID, primary_key=True)
    project_id = Column(UUID, primary_key=False)
    title = Column(String, primary_key=False)
    description = Column(String, primary_key=False)
    is_complete = Column(Boolean, primary_key=False)
    order_index = Column(Integer, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)


class Materials(Base):
    __tablename__ = 'materials'
    id = Column(UUID, primary_key=True)
    project_id = Column(UUID, primary_key=False)
    name = Column(String, primary_key=False)
    quantity = Column(String, primary_key=False)
    unit = Column(String, primary_key=False)
    price = Column(String, primary_key=False)
    purchased = Column(Boolean, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)


class Photos(Base):
    __tablename__ = 'photos'
    id = Column(UUID, primary_key=True)
    task_id = Column(UUID, primary_key=False)
    url = Column(String, primary_key=False)
    caption = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)


class Collaborators(Base):
    __tablename__ = 'collaborators'
    id = Column(UUID, primary_key=True)
    project_id = Column(UUID, primary_key=False)
    user_id = Column(UUID, primary_key=False)
    role = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)


