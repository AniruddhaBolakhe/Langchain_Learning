from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chatllm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
result = chatllm.invoke("What is the capital of India")
print(result)
#the result is not a simple plain text
print(result.content) # only to see the answer