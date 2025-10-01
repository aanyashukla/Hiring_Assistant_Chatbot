import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Checking for available models that support 'generateContent'...\n")

# List all available models and check their supported methods
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)