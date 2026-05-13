from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

chat_history = [
    SystemMessage(content="You are a well researched assistant")
]

while True:
    user_input = input("you: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        print("bye")
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Ai: ", result.content)

print(chat_history)