import openai
import os
import json
import numpy as np

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_embeddings(docs, chunk = 1000):

    embeddings = []
    if len(docs) > chunk:
        for i in range(0, len(docs), chunk):
            response = get_embeddings(docs[i:i+chunk])
            embeddings.extend(response)          
    else:
        response = openai.Embedding.create(model='text-embedding-ada-002', input = docs) 
        embeddings = [doc['embedding'] for doc in response['data']]

    return embeddings

class EmbeddingLookup:

    def __init__(self, keys = None, embeddings = None):
        self.__keys = keys
        self.__embeddings = embeddings

    def save(self, path):
        combined = dict(zip(self.__keys, self.__embeddings))
        with open(path, 'w') as f:
            json.dump(combined, f)
    
    def load(self, path):
        with open(path, 'r') as f:
            combined = json.load(f)
        self.__keys = list(combined.keys())
        self.__embeddings = list(combined.values())

    def get_similar(self, query, top_n = 5):
        query_emb = get_embeddings([query])
        sims = np.dot(self.__embeddings, query_emb[0])
        top = np.argsort(sims)[-top_n:]
        return [self.__keys[i] for i in top]
