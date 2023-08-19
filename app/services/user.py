from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db
from ..hashing import Hash

router = APIRouter(prefix='/user', tags=['users'])


def create_user(req: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=req.name, email=req.email, password=Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id='{id}' not found")
    return user
