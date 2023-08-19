from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..services import user

router = APIRouter(prefix='/user', tags=['Users'])


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(req: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(req, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user_by_id(id, db: Session = Depends(get_db)):
    return user.get_user_by_id(id, db)
