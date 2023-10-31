from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def read_all_order_details(db: Session) -> list:
    details = db.query(models.OrderDetail).all()
    return details


def read_one_order_detail(db: Session, detail_id: int) -> models.OrderDetail:
    detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id).first()
    return detail


def create_order_detail(db: Session, detail_data: schemas.OrderDetailCreate) -> models.OrderDetail:
    new_order_detail = models.OrderDetail(
        order_id=detail_data.order_id,
        sandwich_id=detail_data.sandwich_id,
        amount=detail_data.amount
    )

    db.add(new_order_detail)
    db.commit()
    db.refresh(new_order_detail)

    return new_order_detail


def update_order_detail(db: Session, detail_id: int, updated_data: schemas.OrderDetailUpdate) -> models.OrderDetail:
    detail_query = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    update_info = updated_data.dict(exclude_unset=True)

    detail_query.update(update_info, synchronize_session=False)
    db.commit()

    return detail_query.first()


def delete_order_detail(db: Session, detail_id: int) -> Response:
    detail_to_delete = db.query(models.OrderDetail).filter(models.OrderDetail.id == detail_id)
    detail_to_delete.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
