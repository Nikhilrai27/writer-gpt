from memory import vectorstore

results=vectorstore.similarity_search("who is the cricketer",k=1)
print(results[0].page_content)