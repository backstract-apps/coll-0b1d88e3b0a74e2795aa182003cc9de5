from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.delete('/projects/id')
async def delete_projects_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_projects_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/')
async def get_tasks(db: Session = Depends(get_db)):
    try:
        return await service.get_tasks(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/id')
async def get_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/photos/id')
async def delete_photos_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_photos_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/collaborators/')
async def get_collaborators(db: Session = Depends(get_db)):
    try:
        return await service.get_collaborators(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/collaborators/id')
async def get_collaborators_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_collaborators_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/collaborators/')
async def post_collaborators(raw_data: schemas.PostCollaborators, db: Session = Depends(get_db)):
    try:
        return await service.post_collaborators(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/collaborators/id/')
async def put_collaborators_id(id: str, project_id: str, user_id: str, role: str, created_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_collaborators_id(db, id, project_id, user_id, role, created_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/collaborators/id')
async def delete_collaborators_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_collaborators_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tasks/')
async def post_tasks(raw_data: schemas.PostTasks, db: Session = Depends(get_db)):
    try:
        return await service.post_tasks(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tasks/id/')
async def put_tasks_id(id: str, project_id: str, title: str, description: str, is_complete: str, order_index: int, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_tasks_id(db, id, project_id, title, description, is_complete, order_index, created_at, updated_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tasks/id')
async def delete_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/materials/')
async def get_materials(db: Session = Depends(get_db)):
    try:
        return await service.get_materials(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/materials/id')
async def get_materials_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_materials_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/materials/')
async def post_materials(raw_data: schemas.PostMaterials, db: Session = Depends(get_db)):
    try:
        return await service.post_materials(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/materials/id/')
async def put_materials_id(id: str, project_id: str, name: str, quantity: float, unit: str, price: float, purchased: str, created_at: str, updated_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_materials_id(db, id, project_id, name, quantity, unit, price, purchased, created_at, updated_at)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/materials/id')
async def delete_materials_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_materials_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/photos/')
async def get_photos(db: Session = Depends(get_db)):
    try:
        return await service.get_photos(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/photos/id')
async def get_photos_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_photos_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/photos/')
async def post_photos(raw_data: schemas.PostPhotos, db: Session = Depends(get_db)):
    try:
        return await service.post_photos(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/photos/id/')
async def put_photos_id(id: str, task_id: str, url: str, caption: str, created_at: str, db: Session = Depends(get_db)):
    try:
        return await service.put_photos_id(db, id, task_id, url, caption, created_at)
    except Exception as e:
        raise HTTPException(500, str(e))

