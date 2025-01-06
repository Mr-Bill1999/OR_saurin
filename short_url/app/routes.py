from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from app import crud, schemas
from app.database import get_db
from typing import List


router = APIRouter()

@router.get("/all", response_model=List[schemas.URLStats])
def get_all_urls(db: Session = Depends(get_db)):
    db_urls = crud.get_all_urls(db)
    return db_urls

@router.post("/shorten", response_model=schemas.URLStats)
def shorten_url(url_data: schemas.URLCreate, db: Session = Depends(get_db)):
    db_url = crud.create_short_url(db, url_data.url)
    return db_url

@router.get("/{short_id}", response_class=RedirectResponse)
def redirect_to_url(short_id: str, db: Session = Depends(get_db)):
    db_url = crud.get_full_url(db, short_id)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=db_url.full_url, status_code=303)


@router.get("/stats/{short_id}", response_model=schemas.URLStats)
def get_url_stats(short_id: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_stats(db, short_id)
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return db_url
