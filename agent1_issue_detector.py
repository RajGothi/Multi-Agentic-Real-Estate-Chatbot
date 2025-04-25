from transformers import BlipProcessor, BlipForConditionalGeneration
from langchain_community.llms import Ollama

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cuda")
llm = Ollama(model="llama3")

def analyze_issue_stream(image_file=None, user_text="", context=""):
    if image_file is not None:
        image = image_file.convert("RGB")
        inputs = processor(image, return_tensors="pt").to("cuda")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        prompt = context + f" The user uploaded an image with the caption: '{caption}'."
        if user_text:
            prompt += f" They also said: '{user_text}'."
    else:
        prompt = context + f"The user reported an issue: '{user_text}'."

    prompt += "What are the possible visible or described issues with the property? Suggest remedies."

    for chunk in llm.stream(prompt):
        yield chunk.content if hasattr(chunk, 'content') else str(chunk)

