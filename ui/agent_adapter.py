from typing import Any

from agent import agent


TOOL_LABELS = {
    "institutions_db_tool": ("🏛️", "Institutions DB"),
    "hospitals_db_tool": ("🏥", "Hospitals DB"),
    "restaurants_db_tool": ("🍽️", "Restaurants DB"),
    "web_search_tool": ("🌐", "Web Search"),
}


def _normalize_content(content: Any) -> str:
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []
        for part in content:
            if isinstance(part, dict) and "text" in part:
                text_parts.append(str(part["text"]))
            else:
                text_parts.append(str(part))
        return "\n".join(text_parts)

    return str(content)


def run_agent_with_trace(question: str) -> dict:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    messages = result.get("messages", [])
    final_message = messages[-1] if messages else None
    answer = _normalize_content(getattr(final_message, "content", final_message))

    tools = []
    query_details = []

    for message in messages:
        tool_calls = getattr(message, "tool_calls", None) or []

        for call in tool_calls:
            if isinstance(call, dict):
                name = call.get("name")
                args = call.get("args", {})
            else:
                name = getattr(call, "name", None)
                args = getattr(call, "args", {})

            if name in TOOL_LABELS and name not in tools:
                tools.append(name)

            if name in TOOL_LABELS:
                query_details.append(
                    {
                        "tool": name,
                        "args": args,
                    }
                )

        tool_name = getattr(message, "name", None)
        if tool_name in TOOL_LABELS and tool_name not in tools:
            tools.append(tool_name)

    return {
        "answer": answer,
        "tools": tools,
        "query_details": query_details,
    }


def tool_label(tool_name: str) -> str:
    icon, label = TOOL_LABELS.get(tool_name, ("🧩", tool_name))
    return f"{icon} {label}"
