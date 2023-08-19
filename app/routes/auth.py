from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import schemas
from ..database import get_db
from ..services import auth

router = APIRouter(prefix='/auth', tags=['Authentication'])


@router.post('/login', status_code=status.HTTP_200_OK, response_model=schemas.Token)
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth.login(req, db)
