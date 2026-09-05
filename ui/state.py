from copy import deepcopy
from datetime import datetime

import streamlit as st


def init_state():
    defaults = {
        "messages": [],
        "chat_threads": [],
        "current_chat_title": "New conversation",
        "prefill_prompt": "",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = deepcopy(value)


def make_title(messages):
    for message in messages:
        if message.get("role") == "user":
            text = message.get("content", "").strip()
            if text:
                return text[:42] + ("…" if len(text) > 42 else "")
    return "New conversation"


def archive_current_chat():
    messages = st.session_state.get("messages", [])

    if not messages:
        return

    title = make_title(messages)

    st.session_state.chat_threads.insert(
        0,
        {
            "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
            "title": title,
            "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            "messages": deepcopy(messages),
        },
    )


def start_new_chat(archive=True):
    if archive:
        archive_current_chat()

    st.session_state.messages = []
    st.session_state.current_chat_title = "New conversation"
    st.session_state.prefill_prompt = ""


def load_thread(thread):
    st.session_state.messages = deepcopy(thread["messages"])
    st.session_state.current_chat_title = thread["title"]
