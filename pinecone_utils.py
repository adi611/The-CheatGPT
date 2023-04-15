import pinecone
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


load_dotenv()
model = SentenceTransformer('all-MiniLM-L6-v2')  # 384 dimensional

pinecone.init(api_key=os.getenv("PINECONE_KEY"),
              environment="northamerica-northeast1-gcp")
index = pinecone.Index("dbms-project")


def addData(corpusData):
    id = index.describe_index_stats()['total_vector_count']
    for i in range(len(corpusData)):
        chunk = corpusData[i]
        chunkInfo = (str(id+i),
                     model.encode(chunk).tolist(),
                     {'title': 'korth3', 'context': chunk})
        index.upsert(vectors=[chunkInfo])


def find_match(query, k):
    query_em = model.encode(query).tolist()
    result = index.query(query_em, top_k=k, includeMetadata=True)

    return [result['matches'][i]['metadata']['title'] for i in range(k)], [result['matches'][i]['metadata']['context'] for i in range(k)]
