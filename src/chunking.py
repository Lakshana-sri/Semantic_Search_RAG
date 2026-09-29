
def chunk_text(text, chunk_size=500, overlap=50):

    words = text.split()
    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_documents(documents):

    all_chunks = []

    for document in documents:

        chunks = chunk_text(document["text"])

        for i, chunk in enumerate(chunks):

            all_chunks.append({
                "filename": document["filename"],
                "file_type": document["file_type"],
                "chunk_id": i + 1,
                "text": chunk
            })

    return all_chunks