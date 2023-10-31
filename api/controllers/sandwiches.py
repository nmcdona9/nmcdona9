from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def read_all_sandwiches(db: Session) -> list:
    sandwiches = db.query(models.Sandwich).all()
    return sandwiches


def read_one_sandwich(db: Session, sandwich_id: int) -> models.Sandwich:
    sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    return sandwich


def create_sandwich(db: Session, sandwich_data: schemas.SandwichCreate) -> models.Sandwich:
    new_sandwich = models.Sandwich(
        sandwich_name=sandwich_data.sandwich_name,
        price=sandwich_data.price
    )

    db.add(new_sandwich)
    db.commit()
    db.refresh(new_sandwich)

    return new_sandwich

def update_sandwich(db: Session, sandwich_id: int, updated_data: schemas.SandwichUpdate) -> models.Sandwich:
    sandwich_query = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    update_info = updated_data.dict(exclude_unset=True)

    sandwich_query.update(update_info, synchronize_session=False)
    db.commit()

    return sandwich_query.first()
x

def delete_sandwich(db: Session, sandwich_id: int) -> Response:
    sandwich_to_delete = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    sandwich_to_delete.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
