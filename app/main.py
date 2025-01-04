from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# FastAPI app instance
app = FastAPI()

# Load OpenLLaMA model and tokenizer
model_name = "openlm-research/open_llama_7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    offload_folder="/Volumes/LaCie/AgenticModels/offload"
)

# Input schema for recipe generation
class RecipeRequest(BaseModel):
    ingredients: str

# Recipe generation endpoint
@app.post("/generate-recipe")
async def generate_recipe(request: RecipeRequest):
    prompt = f"""
    Create a unique recipe using the following ingredients: {request.ingredients}.
    Provide a title, list of ingredients with quantities, and step-by-step instructions.
    """
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    with torch.no_grad():
        outputs = model.generate(
            inputs['input_ids'],
            max_length=150,
            do_sample=True,
            temperature=0.7
        )
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"recipe": recipe}


