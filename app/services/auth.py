from datetime import timedelta

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db
from ..hashing import Hash
from ..jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix='/user', tags=['users'])


def login(req: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user or not Hash.verify(req.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
    # return user
