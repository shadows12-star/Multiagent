import html

import streamlit as st

from ui.agent_adapter import run_agent_with_trace, tool_label
from ui.state import init_state, start_new_chat

init_state()

left, right = st.columns([0.72, 0.28], vertical_alignment="top")

with left:
    st.markdown(
        '<div class="eyebrow">🇧🇩 Bangladesh intelligence workspace</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-title">What would you like to know about Bangladesh?</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="hero-copy">
            Ask questions using institutional, healthcare and restaurant datasets,
            or let the agent search the web for general and current information.
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="badge-row">
            <span class="pill">✨ Mistral AI</span>
            <span class="pill">🧰 4 Tools Active</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

if st.session_state.messages:
    top_cols = st.columns([0.82, 0.18])
    with top_cols[1]:
        if st.button("＋ New chat", use_container_width=True):
            start_new_chat(archive=True)
            st.rerun()

if not st.session_state.messages:
    suggestions = [
        ("🏥", "Hospitals", "How many health facilities are in Dhaka district?"),
        ("🎓", "Institutions", "How many educational institutions are in Chattogram?"),
        ("🍽️", "Restaurants", "Show me 5 highly rated restaurants with addresses containing Dhaka."),
        ("🌐", "General Knowledge", "What is the role of DGHS in Bangladesh?"),
    ]

    cols = st.columns(4)

    for col, (icon, title, question) in zip(cols, suggestions):
        with col:
            st.markdown(
                f"""
                <div class="suggestion-card">
                    <div class="card-icon">{icon}</div>
                    <div class="card-title">{html.escape(title)}</div>
                    <div class="card-copy">{html.escape(question)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Ask this", key=f"suggest_{title}", use_container_width=True):
                st.session_state.prefill_prompt = question
                st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

for message in st.session_state.messages:
    role = message["role"]
    avatar = "🧑" if role == "user" else "🇧🇩"

    with st.chat_message(role, avatar=avatar):
        if role == "assistant":
            for tool in message.get("tools", []):
                st.markdown(
                    f'<span class="tool-badge">{html.escape(tool_label(tool))}</span>',
                    unsafe_allow_html=True,
                )

        st.markdown(message["content"])

        details = message.get("query_details", [])
        if role == "assistant" and details:
            with st.expander("View query details"):
                for item in details:
                    st.markdown(f"**Tool:** {tool_label(item['tool'])}")
                    args = item.get("args", {})
                    sql = args.get("sql") if isinstance(args, dict) else None
                    query = args.get("query") if isinstance(args, dict) else None

                    if sql:
                        st.code(sql, language="sql")
                    elif query:
                        st.code(query, language="text")
                    else:
                        st.json(args)

pending_prompt = st.session_state.pop("prefill_prompt", "") or None
prompt = st.chat_input(
    "Ask something about Bangladesh...",
    key="main_chat_input",
)

if pending_prompt and not prompt:
    prompt = pending_prompt

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🇧🇩"):
        try:
            with st.status(
                "Selecting the best data source...",
                expanded=False,
            ) as status:
                result = run_agent_with_trace(prompt)
                status.update(
                    label="Answer ready",
                    state="complete",
                    expanded=False,
                )

            for tool in result["tools"]:
                st.markdown(
                    f'<span class="tool-badge">{html.escape(tool_label(tool))}</span>',
                    unsafe_allow_html=True,
                )

            st.markdown(result["answer"])

            if result["query_details"]:
                with st.expander("View query details"):
                    for item in result["query_details"]:
                        st.markdown(f"**Tool:** {tool_label(item['tool'])}")
                        args = item.get("args", {})
                        sql = args.get("sql") if isinstance(args, dict) else None
                        query = args.get("query") if isinstance(args, dict) else None

                        if sql:
                            st.code(sql, language="sql")
                        elif query:
                            st.code(query, language="text")
                        else:
                            st.json(args)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result["answer"],
                    "tools": result["tools"],
                    "query_details": result["query_details"],
                }
            )

        except Exception as exc:
            error_message = (
                "I couldn't complete that request. "
                "Please verify that the Mistral and Tavily API keys are configured "
                f"and that the local databases exist.\n\nTechnical message: `{exc}`"
            )
            st.error(error_message)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message,
                    "tools": [],
                    "query_details": [],
                }
            )

st.markdown(
    '<div class="chat-note">The agent automatically chooses the best tool for your question.</div>',
    unsafe_allow_html=True,
)
