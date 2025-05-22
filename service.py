from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def delete_projects_id(db: Session, id: int):

    projects_deleted = None
    record_to_delete = db.query(models.Projects).filter(models.Projects.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        projects_deleted = record_to_delete.to_dict() 

    res = {
        'projects_deleted': projects_deleted,
    }
    return res

async def get_tasks(db: Session):

    tasks_all = db.query(models.Tasks).all()
    tasks_all = [new_data.to_dict() for new_data in tasks_all] if tasks_all else tasks_all

    res = {
        'tasks_all': tasks_all,
    }
    return res

async def get_tasks_id(db: Session, id: int):

    tasks_one = db.query(models.Tasks).filter(models.Tasks.id == id).first() 
    tasks_one = tasks_one.to_dict() if tasks_one else tasks_one

    res = {
        'tasks_one': tasks_one,
    }
    return res

async def delete_photos_id(db: Session, id: int):

    photos_deleted = None
    record_to_delete = db.query(models.Photos).filter(models.Photos.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        photos_deleted = record_to_delete.to_dict() 

    res = {
        'photos_deleted': photos_deleted,
    }
    return res

async def get_collaborators(db: Session):

    collaborators_all = db.query(models.Collaborators).all()
    collaborators_all = [new_data.to_dict() for new_data in collaborators_all] if collaborators_all else collaborators_all

    res = {
        'collaborators_all': collaborators_all,
    }
    return res

async def get_collaborators_id(db: Session, id: int):

    collaborators_one = db.query(models.Collaborators).filter(models.Collaborators.id == id).first() 
    collaborators_one = collaborators_one.to_dict() if collaborators_one else collaborators_one

    res = {
        'collaborators_one': collaborators_one,
    }
    return res

async def post_collaborators(db: Session, raw_data: schemas.PostCollaborators):
    id:uuid.UUID = raw_data.id
    project_id:uuid.UUID = raw_data.project_id
    user_id:uuid.UUID = raw_data.user_id
    role:str = raw_data.role
    created_at:datetime.datetime = raw_data.created_at


    record_to_be_added = {'id': id, 'role': role, 'user_id': user_id, 'created_at': created_at, 'project_id': project_id}
    new_collaborators = models.Collaborators(**record_to_be_added)
    db.add(new_collaborators)
    db.commit()
    db.refresh(new_collaborators)
    collaborators_inserted_record = new_collaborators.to_dict()

    res = {
        'collaborators_inserted_record': collaborators_inserted_record,
    }
    return res

async def put_collaborators_id(db: Session, id: str, project_id: str, user_id: str, role: str, created_at: str):

    collaborators_edited_record = db.query(models.Collaborators).filter(models.Collaborators.id == id).first()
    for key, value in {'id': id, 'role': role, 'user_id': user_id, 'created_at': created_at, 'project_id': project_id}.items():
          setattr(collaborators_edited_record, key, value)
    db.commit()
    db.refresh(collaborators_edited_record)
    collaborators_edited_record = collaborators_edited_record.to_dict() 

    res = {
        'collaborators_edited_record': collaborators_edited_record,
    }
    return res

async def delete_collaborators_id(db: Session, id: int):

    collaborators_deleted = None
    record_to_delete = db.query(models.Collaborators).filter(models.Collaborators.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        collaborators_deleted = record_to_delete.to_dict() 

    res = {
        'collaborators_deleted': collaborators_deleted,
    }
    return res

async def post_tasks(db: Session, raw_data: schemas.PostTasks):
    id:uuid.UUID = raw_data.id
    project_id:uuid.UUID = raw_data.project_id
    title:str = raw_data.title
    description:str = raw_data.description
    is_complete:bool = raw_data.is_complete
    order_index:int = raw_data.order_index
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at


    record_to_be_added = {'id': id, 'title': title, 'created_at': created_at, 'project_id': project_id, 'updated_at': updated_at, 'description': description, 'is_complete': is_complete, 'order_index': order_index}
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    tasks_inserted_record = new_tasks.to_dict()

    res = {
        'tasks_inserted_record': tasks_inserted_record,
    }
    return res

async def put_tasks_id(db: Session, id: str, project_id: str, title: str, description: str, is_complete: str, order_index: int, created_at: str, updated_at: str):

    tasks_edited_record = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    for key, value in {'id': id, 'title': title, 'created_at': created_at, 'project_id': project_id, 'updated_at': updated_at, 'description': description, 'is_complete': is_complete, 'order_index': order_index}.items():
          setattr(tasks_edited_record, key, value)
    db.commit()
    db.refresh(tasks_edited_record)
    tasks_edited_record = tasks_edited_record.to_dict() 

    res = {
        'tasks_edited_record': tasks_edited_record,
    }
    return res

async def delete_tasks_id(db: Session, id: int):

    tasks_deleted = None
    record_to_delete = db.query(models.Tasks).filter(models.Tasks.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tasks_deleted = record_to_delete.to_dict() 

    res = {
        'tasks_deleted': tasks_deleted,
    }
    return res

async def get_materials(db: Session):

    materials_all = db.query(models.Materials).all()
    materials_all = [new_data.to_dict() for new_data in materials_all] if materials_all else materials_all

    res = {
        'materials_all': materials_all,
    }
    return res

async def get_materials_id(db: Session, id: int):

    materials_one = db.query(models.Materials).filter(models.Materials.id == id).first() 
    materials_one = materials_one.to_dict() if materials_one else materials_one

    res = {
        'materials_one': materials_one,
    }
    return res

async def post_materials(db: Session, raw_data: schemas.PostMaterials):
    id:uuid.UUID = raw_data.id
    project_id:uuid.UUID = raw_data.project_id
    name:str = raw_data.name
    quantity:float = raw_data.quantity
    unit:str = raw_data.unit
    price:float = raw_data.price
    purchased:bool = raw_data.purchased
    created_at:datetime.datetime = raw_data.created_at
    updated_at:datetime.datetime = raw_data.updated_at


    record_to_be_added = {'id': id, 'name': name, 'unit': unit, 'price': price, 'quantity': quantity, 'purchased': purchased, 'created_at': created_at, 'project_id': project_id, 'updated_at': updated_at}
    new_materials = models.Materials(**record_to_be_added)
    db.add(new_materials)
    db.commit()
    db.refresh(new_materials)
    materials_inserted_record = new_materials.to_dict()

    res = {
        'materials_inserted_record': materials_inserted_record,
    }
    return res

async def put_materials_id(db: Session, id: str, project_id: str, name: str, quantity: float, unit: str, price: float, purchased: str, created_at: str, updated_at: str):

    materials_edited_record = db.query(models.Materials).filter(models.Materials.id == id).first()
    for key, value in {'id': id, 'name': name, 'unit': unit, 'price': price, 'quantity': quantity, 'purchased': purchased, 'created_at': created_at, 'project_id': project_id, 'updated_at': updated_at}.items():
          setattr(materials_edited_record, key, value)
    db.commit()
    db.refresh(materials_edited_record)
    materials_edited_record = materials_edited_record.to_dict() 

    res = {
        'materials_edited_record': materials_edited_record,
    }
    return res

async def delete_materials_id(db: Session, id: int):

    materials_deleted = None
    record_to_delete = db.query(models.Materials).filter(models.Materials.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        materials_deleted = record_to_delete.to_dict() 

    res = {
        'materials_deleted': materials_deleted,
    }
    return res

async def get_photos(db: Session):

    photos_all = db.query(models.Photos).all()
    photos_all = [new_data.to_dict() for new_data in photos_all] if photos_all else photos_all

    res = {
        'photos_all': photos_all,
    }
    return res

async def get_photos_id(db: Session, id: int):

    photos_one = db.query(models.Photos).filter(models.Photos.id == id).first() 
    photos_one = photos_one.to_dict() if photos_one else photos_one

    res = {
        'photos_one': photos_one,
    }
    return res

async def post_photos(db: Session, raw_data: schemas.PostPhotos):
    id:uuid.UUID = raw_data.id
    task_id:uuid.UUID = raw_data.task_id
    url:str = raw_data.url
    caption:str = raw_data.caption
    created_at:datetime.datetime = raw_data.created_at


    record_to_be_added = {'id': id, 'url': url, 'caption': caption, 'task_id': task_id, 'created_at': created_at}
    new_photos = models.Photos(**record_to_be_added)
    db.add(new_photos)
    db.commit()
    db.refresh(new_photos)
    photos_inserted_record = new_photos.to_dict()

    res = {
        'photos_inserted_record': photos_inserted_record,
    }
    return res

async def put_photos_id(db: Session, id: str, task_id: str, url: str, caption: str, created_at: str):

    photos_edited_record = db.query(models.Photos).filter(models.Photos.id == id).first()
    for key, value in {'id': id, 'url': url, 'caption': caption, 'task_id': task_id, 'created_at': created_at}.items():
          setattr(photos_edited_record, key, value)
    db.commit()
    db.refresh(photos_edited_record)
    photos_edited_record = photos_edited_record.to_dict() 

    res = {
        'photos_edited_record': photos_edited_record,
    }
    return res

