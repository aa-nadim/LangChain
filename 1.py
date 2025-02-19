from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create a ChatGoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model="gemini-pro")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
