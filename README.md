# 🤖 TalentScout AI Hiring Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hiringassistantchatbot-67.streamlit.app/)

## Project Overview

This project is an intelligent AI Hiring Assistant chatbot created for "TalentScout," a fictional recruitment agency. The chatbot is designed to conduct the initial screening of candidates by gathering essential information and generating relevant technical questions based on the candidate's declared tech stack. This project demonstrates the practical application of Large Language Models (LLMs) in a real-world scenario.

---

## 🚀 Features

* **Interactive Chat Interface**: A clean and user-friendly interface built with Streamlit. 
* **Candidate Information Gathering**: Collects key details like name, contact information, experience, and location. 
* **Dynamic Technical Questions**: Generates 3-5 tailored technical questions based on the candidate's specified tech stack. 
* **Context-Aware Conversations**: Maintains the flow and context of the conversation for a seamless user experience. 
* **Graceful Error Handling**: Includes a fallback mechanism for unexpected user inputs. 

---

## 🛠️ Tech Stack
* **Language**: Python
* **Frontend**: Streamlit
* **LLM**: Google Gemini Pro (via `google-generativeai` library)
* **Environment Management**: `python-dotenv`

---

## ⚙️ Setup and Installation

Follow these steps to set up and run the application locally:

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/aanyashukla/Hiring_Assistant_Chatbot
    cd Hiring_Assistant_Chatbot
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # Create the environment
    python -m venv .venv

    # Activate on Windows
    .\.venv\Scripts\activate

    # Activate on macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    All required libraries are listed in `requirements.txt`. Install them with:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    * Create a file named `.env` in the root of the project.
    * Add your Google Gemini API key to the file:
    ```
    GOOGLE_API_KEY="AIzaSy..."
    ```

5.  **Run the Application**
    ```bash
    streamlit run app.py
    ```
    The application will open in a new tab in your web browser.

---

## 📝 Prompt Design

The chatbot's behavior is guided by a comprehensive **system instruction** provided to the Gemini model. This prompt defines the AI's persona ("Scout," a professional hiring assistant), its mission, and a strict, multi-step process to follow:
1.  **Greet**: Introduce itself and its purpose.
2.  **Collect Information**: Systematically ask for specific candidate details.
3.  **Identify Tech Stack**: Prompt the user to list their technical skills.
4.  **Generate Questions**: Use the tech stack to create relevant questions.
5.  **Conclude**: End the conversation gracefully.

This structured approach ensures the chatbot stays on task and fulfills all requirements of the initial screening process. 

---

## 💡 Challenges & Solutions

During development, several challenges were encountered and resolved:

* **Challenge**: The initial attempt using the OpenAI API was blocked due to their new policy requiring a paid account for API access, even for new users.
* **Solution**: The project was pivoted to use the **Google Gemini API**, which offers a generous and accessible free tier for development.

* **Challenge**: The application encountered `404 Not Found` errors for certain Gemini models (`gemini-1.5-flash`, `gemini-pro`), indicating they were not available for the specific API key.
* **Solution**: A diagnostic script (`check_models.py`) was written to programmatically list all models available to the API key. This allowed for the selection of a confirmed, stable model (`gemini-pro-latest`), ensuring a reliable connection.

* **Challenge**: `ModuleNotFoundError` and other environment issues arose within VS Code.
* **Solution**: The issue was traced to the VS Code interpreter not being correctly pointed to the project's virtual environment. This was resolved by using the **`Python: Select Interpreter`** command in VS Code to correctly link the project to its isolated environment.