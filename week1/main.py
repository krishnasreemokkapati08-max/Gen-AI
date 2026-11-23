import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")

client = genai.Client(api_key=api_key)

print("Sending request to Gemini...")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is Artificial Intelligence? Explain in simple words."
)

print("\nLLM Response:")
print(interaction.output_text)