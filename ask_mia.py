import streamlit as st
import time
from langchain_groq.chat_models import ChatGroq
from langchain.schema import SystemMessage, HumanMessage



# Simulate typing effect for assistant responses, this will create a more engaging experience and mimic a real conversation.
# This function will yield one character at a time with a delay
def chat_stream(text):
    for char in text:
        yield char
        time.sleep(0.02)

# Save feedback (thumbs up/down)
def save_feedback(index):
    st.session_state.history[index]["feedback"] = st.session_state[f"feedback_{index}"]

def show_ask_mia():
    """
    Renders the MIA Funding Chatbot page.
    """
    st.title("MIA Funding Chatbot")
    st.write("This is a funding chatbot that provides insights and answers to your funding queries.")
    # Ensure chat history is initialized for every session
    if "history" not in st.session_state:
        st.session_state["history"] = []

    # Display chat history (if any)
    for i, message in enumerate(st.session_state.history):
        with st.chat_message(message["role"]):
            st.write(message["content"])
            # Display feedback if available
            if message["role"] == "assistant":
                feedback = message.get("feedback", None)
                st.session_state[f"feedback_{i}"] = feedback
                st.feedback(
                    "thumbs",
                    key=f"feedback_{i}",
                    disabled=feedback is not None,
                    on_change=save_feedback,
                    args=[i],
                )

    # Input from user and response handling
    if prompt := st.chat_input("Type your message here..."):
        # Show user message
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.history.append({"role": "user", "content": prompt})

        # Initialize model
        model = ChatGroq(
            temperature=0.7,
            api_key=st.secrets["GROQ_API_KEY"],
            model_name="llama3-8b-8192"
        )

        # Define assistant's role and behavior
        system_message = SystemMessage(
            content=(
                "You are MIA, a friendly and knowledgeable assistant specialized in funding-related questions. "
                "Only respond to questions that are directly related to funding, such as grants, subsidies, budgeting, or financial support. "
                "Maintain a warm, clear, and professional tone. "
                "If a question is unrelated to funding, politely decline to answer and suggest the user search online or consult a relevant expert. "
                "Do not attempt to answer questions outside your scope, even if you can. Stay strictly within the funding domain."
            )
        )
        user_message = HumanMessage(content=prompt)

        # Generate response from the model
        response_message = model.predict_messages([system_message, user_message])
        response_text = response_message.content

        # Show assistant's response with typing effect
        with st.chat_message("assistant"):
            response = st.write_stream(chat_stream(response_text))

        # Allow feedback for assistant's reply
        st.feedback(
            "thumbs",
            key=f"feedback_{len(st.session_state.history)}",
            on_change=save_feedback,
            args=[len(st.session_state.history)],
        )

        # Save assistant response in chat history
        st.session_state.history.append({"role": "assistant", "content": response_text})
