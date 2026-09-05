import streamlit as st

st.markdown(
    '<div class="eyebrow">🗄️ Structured knowledge</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-title">Connected Data Sources</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="section-copy">
        The agent queries three local SQLite databases for exact structured answers.
        General or current information is routed to web search.
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.markdown("### 🏛️ Institutions")
        st.caption("institutions.db · table: institutions")
        st.markdown('<span class="status-chip">Connected</span>', unsafe_allow_html=True)
        st.markdown(
            """
            **Available fields**
            - Institution name
            - EIIN
            - Institution type
            - Division / district / thana
            - Address
            - Management type
            - Education level
            - Affiliation
            - MPO status
            """
        )
        st.caption("Source: Hugging Face")

with c2:
    with st.container(border=True):
        st.markdown("### 🏥 Hospitals")
        st.caption("hospitals.db · table: hospitals")
        st.markdown('<span class="status-chip">Connected</span>', unsafe_allow_html=True)
        st.markdown(
            """
            **Available fields**
            - Facility name
            - Agency
            - Type
            - Division / district
            - City corporation
            - Upazila
            - Paurasava / union
            - Private status
            """
        )
        st.warning(
            "Bed counts, doctor counts, treatment prices and detailed facilities are not in this dataset."
        )

with c3:
    with st.container(border=True):
        st.markdown("### 🍽️ Restaurants")
        st.caption("restaurants.db · table: restaurants")
        st.markdown('<span class="status-chip">Connected</span>', unsafe_allow_html=True)
        st.markdown(
            """
            **Available fields**
            - Restaurant name
            - Rating
            - Number of reviews
            - Address
            - Latitude / longitude
            - Affluence
            """
        )
        st.warning(
            "Cuisine, menu items, food prices and opening hours are not in this dataset."
        )

st.markdown("### 🌐 Web Search")
with st.container(border=True):
    cols = st.columns([0.68, 0.32])
    with cols[0]:
        st.markdown(
            """
            Used for **general knowledge, current information, policies, definitions,
            and information that is missing from the local structured datasets**.
            """
        )
    with cols[1]:
        st.metric("Search tool", "Tavily")
        st.caption("Selected automatically by the Mistral agent")
