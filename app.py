
import streamlit as st
import re
import html

from src.rag import generate_answer
from src.document_loader import load_all_documents
from src.chunking import chunk_documents


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="NEXUS AI | Semantic Search",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0d1020, #17182c);
    color: #f5f5ff;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}

.hero {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(120deg, #30265c, #222d54);
    border: 1px solid #514477;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 8px;
}

.hero p {
    color: #d0c9ed;
    font-size: 16px;
    line-height: 1.7;
}

.metric-card {
    background: #20243b;
    border: 1px solid #393c59;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
}

.metric-number {
    color: #bba7ff;
    font-size: 30px;
    font-weight: 700;
}

.metric-label {
    color: #b8bad0;
    font-size: 13px;
}

.answer-card {
    background: #20243b;
    border: 1px solid #514477;
    border-left: 5px solid #9b7aff;
    border-radius: 15px;
    padding: 23px;
    line-height: 1.9;
    color: #f5f3ff;
    font-size: 16px;
    overflow-wrap: anywhere;
}

.document-content {
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    word-break: normal;
    line-height: 1.9;
    font-size: 15px;
    color: #e2e2f0;
    background: #171a2e;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #393c59;
}

div.stButton > button {
    border-radius: 12px;
    border: 1px solid #8065d9;
    background: linear-gradient(90deg, #7355d9, #5943b4);
    color: white;
    font-weight: 600;
    min-height: 45px;
    transition: 0.2s;
}

div.stButton > button:hover {
    border-color: #c0aaff;
    color: white;
    background: #8065d9;
}

div[data-testid="stExpander"] {
    background: #20243b;
    border: 1px solid #393c59;
    border-radius: 12px;
}

section[data-testid="stSidebar"] {
    background: #15182b;
    border-right: 1px solid #343751;
}

.stTextInput input {
    background: #20243b;
    color: white;
    border-radius: 12px;
    border: 1px solid #514477;
}

h2, h3 {
    color: #e9e4ff;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# LOAD DOCUMENTS
# ==================================================

documents = load_all_documents("data/documents")
chunks = chunk_documents(documents)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("# 🧠 NEXUS AI")

    st.caption("Your Intelligent Knowledge Assistant")

    st.divider()

    st.markdown("### Navigation")

    st.markdown("🔎 Semantic Search")
    st.markdown("📚 Knowledge Base")
    st.markdown("✨ AI Answer Generator")

    st.divider()

    st.markdown("### System Status")

    st.success("Local AI Model Ready")
    st.info("FAISS Vector Database Active")
    st.info("Hybrid Retrieval Enabled")

    st.divider()

    st.markdown("### Technologies")

    st.caption("Sentence Transformers")
    st.caption("FAISS + BM25")
    st.caption("FLAN-T5 Small")
    st.caption("Streamlit")


# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<div class="hero">
    <h1>Ask your knowledge base.</h1>
    <p>
        Discover information from your documents using semantic search,
        hybrid retrieval and local AI answer generation.
    </p>
</div>
""", unsafe_allow_html=True)


# ==================================================
# DASHBOARD METRICS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{len(documents)}</div>
        <div class="metric-label">Documents Indexed</div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-number">{len(chunks)}</div>
        <div class="metric-label">Text Chunks</div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">384</div>
        <div class="metric-label">Embedding Dimensions</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")


# ==================================================
# SEARCH SECTION
# ==================================================

st.markdown("## 🔍 Intelligent Search")


# Callback for sample questions
def set_query(example):
    st.session_state.search_input = example


if "search_input" not in st.session_state:
    st.session_state.search_input = ""


query = st.text_input(
    "Ask anything",
    placeholder="e.g. How does machine learning work?",
    key="search_input"
)


st.markdown("**Try these questions:**")

examples = [
    "What is Artificial Intelligence?",
    "How does machine learning work?",
    "What is cybersecurity?",
    "How is IoT used in healthcare?"
]

cols = st.columns(4)

for i, example in enumerate(examples):

    with cols[i]:

        st.button(
            example,
            key=f"example_{i}",
            on_click=set_query,
            args=(example,),
            use_container_width=True
        )


search_clicked = st.button(
    "✨ Generate AI Answer",
    type="primary",
    use_container_width=True
)


#
# ==================================================
# ANSWER GENERATION
# ==================================================

if search_clicked:

    if not query.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner(
            "Searching documents and generating AI answer..."
        ):

            try:

                result = generate_answer(query)

                st.markdown("---")

                st.markdown("## ✨ AI Generated Answer")

                st.markdown(
                    f"""
                    <div class="answer-card">
                        {html.escape(result["answer"])}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.caption(
                    "Generated using retrieved knowledge from your documents."
                )

                # ======================================
                # RETRIEVED SOURCES
                # ======================================

                st.markdown("## 📚 Retrieved Sources")

                for source_number, source in enumerate(
                    result["sources"], 1
                ):

                    filename = source["filename"]
                    chunk_id = source["chunk_id"]
                    score = source["score"]

                    with st.expander(
                        f"📄 {source_number}. {filename} | "
                        f"Chunk {chunk_id} | "
                        f"Score {score:.3f}"
                    ):

                        # Get original retrieved text
                        text = source["text"]

                        # Remove excessive spaces and line breaks
                        text = re.sub(r'\s+', ' ', text).strip()

                        # Divide text into readable paragraphs
                        sentences = re.split(
                            r'(?<=[.!?])\s+',
                            text
                        )

                        paragraphs = []

                        for sentence_index in range(
                            0, len(sentences), 4
                        ):

                            paragraph = " ".join(
                                sentences[
                                    sentence_index:sentence_index + 4
                                ]
                            )

                            paragraphs.append(paragraph)

                        formatted_text = "\n\n".join(paragraphs)

                        # Safely display formatted text
                        safe_text = html.escape(formatted_text)

                        st.markdown(
                            f"""
                            <div class="document-content">
                                {safe_text}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        st.write("")

                        st.progress(
                            min(max(score, 0.0), 1.0),
                            text=(
                                f"Hybrid Relevance Score: "
                                f"{score:.3f}"
                            )
                        )

            except Exception as e:

                st.error(f"Error generating answer: {e}")
# ==================================================
# KNOWLEDGE BASE
# ==================================================

st.markdown("---")

st.markdown("## 📂 Knowledge Base")

with st.expander("View all indexed documents"):

    if documents:

        for doc in documents:

            st.markdown(
                f"""
                📄 **{doc['filename']}**

                <span style="color:#aaaacc">
                {doc['word_count']:,} words
                </span>
                """,
                unsafe_allow_html=True
            )

            st.divider()

    else:

        st.warning("No documents found.")


# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    "<div style='text-align:center;color:#9999b5;'>"
    "NEXUS AI | Semantic Search Engine with RAG<br>"
    "Powered by Local AI"
    "</div>",
    unsafe_allow_html=True
)