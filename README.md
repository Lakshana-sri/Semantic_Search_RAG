
# 🧠 NEXUS AI
## Semantic Search Engine with Retrieval-Augmented Generation (RAG)

### 📌 Project Overview

NEXUS AI is an intelligent document search system that combines semantic search, hybrid retrieval, and Retrieval-Augmented Generation (RAG) to retrieve relevant information from documents and generate contextual answers.

The system allows users to ask natural language questions and obtain answers based on the content of PDF, DOCX, and HTML documents.

It uses Sentence Transformers for embedding generation, FAISS for vector similarity search, BM25 for keyword retrieval, and a locally running FLAN-T5 Small model for answer generation.

### 🎯 Objectives

- Develop an intelligent document search engine.
- Extract text from PDF, DOCX, and HTML files.
- Divide large documents into smaller chunks.
- Generate semantic embeddings for document content.
- Retrieve relevant information using semantic and keyword search.
- Generate context-based answers using a local language model.
- Display answers and source documents through an interactive web interface.

### ✨ Key Features

- Semantic Search
- Hybrid Search using FAISS and BM25
- Retrieval-Augmented Generation
- Local AI Model without API key
- PDF, DOCX, and HTML document support
- Source document identification
- Interactive Streamlit interface
- Similarity score display

### 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Streamlit | Interactive user interface |
| Sentence Transformers | Text embedding generation |
| FAISS | Vector similarity search |
| BM25 | Keyword-based retrieval |
| FLAN-T5 Small | Local answer generation |
| PyMuPDF | PDF text extraction |
| python-docx | DOCX processing |
| BeautifulSoup | HTML parsing |
| NumPy | Numerical operations |

### 🏗️ System Architecture

```text
          Document Collection
                   |
                   v
           Document Loading
                   |
                   v
            Text Extraction
                   |
                   v
             Text Chunking
                   |
                   v
          Embedding Generation
                   |
                   v
            FAISS Indexing
                   |
                   v
           Hybrid Retrieval
          /              \
   Semantic Search    BM25 Search
          \              /
           Relevant Context
                   |
                   v
          Local FLAN-T5 Model
                   |
                   v
          Generated Answer
                   |
                   v
       Streamlit User Interface
                   |
                   v
          Answer + Sources
```

### 📂 Project Structure

```text
Semantic_Search_RAG/
│
├── data/
│   └── documents/
│
├── indexes/
│   ├── documents.index
│   └── chunks.pkl
│
├── notebooks/
│
├── outputs/
│
├── src/
│   ├── document_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── search.py
│   ├── hybrid_search.py
│   └── rag.py
│
├── app.py
├── requirements.txt
└── README.md
```

### ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd Semantic_Search_RAG
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the environment on Windows**

```powershell
.venv\Scripts\activate
```

**5. Install the required packages**

```bash
pip install -r requirements.txt
```

### ▶️ How to Run

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

### 🔍 Working Process

1. Load documents from the document collection.
2. Extract textual content from supported file formats.
3. Divide extracted text into chunks.
4. Generate vector embeddings using Sentence Transformers.
5. Store embeddings in a FAISS index.
6. Process the user's natural language query.
7. Retrieve relevant content using hybrid search.
8. Pass retrieved context to the local FLAN-T5 model.
9. Generate a context-based answer.
10. Display the answer and source documents in Streamlit.

### 📊 Current Implementation

- Supported document formats: PDF, DOCX, HTML
- Chunk size: 500 words
- Chunk overlap: 50 words
- Embedding model: all-MiniLM-L6-v2
- Embedding dimensions: 384
- Vector index: FAISS
- Answer generation: FLAN-T5 Small

### 🚀 Future Enhancements

- Dynamic document uploads
- Improved answer generation
- Conversation history
- Document summarization
- User feedback and relevance evaluation
- Advanced ranking and explainability

### 👩‍💻 Developed By

**Lakshana Sri Varshini**

B.Sc. Computer Science (Artificial Intelligence)

