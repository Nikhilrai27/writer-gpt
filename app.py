from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from prompts import (character_prompt,dialogue_prompt,
    plot_prompt
)
from memory import vectorstore

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
            "request":user_input}
            )
        vectorstore.add_texts(
            [response.content]
            )
        

 #DIALOGUE       
    elif task=='2':
        response=dialogue_chain.invoke(
            {
                "request":user_input
            }
        )

#PLOT            
    elif task=='3':
        response=plot_chain.invoke(
            {
              "request":user_input  
            }
        )


# MEMORY SEARCH        
    elif task == "4":

        results = vectorstore.similarity_search(
            user_input,
            k=3
        )

        print("\nMEMORY RESULTS:\n")

        if results:
            print(results[0].page_content)
    
    else:
        print("invalid choice")
        continue
    print("\nAI:")
    print(response.content)    
            