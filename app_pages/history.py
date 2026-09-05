import html

import streamlit as st

from ui.state import init_state, load_thread, start_new_chat

init_state()

st.markdown(
    '<div class="eyebrow">🕘 Conversation workspace</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="section-title">Chat History</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="section-copy">
        Reopen previous questions, continue an earlier analysis, or start a clean conversation.
        History is stored for the current Streamlit session.
    </div>
    """,
    unsafe_allow_html=True,
)

actions = st.columns([0.2, 0.8])
with actions[0]:
    if st.button("＋ New chat", type="primary", use_container_width=True):
        start_new_chat(archive=True)
        st.switch_page("app_pages/chat.py")

threads = st.session_state.chat_threads

if st.session_state.messages:
    st.info(
        "Your current conversation is active. Starting a new chat archives it here."
    )

if not threads:
    st.markdown(
        """
        <div class="history-card">
            <div class="card-title">No archived conversations yet</div>
            <div class="card-copy">
                Your previous chats will appear here after you start a new conversation.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

for index, thread in enumerate(threads):
    with st.container(border=True):
        cols = st.columns([0.68, 0.20, 0.12], vertical_alignment="center")

        with cols[0]:
            st.markdown(f"#### {html.escape(thread['title'])}")
            st.caption(thread["timestamp"])

        with cols[1]:
            if st.button(
                "Open",
                key=f"open_{thread['id']}",
                use_container_width=True,
            ):
                load_thread(thread)
                st.switch_page("app_pages/chat.py")

        with cols[2]:
            if st.button(
                "Delete",
                key=f"delete_{thread['id']}",
                use_container_width=True,
            ):
                del st.session_state.chat_threads[index]
                st.rerun()

        message_count = len(thread.get("messages", []))
        st.caption(f"{message_count} messages")
