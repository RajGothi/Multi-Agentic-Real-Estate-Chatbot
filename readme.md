## Tool Tech : 

Hugging Face
Ollama-server (Locally Fast inference)
Langchain (Pipeline)
LLM Model : llama3 (locally deployed to my server)
Image captioning model : Salesforce/blip-image-captioning-base
Gradio (ChatbotUI)

Everything is deployed locally to my server, No use of any paid APIs.


## The logic behind agent switching:

agent_router.py has the logic begind agent switching between issue_detector/remedy and FAQ agent.
Logic : router has llm as classification which decide whether it is "Issue", "FAQ" or "unclear".
    If it is "Issue" then pass to agent1 issue detector/remedy
    else if "FAQ" then pass to agent 2 FAQ 
    else ask question to user again : "Could you clarify if this is about a property issue or tenancy law?"

    If user has uploaded image then we pass to issue_detector(image captioning) followed by LLM for remedy.

## How image-based issue detection works
    If user has uploaded image then we pass to issue_detector(image captioning) followed by LLM for remedy.
    I have used BLIP-image-captioning model which take image as input and give caption of image.
    Then pass to LLM with Caption + prompt ("What are the possible visible or described issues with the property? Suggest remedies.")

## Use case examples covered


## Gradio Link (Active till 72 hours): 


## To run locally: 
Install ollama server (https://ollama.com/) and mentioned libraray in requirements.txt
Run : python app.py


