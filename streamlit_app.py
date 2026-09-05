import streamlit as st

from ui.styles import inject_global_css
from ui.state import init_state

st.set_page_config(
    page_title="Bangladesh Multi-Tool AI Agent",
    page_icon="🇧🇩",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_state()
inject_global_css()

with st.sidebar:
    st.markdown(
        """
        <div class="brand-wrap">
            <div class="brand-mark">🇧🇩</div>
            <div>
                <div class="brand-title">Bangladesh AI Agent</div>
                <div class="brand-subtitle">Multi-Tool Intelligence Platform</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

pages = {
    "Workspace": [
        st.Page("app_pages/chat.py", title="New Chat", icon="💬", default=True),
        st.Page("app_pages/history.py", title="Chat History", icon="🕘"),
    ],
    "Project": [
        st.Page("app_pages/data_sources.py", title="Data Sources", icon="🗄️"),
        st.Page("app_pages/about.py", title="About Project", icon="🧠"),
    ],
}

pg = st.navigation(pages, position="sidebar", expanded=True)

with st.sidebar:
    st.markdown("---")
    st.markdown("#### Available tools")
    st.markdown(
        """
        <div class="tool-mini"><span>🏛️</span><div><b>Institutions DB</b><small>Connected</small></div></div>
        <div class="tool-mini"><span>🏥</span><div><b>Hospitals DB</b><small>Connected</small></div></div>
        <div class="tool-mini"><span>🍽️</span><div><b>Restaurants DB</b><small>Connected</small></div></div>
        <div class="tool-mini"><span>🌐</span><div><b>Web Search</b><small>Connected</small></div></div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="sidebar-footer">
            <span class="online-dot"></span>
            <div>
                <b>System Online</b><br/>
                <small>Powered by Mistral AI</small>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

pg.run()
