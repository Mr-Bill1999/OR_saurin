import uuid
from sqlalchemy.orm import Session
from app import models

def generate_short_id():
    return str(uuid.uuid4())[:10]

def get_all_urls(db: Session):
    return db.query(models.URL).all()

def create_short_url(db: Session, url: str):
    # Проверяем, существует ли уже такая ссылка
    existing_url = db.query(models.URL).filter(models.URL.full_url == url).first()
    if existing_url:
        return existing_url

    short_url = generate_short_id()
    new_url = models.URL(full_url=url, short_id=short_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url


def get_full_url(db: Session, short_id: str):
    return db.query(models.URL).filter(models.URL.short_id == short_id).first()

def get_url_stats(db: Session, short_id: str):
    return db.query(models.URL).filter(models.URL.short_id == short_id).first()
