# Use the explicit AutoTokenizer and AutoModelForSeq2SeqLM classes. 
# This guarantees that your model runs correctly regardless of internal pipeline task mappings.

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# 1. Load the tokenizer and model explicitly
model_name = "Harsh-Gupta/t5-small-news-summarizer"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 2. Add the mandatory T5 task prefix
text = "summarize: SpaceX launched its Falcon 9 rocket from Florida on Tuesday. The rocket successfully delivered a new batch of communication satellites into orbit. Engineers confirmed all systems functioned normally after liftoff."

# 3. Tokenize input text
inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)

# 4. Generate the summary with clean decoding constraints
outputs = model.generate(
    **inputs, 
    max_new_tokens=20, 
    #num_beams=4,          # Uses beam search for higher-quality, cohesive phrases
    #early_stopping=True   # Stops generating as soon as the model finishes a clean sentence
)

# 5. Decode and print the clean summary
summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(summary)