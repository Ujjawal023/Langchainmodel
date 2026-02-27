from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="", dimensions=32)

documents = [
    "delhi is the capital of india"
    "paris is the capital of France"
    "kolkata is the capital of west bengal"

]

result = embedding.embed_documents(documents)

print(str(result))