from dotenv import load_dotenv
import json
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from character_manager import save_character
from prompts import (character_prompt,dialogue_prompt,
    plot_prompt,memory_prompt
)
from memory import (vectorstore,retrieve_context,)

load_dotenv()

#LLM
llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    max_tokens=3000)

#chains
character_chain = character_prompt | llm
dialogue_chain = dialogue_prompt | llm
plot_chain = plot_prompt | llm
memory_chain= memory_prompt|llm


while True:
    print("\n1. Character")
    print("2. Dialogue")
    print("3. Plot")
    print("4. search memory")
    print("Type exit to quit")
    

    task= input("\nChoose")
    
    #user_input= input("Request > ")

    if task.lower()=="exit":
        print("Goodbye!!")
        break

    user_input= input("Request > ")

#CHARACTER
    if task=='1':
        response=character_chain.invoke({
            "request":user_input,}
            )
        
        memory = memory_chain.invoke(
        {   
            "character": response.content
            }
        )
        memory_data=json.loads(memory.content)
        save_character(memory_data)
        print(".........",memory_data)


        

        

 #DIALOGUE       
    elif task=='2':
        context=retrieve_context(
            user_input)
        response=dialogue_chain.invoke(
            {
                "request":user_input,
                "context":context
            }
        )

#PLOT            
    elif task=='3':
        context=retrieve_context(
            user_input)
        response=plot_chain.invoke(
            {
              "request":user_input,
              "context":context  
            }
        )


# MEMORY SEARCH        
    elif task == "4":

        results = vectorstore.similarity_search(
            user_input,
            k=1
        )

        print("\nMEMORY RESULTS:\n")

        if results:
            print(results[0].page_content)

        continue    
    
    else:
        print("invalid choice")
        continue
    print("\nAI:")
    print(response.content)    
            