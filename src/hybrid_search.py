from rank_bm25 import BM25Okapi
from src.search import semantic_search
from src.vector_store import load_vector_store

def hybrid_search(query, top_k=5):
    index, chunks = load_vector_store()

    tokenized_docs = [
        chunk["text"].lower().split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_docs)

    query_tokens = query.lower().split()
    bm25_scores = bm25.get_scores(query_tokens)

    semantic_results = semantic_search(query, top_k=len(chunks))

    semantic_scores = {
        (r["filename"], r["chunk_id"]): r["score"]
        for r in semantic_results
    }

    results = []

    for i, chunk in enumerate(chunks):
        key = (chunk["filename"], chunk["chunk_id"])

        semantic_score = semantic_scores.get(key, 0)
        keyword_score = bm25_scores[i]

        combined_score = (
            0.6 * semantic_score +
            0.4 * (keyword_score / (max(bm25_scores) + 1e-9))
        )

        results.append({
            "filename": chunk["filename"],
            "chunk_id": chunk["chunk_id"],
            "text": chunk["text"],
            "score": float(combined_score)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]