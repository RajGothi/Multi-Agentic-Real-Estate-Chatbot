import gradio as gr
from agent_router import route_query_stream

def style_message(role, text):
    if role == "user":
        return f'<div style="display:inline-block; background-color:#004D40; color:#FFFFFF; padding:10px; border-radius:10px; ">{text}</div>'
    elif role == "assistant":
        return f'<div style="display:inline-block; background-color:#1A237E; color:#FFFFFF; padding:10px; border-radius:10px; ">{text}</div>'
    else:
        return f'<div style="display:inline-block; background-color:#BF360C; color:#FFFFFF; padding:10px; border-radius:10px; ">{text}</div>'

def chatbot_interface_stream(image, text, history):
    if not image and not text:
        yield history + [gr.ChatMessage(role="system", content="Please upload an image or enter a question.")]
    else:
        # Ensure history is always in ChatMessage format, not dictionaries
        formatted_history = []
        for msg in history:
            if isinstance(msg, dict):
                formatted_history.append(gr.ChatMessage(role=msg['role'], content=msg['content']))
            else:
                formatted_history.append(msg)
        
        context = "\n".join([f"User: {msg.content}" if msg.role == "user" else f"Assistant: {msg.content}" for msg in formatted_history])
        context += f"\nUser: {text}"


        response = ""
        for chunk in route_query_stream(image=image, query=text, context=context):
            response += chunk
            formatted = formatted_history + [
                gr.ChatMessage(role="user", content=style_message("user", text)),
                gr.ChatMessage(role="assistant", content=style_message("assistant", response))
            ]
            yield formatted

description = """
## 🏠 Multi-Agent Real Estate Assistant
Chat with our assistant about property issues or tenancy FAQs.
Upload an image or ask a question. You can follow up for more help!
"""

with gr.Blocks(theme=gr.themes.Default(primary_hue="indigo")) as demo:
    gr.Markdown(description)
    chatbot = gr.Chatbot(type="messages")  # Keeps the structure you requested
    with gr.Row():
        image_input = gr.Image(type="pil", label="Upload a property image (optional)")
        text_input = gr.Textbox(lines=2, placeholder="Enter your question or describe the issue")
    submit_btn = gr.Button("Submit")
    state = gr.State([])  # Initialize state to an empty list to store the history

    submit_btn.click(
        fn=chatbot_interface_stream,
        inputs=[image_input, text_input, state],
        outputs=[chatbot],
        show_progress=True
    ).then(lambda messages: messages, inputs=[chatbot], outputs=state)

demo.launch(share=True)