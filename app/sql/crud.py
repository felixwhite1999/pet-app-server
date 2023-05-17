from sqlalchemy.orm import Session
from . import models, schemas


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit() #saves on disk
    db.refresh(db_user) #refresh instance so that new additions (like new id) take effect in code as well
    return db_user



def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post_by_id(db: Session, id: int):
    return db.query(models.Post).filter(models.Post.id == id).first()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post_replies(db: Session, postid: int):
    return db.query(models.Post).filter(models.Post.response_to == postid).all()