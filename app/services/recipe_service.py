from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the OpenLLaMA model and tokenizer globally
model_name = "openlm-research/open_llama_7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

def generate_recipe(ingredients):
    prompt = f"Create a unique recipe using the following ingredients: {', '.join(ingredients)}. Provide a title, list of ingredients with quantities, and step-by-step instructions."
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs['input_ids'], max_length=200, do_sample=True, temperature=0.7)
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return recipe

def suggest_variations(recipe):
    prompt = f"Suggest three variations for this recipe: {recipe}"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs['input_ids'], max_length=150, do_sample=True, temperature=0.7)
    variations = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return variations.split("\n")
