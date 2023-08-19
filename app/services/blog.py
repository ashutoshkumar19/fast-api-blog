from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models


def get_all_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_blog_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id='{id}' not found")
    return blog


def create_blog(req: schemas.Blog, user: schemas.TokenData, db: Session):
    new_bog = models.Blog(title=req.title, body=req.body, user_id=user.id)
    db.add(new_bog)
    db.commit()
    db.refresh(new_bog)
    return new_bog


def update_blog_by_id(id: int, req: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update({'title': req.title, 'body': req.body})
    db.commit()
    new_blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return {'message': f"Blog with id {id} updated", 'data': new_blog}


def delete_blog_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': f"Blog with id={id} deleted"}
