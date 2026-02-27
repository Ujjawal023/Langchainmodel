from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "delhi is the capital of india"
    "paris is the capital of France"
    "kolkata is the capital of west bengal"
]

vector = embedding.embed_documents(documents)
print(str(vector))