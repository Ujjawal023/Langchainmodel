from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

#chat model 
model = ChatGroq(model="llama-3.1-8b-instant", temperature=1.5, max_tokens=10)

result = model.invoke("what is the capital of india")
print(result.content)