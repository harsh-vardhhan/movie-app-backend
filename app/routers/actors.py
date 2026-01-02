from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter(
    prefix="/actors",
    tags=["actors"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{actor_id}", response_model=schemas.ActorDetail)
def read_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = crud.get_actor(db, actor_id=actor_id)
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor
