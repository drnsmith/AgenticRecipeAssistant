from pydantic import BaseModel
from typing import List

class IngredientsRequest(BaseModel):
    ingredients: List[str]

class RecipeResponse(BaseModel):
    recipe: str

class VariationsRequest(BaseModel):
    recipe_id: int

class VariationsResponse(BaseModel):
    variations: List[str]
