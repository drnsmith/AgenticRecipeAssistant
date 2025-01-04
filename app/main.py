from fastapi import FastAPI
from app.services.recipe_service import generate_recipe, suggest_variations

app = FastAPI()

@app.get("/health-check")
def health_check():
    return {"status": "ok"}

@app.post("/generate-recipe")
def generate_recipe_endpoint(ingredients: list[str]):
    recipe = generate_recipe(ingredients)
    return {"recipe": recipe}

@app.post("/suggest-variations")
def suggest_variations_endpoint(recipe: dict):
    variations = suggest_variations(recipe)
    return {"variations": variations}

