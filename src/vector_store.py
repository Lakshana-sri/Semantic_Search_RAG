
import faiss
import numpy as np
import pickle
import os


def create_vector_store(embeddings, chunks):

    embeddings = np.asarray(embeddings, dtype="float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    os.makedirs("indexes", exist_ok=True)

    faiss.write_index(index, "indexes/documents.index")

    with open("indexes/chunks.pkl", "wb") as file:
        pickle.dump(chunks, file)

    print("Vector index created successfully!")
    print("Total vectors:", index.ntotal)
    print("Vector dimensions:", dimension)

    return index


def load_vector_store():

    index = faiss.read_index("indexes/documents.index")

    with open("indexes/chunks.pkl", "rb") as file:
        chunks = pickle.load(file)

    return index, chunks