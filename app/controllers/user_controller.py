from sqlalchemy.orm import Session

from models import user_model
from schemas import user_schema


def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.User):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = user_model.User(
        user_name=user.user_name,
        email=user.email,
        password=fake_hashed_password,
        age=user.age

    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user