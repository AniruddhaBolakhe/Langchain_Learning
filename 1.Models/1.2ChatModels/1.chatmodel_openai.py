from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
#temperature parameter is from 0 to 2
chatllm = ChatOpenAI(model = "gpt-4" , temperature=0 , max_completion_tokens=10)
result = chatllm.invoke("What is the capital of India")
print(result)
#the result is not a simple plain text
print(result.content) # only to see the answer
