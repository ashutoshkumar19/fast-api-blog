from typing import List
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import get_db
from ..services import blog

router = APIRouter(prefix='/blog', tags=['Blogs'])


@router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all_blogs(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id, db: Session = Depends(get_db), user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog_by_id(id, db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(req: schemas.Blog, db: Session = Depends(get_db),
                user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(req, user, db)


@router.patch('', status_code=status.HTTP_200_OK)
def update_blog_by_id(id, req: schemas.Blog, db: Session = Depends(get_db),
                      user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog_by_id(id, req, db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete_blog_by_id(id, response: Response, db: Session = Depends(get_db),
                      user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog_by_id(id, db)
