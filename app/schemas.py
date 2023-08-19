from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class Blog(BaseModel):
    id: int
    title: str
    body: str


# ==========================================================


class ShowUser(BaseModel):
    id: int
    name: str
    email: str

    blogs: List[Blog]


class ShowBlogUser(BaseModel):
    id: int
    name: str
    email: str


class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    user: ShowBlogUser

    class Config:
        # orm_mode = True
        from_attributes = True


# ==========================================================


class Login(BaseModel):
    username: str
    password: str


# ==========================================================


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
