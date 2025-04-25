from agent1_issue_detector import analyze_issue_stream
from agent2_faq_agent import answer_faq
from langchain_community.llms import Ollama

llm_router = Ollama(model="llama3")

def route_query_stream(image, query, context=""):
    if image:
        yield from analyze_issue_stream(image, query, context)
    elif query:
        classification_prompt = (
            context
            + f"\nDecide if the user's message is about a property issue (e.g., water damage, mold, cracks, poor lighting, broken fixtures) or tenancy law related FAQ (e.g., rent, landlord rights, agreements, tenant responsibilities, and rental processes.)."
            + f"\nMessage: '{query}'"
            + "\nRespond with either 'issue', 'FAQ', or 'unclear'."
        )

        classification = llm_router.invoke(classification_prompt).strip().lower()
        print("classification", classification)
        if "issue" in classification:
            yield from analyze_issue_stream(None, query, context)
        elif "FAQ" in classification:
            yield from answer_faq(query, context)
        else:
            yield "Could you clarify if this is about a property issue or tenancy law?"
    else:
        yield "Please upload an image or provide a question."
