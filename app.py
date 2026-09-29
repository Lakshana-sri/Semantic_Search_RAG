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
    page_title="NEXUS AI | Intelligent Search",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# PROFESSIONAL LIGHT THEME
# ==================================================

st.markdown("""
<style>

/* Main Application */

.stApp {
    background: #F6F7FB;
    color: #25304A;
}

header[data-testid="stHeader"] {
    background: rgba(246, 247, 251, 0.95);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* Sidebar */

section[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid #E8EAF2;
}

section[data-testid="stSidebar"] h1 {
    color: #5145A8;
    font-size: 27px;
}

section[data-testid="stSidebar"] h3 {
    color: #344064;
}


/* Hero Section */

.hero {
    background: linear-gradient(
        120deg,
        #FFFFFF 0%,
        #F0EDFF 100%
    );
    padding: 38px;
    border-radius: 24px;
    border: 1px solid #E3DDFB;
    box-shadow: 0 8px 30px rgba(60, 48, 120, 0.06);
    margin-bottom: 28px;
}

.hero-tag {
    display: inline-block;
    background: #EAE5FF;
    color: #6254C7;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 16px;
}

.hero h1 {
    color: #26345B;
    font-size: 42px;
    font-weight: 750;
    line-height: 1.2;
    margin-bottom: 12px;
}

.hero p {
    color: #65708A;
    font-size: 16px;
    line-height: 1.8;
    max-width: 750px;
}


/* Dashboard Cards */

.metric-card {
    background: #FFFFFF;
    border: 1px solid #E8EAF2;
    padding: 24px 18px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 5px 18px rgba(35, 45, 75, 0.04);
    transition: 0.2s ease;
}

.metric-card:hover {
    border-color: #CFC5FA;
    box-shadow: 0 8px 24px rgba(75, 60, 145, 0.09);
}

.metric-number {
    color: #6254C7;
    font-size: 32px;
    font-weight: 750;
}

.metric-label {
    color: #758099;
    font-size: 13px;
    margin-top: 5px;
    font-weight: 500;
}


/* Section Headings */

h1, h2, h3 {
    color: #29365D;
    font-weight: 700;
}


/* Generated Answer */

.answer-card {
    background: #FFFFFF;
    border: 1px solid #E5E0FA;
    border-left: 5px solid #7565D8;
    border-radius: 16px;
    padding: 26px;
    line-height: 1.9;
    color: #34415E;
    font-size: 16px;
    overflow-wrap: anywhere;
    box-shadow: 0 5px 20px rgba(45, 45, 90, 0.04);
}


/* Retrieved Documents */

.document-content {
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    line-height: 1.85;
    font-size: 15px;
    color: #34415E;
    background: #F8F9FD;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E7E9F1;
}


/* Buttons */

div.stButton > button {
    background: #6254C7;
    color: #FFFFFF !important;
    border: 1px solid #6254C7;
    border-radius: 12px;
    min-height: 46px;
    font-weight: 600;
    transition: all 0.2s ease;
}

div.stButton > button p,
div.stButton > button span,
div.stButton > button div {
    color: #FFFFFF !important;
}

div.stButton > button:hover {
    background: #5042B2;
    border-color: #5042B2;
    color: #FFFFFF !important;
    box-shadow: 0 5px 14px rgba(98, 84, 199, 0.2);
}


/* Search Input */

.stTextInput input {
    background: #FFFFFF;
    color: #25304A;
    border: 1px solid #DDE1EC;
    border-radius: 13px;
    min-height: 48px;
}

.stTextInput input:focus {
    border-color: #7565D8;
    box-shadow: 0 0 0 1px #7565D8;
}


/* Expanders */

div[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid #E5E8F0;
    border-radius: 14px;
}

div[data-testid="stExpander"] summary {
    color: #344064;
    font-weight: 600;
}


/* Dividers */

hr {
    border-color: #E3E6EF;
}


/* General Text */

p, label {
    color: #34415E;
}

[data-testid="stCaptionContainer"] {
    color: #758099;
}


/* Footer */

.footer {
    text-align: center;
    color: #8991A5;
    font-size: 13px;
    line-height: 1.8;
    padding: 20px;
}

.footer strong {
    color: #6254C7;
    font-size: 17px;
    letter-spacing: 1px;
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

    st.caption("INTELLIGENT KNOWLEDGE ASSISTANT")

    st.divider()

    st.markdown("### Navigation")

    st.markdown("🔎  Semantic Search")
    st.markdown("📚  Knowledge Base")
    st.markdown("✨  AI Answer Generator")

    st.divider()

    st.markdown("### System Status")

    st.success("● Local AI Model Ready")
    st.info("● FAISS Vector Database Active")
    st.info("● Hybrid Retrieval Enabled")

    st.divider()

    st.markdown("### Technology Stack")

    st.caption("Sentence Transformers")
    st.caption("FAISS + BM25")
    st.caption("FLAN-T5 Small")
    st.caption("Streamlit")

    st.divider()

    st.caption("NEXUS AI | Version 1.0")


# ==================================================
# HERO SECTION
# ==================================================

st.html("""
<div class="hero">

    <div class="hero-tag">
        AI POWERED DOCUMENT INTELLIGENCE
    </div>

    <h1>Knowledge, at your fingertips.</h1>

    <p>
        Discover insights from your documents through intelligent
        semantic search, hybrid retrieval, and context-aware
        AI answer generation.
    </p>

</div>
""")


# ==================================================
# DASHBOARD METRICS
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.html(f"""
    <div class="metric-card">
        <div class="metric-number">{len(documents)}</div>
        <div class="metric-label">Documents Indexed</div>
    </div>
    """)

with col2:

    st.html(f"""
    <div class="metric-card">
        <div class="metric-number">{len(chunks)}</div>
        <div class="metric-label">Knowledge Chunks</div>
    </div>
    """)

with col3:

    st.html("""
    <div class="metric-card">
        <div class="metric-number">384</div>
        <div class="metric-label">Embedding Dimensions</div>
    </div>
    """)


st.write("")
st.write("")


# ==================================================
# SEARCH SECTION
# ==================================================

st.markdown("## 🔍 Intelligent Search")

st.caption(
    "Ask a question and retrieve meaningful answers from your knowledge base."
)


def set_query(example):
    st.session_state.search_input = example


if "search_input" not in st.session_state:
    st.session_state.search_input = ""


query = st.text_input(
    "Your question",
    placeholder="e.g. How does machine learning work?",
    key="search_input"
)


st.markdown("**Explore example questions**")

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


st.write("")

search_clicked = st.button(
    "✨  Generate AI Answer",
    type="primary",
    use_container_width=True
)


# ==================================================
# ANSWER GENERATION
# ==================================================

if search_clicked:

    if not query.strip():

        st.warning("Please enter a question to continue.")

    else:

        with st.spinner(
            "Analyzing your query and retrieving relevant information..."
        ):

            try:

                result = generate_answer(query)

                st.markdown("---")

                st.markdown("## ✨ AI Generated Answer")

                st.html(f"""
                <div class="answer-card">
                    {html.escape(result["answer"])}
                </div>
                """)

                st.caption(
                    "Response generated using retrieved information "
                    "from your knowledge base."
                )


                # ======================================
                # RETRIEVED SOURCES
                # ======================================

                st.markdown("## 📚 Retrieved Sources")

                st.caption(
                    "Explore the document passages used during retrieval."
                )

                for source_number, source in enumerate(
                    result["sources"], 1
                ):

                    filename = source["filename"]
                    chunk_id = source["chunk_id"]
                    score = source["score"]

                    with st.expander(
                        f"📄 {source_number}. {filename} | "
                        f"Chunk {chunk_id} | Score {score:.3f}"
                    ):

                        text = source["text"]

                        text = re.sub(
                            r'\s+',
                            ' ',
                            text
                        ).strip()

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

                        safe_text = html.escape(formatted_text)

                        st.html(f"""
                        <div class="document-content">
                            {safe_text}
                        </div>
                        """)

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

st.caption(
    "Documents currently available for intelligent retrieval."
)

with st.expander("Explore Indexed Documents"):

    if documents:

        for doc in documents:

            st.markdown(
                f"""
                📄 **{doc['filename']}**

                <span style="color:#758099">
                {doc['word_count']:,} words
                </span>
                """,
                unsafe_allow_html=True
            )

            st.divider()

    else:

        st.warning("No documents found in the knowledge base.")


# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.html("""
<div class="footer">

    <strong>NEXUS AI</strong><br>

    Semantic Search Engine with Retrieval-Augmented Generation<br>

    Search · Retrieve · Generate · Discover<br><br>

    Powered by Local AI

</div>
""")