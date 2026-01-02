from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/directors",
    tags=["directors"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{director_id}", response_model=schemas.DirectorDetail)
def read_director(director_id: int, db: Session = Depends(get_db)):
    director = crud.get_director(db, director_id=director_id)
    if director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return director
