from transformers import AutoTokenizer, AutoModelForCausalLM

# Load your LLM model here
model_name = "openlm-research/open_llama_7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

def generate_recipe(ingredients):
    prompt = f"Create a unique recipe using these ingredients: {', '.join(ingredients)}."
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs["input_ids"],
        max_length=150,
        do_sample=True,
        temperature=0.7
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
