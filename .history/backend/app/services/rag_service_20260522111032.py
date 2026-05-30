import os

import chromadb

from sentence_transformers import SentenceTransformer


# Embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# ChromaDB client
client = chromadb.Client()

collection = client.get_or_create_collection(
    name="coding_knowledge"
)


def load_documents():

    folder_path = "app/data/coding_docs"

    documents = []

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as file:

            content = file.read()

            documents.append({
                "id": filename,
                "content": content
            })

    return documents


def store_documents():

    existing_docs = collection.count()

    if existing_docs > 0:
        return

    documents = load_documents()

    for doc in documents:

        embedding = embedding_model.encode(
            doc["content"]
        ).tolist()

        collection.add(
            ids=[doc["id"]],
            documents=[doc["content"]],
            embeddings=[embedding]
        )


def retrieve_relevant_context(query):

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    return results["documents"][0]