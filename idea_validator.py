import streamlit as st
import re
# placing packages
from langchain_groq import ChatGroq
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA


def save_feedback_idea(value):
    st.session_state.idea_feedback = value

def show_idea_validator():
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None
    if "idea_feedback" not in st.session_state:
        st.session_state.idea_feedback = None

    st.title("Establish your innovative idea")
    st.write(
        "MediacampusNL connects you with partners. Your data remains private, "
        "in your control, and will not be used to train AI. Your idea will be assessed "
        "based on carefully developed criteria, created by professionals with expertise in the field."
    )

    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

    if uploaded_file and st.session_state.qa_chain is None:
        text = uploaded_file.read().decode("utf-8", errors="ignore")

        errors = []
        if not text.strip():
            errors.append("The file is empty.")
        if len(text) < 100:
            errors.append("The document must have at least 100 characters.")
        else:
            st.success("Document processed successfully.")

        documents = [text]
        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.create_documents(documents)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = Chroma.from_documents(texts, embeddings)
        retriever = db.as_retriever()

        llm = ChatGroq(
            groq_api_key=st.secrets["GROQ_API_KEY"],
            model="llama3-8b-8192"
        )

        st.session_state.qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
        st.session_state.llm = llm
        st.session_state.document_text = text

    if "document_text" in st.session_state:
        st.subheader("Validate your idea based on Impact/Effort model")
        idea_text = st.text_area("Review or edit your idea before validation", st.session_state.document_text)

        if st.button("Validate Idea"):
            validation_prompt = f"""
You are an AI agent evaluating innovative ideas using the Impact/Effort model for Dutch media innovation. Your task is to analyze the provided idea and classify it based on its potential impact and effort required for implementation.
Keep the following in mind that the user can be sensitive about their idea, so be respectful and constructive in your feedback.
If the idea is not for the media industry, politely inform the user that you can only validate ideas related to media innovation.
Analyze the following idea:
\"\"\"{idea_text}\"\"\"

1. Assess the **Impact**: Is it High, Medium, or Low?
2. Assess the **Effort**: Is it High, Medium, or Low?
3. Based on your assessment, classify the idea into one of these categories:
   - Quick Win: High Impact / Low Effort
   - Big Bet: High Impact / High Effort
   - Nice to Have: Low Impact / Low Effort
   - Resource Drainer: Low Impact / High Effort

Then:
- Justify the classification with clear reasoning.
- If the idea is not a Quick Win or Big Bet, suggest improvements to increase Impact or reduce Effort.

Respond in this format:
Impact: [High/Medium/Low] - [Reason]  
Effort: [High/Medium/Low] - [Reason]  
Classification: [Quadrant name]  
Justification: [Explanation]  
Suggestions: [Provide specific, concrete suggestions extracted from the idea text to improve it, formatted as a bullet list and give reasoning for each suggestion]
"""
            response = st.session_state.llm.invoke(validation_prompt)
            result = response if isinstance(response, str) else getattr(response, "content", str(response))

            st.subheader("Validation Result")
            st.markdown(result)
            # Show feedback buttons or existing feedback message
            if st.session_state.idea_feedback is None:
                col1, col2, col3, col4 = st.columns(4)
                if col1.button("Helpful"):
                    save_feedback_idea("Helpful")
                if col2.button("Inaccurate or Misinterpreted"):
                    save_feedback_idea("Inaccurate or Misinterpreted")
                if col3.button("Too Vague or Unhelpful"):
                    save_feedback_idea("Too Vague or Unhelpful")
                if col4.button("Request Review from MediacampusNL"):
                    save_feedback_idea("Request Review from MediacampusNL")
            else:
                st.info(f"Your feedback: **{st.session_state.idea_feedback}**")
