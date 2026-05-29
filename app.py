from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from prompts import (character_prompt,dialogue_prompt,
    plot_prompt
)

load_dotenv()


llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
character_chain = character_prompt | llm
dialogue_chain = dialogue_prompt | llm
plot_chain = plot_prompt | llm


while True:
    print("\n1. Character")
    print("2. Dialogue")
    print("3. Plot")
    print("Type exit to quit")

    task= input("\nChoose")
    
    user_input= input("Request > ")

    if task=='1':
        response=character_chain.invoke({
            "request":user_input}
            )
    elif task=='2':
        response=dialogue_chain.invoke(
            {
                "request":user_input
            }
        )
    elif task.lower() == "exit":
        break    
    elif task=='3':
        response=plot_chain.invoke(
            {
              "request":user_input  
            }
        )
    else:
        print("invalid choice")
        continue
    print("\nAI:")
    print(response.content)    
            

#response=llm.invoke(prompt)
#print(response.content)