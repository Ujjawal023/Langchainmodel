from langchain_groq import ChatGroq
from dotenv import load_dotenv  #(dotenv - load api key in current file from env file )

load_dotenv()

# main work start 

llm = ChatGroq(model="llama-3.1-8b-instant")

result = llm.invoke("What is the capital of India") #It is very important function in langchain and core components have invoke method 

print(result.content)
