import os


def create_metadata(documents):
    metadata = []

    for index, document in enumerate(documents, start=1):
        filename = document["filename"]
        extension = os.path.splitext(filename)[1].lower()

        metadata.append({
            "document_id": f"DOC{index:03d}",
            "filename": filename,
            "file_type": extension.replace(".", ""),
            "title": os.path.splitext(filename)[0],
            "author": "Unknown",
            "date": "Unknown",
            "category": "Artificial Intelligence",
            "tags": "AI, Machine Learning"
        })

    return metadata