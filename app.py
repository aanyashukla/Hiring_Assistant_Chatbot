import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# --- SETUP ---
# Load environment variables from .env file
load_dotenv()

# Configure the Google Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the system prompt
SYSTEM_INSTRUCTION = """
You are "Scout", a friendly and highly professional AI Hiring Assistant for "TalentScout," a recruitment agency specializing in technology placements.

**Your Mission**: Your primary purpose is to conduct an initial screening of engineering candidates. You must remain strictly on topic. Do not answer questions outside of this scope.

**Your Process**:
1.  **Greet**: Start with a warm greeting and briefly state your purpose.
2.  **Collect Information**: You MUST collect the following details one by one: Full Name, Email Address, Phone Number, Years of Experience, Desired Position(s), and Current Location.
3.  **Identify Tech Stack**: After collecting the info, ask the candidate to declare their primary tech stack (programming languages, frameworks, databases).
4.  **Generate Questions**: Based *only* on the declared tech stack, generate exactly 3-5 relevant technical questions to assess their proficiency. Do not ask about anything they didn't mention.
5.  **Conclude**: Once you have asked the questions, thank the candidate for their time and inform them that a recruiter from TalentScout will be in touch if their profile is a good fit.

**Rules**:
- Maintain a coherent, context-aware conversation.
- If the user provides a conversation-ending keyword like "bye" or "exit", end the conversation gracefully.
- If you don't understand a user's input, ask for clarification. Do not deviate from your purpose.
"""

# Initialize the Generative Model
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash",
    system_instruction=SYSTEM_INSTRUCTION
)

# --- STREAMLIT APP INTERFACE ---
st.title("🤖 TalentScout AI Hiring Assistant")
st.write("Welcome! I'm Scout, your AI assistant for the initial screening process.")

# Initialize chat history in session state
if "chat" not in st.session_state:
    # Start a new chat session with the model
    st.session_state.chat = model.start_chat(history=[])
    # Add the initial greeting from the assistant to the display history
    st.session_state.display_history = []
    initial_prompt = "Hello! I'm Scout from TalentScout. I'll be assisting you with the initial screening. To start, could you please tell me your full name?"
    st.session_state.display_history.append({"role": "assistant", "content": initial_prompt})


# Display existing chat messages from our display history
for message in st.session_state.display_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input for the user
if prompt := st.chat_input("Your response..."):
    # Add user's message to the display history and show it
    st.session_state.display_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send the user's message to the Gemini API
    try:
        response = st.session_state.chat.send_message(prompt)

    except Exception:
        fallback_model = genai.GenerativeModel("models/gemini-flash-latest")
        fallback_chat = fallback_model.start_chat(history=st.session_state.chat.history)
        response = fallback_chat.send_message(prompt)
        st.session_state.chat = fallback_chat  # switch session to fallback

    st.session_state.display_history.append({"role": "assistant", "content": response.text})
    st.rerun()