# 🛠️ Real Estate Assistant Chatbot

An offline, locally deployed multi-agent chatbot for handling property-related queries and issues using LLMs, image captioning, and agent routing logic.

---

## 🧰 Tech Stack

- **LLM Inference**: [Ollama Server](https://ollama.com/) (Locally hosted, fast inference)  
- **Pipeline Management**: [Langchain](https://www.langchain.com/)  
- **LLM Model**: `llama3` (Locally deployed via Ollama)  
- **Image Captioning Model**: `Salesforce/blip-image-captioning-base`  
- **Chatbot UI**: [Gradio](https://gradio.app/)  
- **Model Hosting**: All models are hosted locally. **No paid APIs used**

---

## 🤖 Agent Switching Logic

The logic for routing between agents is implemented in `agent_router.py`. It uses an LLM to classify the user input into one of the following categories:

- **"Issue"** → Passes the input to **Agent 1** (Issue Detector + Remedy Generator)
- **"FAQ"** → Passes the input to **Agent 2** (FAQ Agent)
- **"Unclear"** → Asks the user:
  > "Could you clarify if this is about a property issue or tenancy law?"

If an image is uploaded, it is routed to image-based issue detection (explained below).

---

## 🖼️ Image-Based Issue Detection

When a user uploads an image:

1. The image is passed to the **BLIP image captioning model** (`Salesforce/blip-image-captioning-base`) to generate a descriptive caption.
2. The caption is combined with the following prompt:  
   _"What are the possible visible or described issues with the property? Suggest remedies."_
3. The caption + prompt is sent to the LLM to generate a response.

**Flow:**

**User Image → Image Captioning (BLIP) → Caption + Prompt → LLM (Remedy Generation)**

---

## ✅ Use Case Examples

- **Property-related FAQs**  
  _Example_: "How do I terminate my lease early?"

- **Issue reporting (text-based)**  
  _Example_: "There’s water leakage near the kitchen ceiling."

- **Image-based issue detection**  
  _Example_: Uploading a photo of wall cracks or mold for automated captioning and remedy suggestions.

---

## 🚀 Gradio Demo

**Live Link (active for 72 hours):**  
*Insert your Gradio link here*

---

## 🛠️ Running Locally

1. **Install Ollama Server**  
   👉 [https://ollama.com/](https://ollama.com/)

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**  
   ```bash
   python app.py
   ```

---

Let me know if you want to add a diagram, Docker setup, or screenshots next!
