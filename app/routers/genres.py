from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/genres",
    tags=["genres"],
)

@router.get("/", response_model=List[schemas.Genre])
def read_genres(db: Session = Depends(get_db)):
    return crud.get_genres(db)
