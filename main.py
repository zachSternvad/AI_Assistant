from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

#@tool

def main():
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    tools = []
    agent_executor = create_react_agent(model, tools)
    
    print("Tjena! Jag är Lennart din AI Assistent!")
    print("Skriv 'Exit' för att avsluta.")
    
    while True:
        user_input = input("\n--Du: ").strip()
        
        if user_input == "Exit":
            break
        
        print("\033[33m\nAssistenten Lennart: \033[0m", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()
        
if __name__ == "__main__":
    main()