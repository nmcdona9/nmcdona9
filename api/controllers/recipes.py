from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def read_all_recipes(db: Session) -> list:
    recipes = db.query(models.Recipe).all()
    return recipes


def read_one_recipe(db: Session, recipe_id: int) -> models.Recipe:
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    return recipe


def create_recipe(db: Session, recipe_data: schemas.RecipeCreate) -> models.Recipe:
    new_recipe = models.Recipe(
        sandwich_id=recipe_data.sandwich_id,
        resource_id=recipe_data.resource_id,
        amount=recipe_data.amount
    )

    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)

    return new_recipe


def update_recipe(db: Session, recipe_id: int, updated_recipe: schemas.RecipeUpdate) -> models.Recipe:
    recipe_query = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    update_data = updated_recipe.dict(exclude_unset=True)

    recipe_query.update(update_data, synchronize_session=False)
    db.commit()

    return recipe_query.first()


def delete_recipe(db: Session, recipe_id: int) -> Response:
    recipe_to_delete = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    recipe_to_delete.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
