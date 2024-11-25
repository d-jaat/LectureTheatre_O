from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_aws import BedrockEmbeddings
from langchain_ollama import OllamaEmbeddings

def get_embedding_function():
    # If you need to switch to BedrockEmbeddings, uncomment the line below:
    # embeddings = BedrockEmbeddings(credentials_profile_name="default", region_name="us-east-1")
    embeddings = OllamaEmbeddings(model="llama3.2-vision")
    return embeddings
