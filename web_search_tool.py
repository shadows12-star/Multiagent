import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_tavily import TavilySearch


# =========================================================
# LOAD ENVIRONMENT VARIABLES FIRST
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


# =========================================================
# CHECK TAVILY API KEY
# =========================================================

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError(
        "TAVILY_API_KEY was not found.\n"
        "Make sure your .env file is in the project root and contains:\n"
        "TAVILY_API_KEY=your_actual_tavily_api_key"
    )


# =========================================================
# TAVILY SEARCH
# =========================================================

tavily = TavilySearch(
    max_results=5,
    topic="general",
    include_answer=True,
    search_depth="basic",
    tavily_api_key=TAVILY_API_KEY
)


# =========================================================
# WEB SEARCH TOOL
# =========================================================

@tool("web_search_tool")
def web_search_tool(query: str) -> str:
    """
    Search the web for general knowledge, current information,
    policies, definitions, and information that is not available
    in the local Bangladesh databases.

    Examples:
    - What is the role of DGHS in Bangladesh?
    - What is Bangladesh's healthcare policy?
    - What does MPO mean?
    - How many beds does Dhaka Medical College Hospital have?
    """

    try:
        result = tavily.invoke(
            {
                "query": query
            }
        )

        if isinstance(result, dict):
            output = []

            answer = result.get("answer")

            if answer:
                output.append(
                    f"Search summary:\n{answer}"
                )

            search_results = result.get(
                "results",
                []
            )

            if search_results:
                output.append("\nSources:")

                for index, item in enumerate(
                    search_results[:5],
                    start=1
                ):
                    title = item.get(
                        "title",
                        "Untitled"
                    )

                    url = item.get(
                        "url",
                        ""
                    )

                    content = item.get(
                        "content",
                        ""
                    )

                    output.append(
                        f"\n{index}. {title}\n"
                        f"URL: {url}\n"
                        f"Content: {content}"
                    )

            if output:
                return "\n".join(output)

        return str(result)

    except Exception as error:
        return f"Web search failed: {str(error)}"