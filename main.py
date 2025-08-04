from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)
    
    tools = []
    agent_executor = create_react_agent(model, tools)
    
    print("Tjena! Jag är din AI Assistent. Skriv 'Exit' för att avsluta.")
    print("Du kan be mig utföra matte eller ställa frågor")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input == "Exit":
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {messages: [HumanMessage(content=user_input)]}
        )