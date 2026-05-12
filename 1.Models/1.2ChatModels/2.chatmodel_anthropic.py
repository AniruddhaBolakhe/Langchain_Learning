from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chatllm = ChatAnthropic(model = "claude-3-5-sonnet-20241022")
result = chatllm.invoke("What is the capital of India")
print(result)
#the result is not a simple plain text
print(result.content) # only to see the answer