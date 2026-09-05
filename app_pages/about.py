import streamlit as st

st.markdown(
    '<div class="eyebrow">🧠 System architecture</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-title">How the Agent Works</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="section-copy">
        This is a tool-calling SQL agent: Mistral decides which data source is appropriate,
        generates read-only SQL for structured datasets, or uses web search for general/current information.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="flow-node">👤 User Question</div>', unsafe_allow_html=True)
st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
st.markdown('<div class="flow-node">✨ Mistral AI Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
st.markdown('<div class="flow-node">🧭 Tool Selection</div>', unsafe_allow_html=True)
st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)

cols = st.columns(4)
nodes = [
    ("🏛️", "Institutions DB", "Exact institutional records and statistics"),
    ("🏥", "Hospitals DB", "Exact health-facility records and counts"),
    ("🍽️", "Restaurants DB", "Ratings, reviews, locations and ranking"),
    ("🌐", "Web Search", "General, contextual and current information"),
]

for col, (icon, title, copy) in zip(cols, nodes):
    with col:
        st.markdown(
            f"""
            <div class="architecture-card">
                <div class="card-icon">{icon}</div>
                <div class="card-title">{title}</div>
                <div class="card-copy">{copy}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
st.markdown('<div class="flow-node">💬 Natural-Language Answer</div>', unsafe_allow_html=True)

st.markdown("### Why SQLite instead of a vector database?")
with st.container(border=True):
    st.markdown(
        """
        Your three Hugging Face datasets are **structured tabular data**. SQL is better for:

        - Exact counts
        - Filtering by district/division/type
        - Sorting by rating or reviews
        - Aggregations and statistics
        - Reproducible, deterministic queries

        A vector database would be useful later if you add **PDFs, policies, reports,
        circulars, long descriptions or other unstructured documents** for semantic RAG.
        """
    )

st.markdown("### Technology Stack")
tech = st.columns(6)
for col, label in zip(
    tech,
    ["Python", "Streamlit", "LangChain", "Mistral AI", "SQLite", "Tavily"],
):
    with col:
        st.markdown(
            f'<div class="pill" style="justify-content:center;width:100%;">{label}</div>',
            unsafe_allow_html=True,
        )
