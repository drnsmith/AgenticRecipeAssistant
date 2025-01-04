from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from services.recipe_service import generate_recipe

app = FastAPI()

class RecipeRequest(BaseModel):
    ingredients: List[str]
    preferences: dict = None

@app.get("/health-check")
def health_check():
    return {"status": "ok"}

@app.post("/generate-recipe")
def generate_recipe_endpoint(request: RecipeRequest):
    recipe = generate_recipe(request.ingredients)
    return {"recipe": recipe}

@app.post("/suggest-variations")
def suggest_variations(recipe: dict):
    # Placeholder for variation logic
    return {"message": "Suggested variations", "variations": []}
