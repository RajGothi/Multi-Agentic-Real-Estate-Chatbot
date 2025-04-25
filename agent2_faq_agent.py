from langchain_community.llms import Ollama

llm_faq = Ollama(model="llama3")

def answer_faq(query, context=""):
    # Let the LLM determine if location is mentioned and respond accordingly
    prompt = context + f"\nAnswer this tenancy-related question: '{query}'.\n"
    prompt += "If the user's city or region is not mentioned, politely ask them to provide it for more accurate legal information."

    for chunk in llm_faq.stream(prompt):
        yield chunk.content if hasattr(chunk, 'content') else str(chunk)
