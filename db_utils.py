import re
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MAX_RETURNED_ROWS = 50


# Commands that the AI is never allowed to execute
FORBIDDEN_SQL_KEYWORDS = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "CREATE",
    "REPLACE",
    "ATTACH",
    "DETACH",
    "VACUUM",
    "PRAGMA"
]


def validate_sql(sql: str) -> tuple[bool, str]:
    """
    Validate that SQL is read-only.
    """

    if not sql:
        return False, "SQL query cannot be empty."

    sql = sql.strip()

    # Only SELECT or WITH statements
    if not re.match(
        r"^(SELECT|WITH)\b",
        sql,
        flags=re.IGNORECASE
    ):
        return (
            False,
            "Only SELECT queries are allowed."
        )

    upper_sql = sql.upper()

    for keyword in FORBIDDEN_SQL_KEYWORDS:

        if re.search(
            rf"\b{keyword}\b",
            upper_sql
        ):
            return (
                False,
                f"{keyword} statements are not allowed."
            )

    return True, ""


def execute_read_only_query(
    database_path: Path,
    sql: str
) -> str:
    """
    Execute a safe read-only SQLite query
    and convert the result into readable text.
    """

    valid, error_message = validate_sql(sql)

    if not valid:
        return f"SQL validation error: {error_message}"

    if not database_path.exists():

        return (
            f"Database not found: {database_path}. "
            "Run build_databases.py first."
        )

    connection = None

    try:

        connection = sqlite3.connect(
            database_path,
            timeout=10
        )

        connection.row_factory = sqlite3.Row

        # Extra database-level protection
        connection.execute(
            "PRAGMA query_only = ON"
        )

        cursor = connection.cursor()

        cursor.execute(sql)

        rows = cursor.fetchmany(
            MAX_RETURNED_ROWS + 1
        )

        if not rows:
            return "No matching records were found."

        truncated = (
            len(rows) > MAX_RETURNED_ROWS
        )

        rows = rows[:MAX_RETURNED_ROWS]

        output = []

        for index, row in enumerate(
            rows,
            start=1
        ):

            values = []

            for column_name in row.keys():

                value = row[column_name]

                if value is None:
                    value = "N/A"

                values.append(
                    f"{column_name}: {value}"
                )

            output.append(
                f"{index}. " + ", ".join(values)
            )

        result = "\n".join(output)

        if truncated:

            result += (
                "\n\nOnly the first "
                f"{MAX_RETURNED_ROWS} rows "
                "are shown."
            )

        return result

    except sqlite3.Error as error:

        return (
            "SQLite query error: "
            f"{str(error)}"
        )

    finally:

        if connection:
            connection.close()