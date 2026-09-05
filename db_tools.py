from pathlib import Path

from langchain.tools import tool

from db_utils import execute_read_only_query


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


INSTITUTIONS_DB = DATA_DIR / "institutions.db"
HOSPITALS_DB = DATA_DIR / "hospitals.db"
RESTAURANTS_DB = DATA_DIR / "restaurants.db"


# =========================================================
# INSTITUTIONS DATABASE TOOL
# =========================================================

@tool("institutions_db_tool")
def institutions_db_tool(sql: str) -> str:
    """
    Query the Bangladesh institutions SQLite database.

    Use this tool when the user's question requires
    information from the Institutional Information of
    Bangladesh dataset.

    Table name:
        institutions

    Available columns:

        name TEXT
        eiin INTEGER
        institute_type TEXT
        division_id INTEGER
        division TEXT
        district_id INTEGER
        district TEXT
        thana_id INTEGER
        thana TEXT
        union_id INTEGER
        union_name TEXT
        mauza_id INTEGER
        mauza_name TEXT
        area_status TEXT
        geographical_status TEXT
        address TEXT
        post TEXT
        management_type TEXT
        mobile TEXT
        student_type TEXT
        education_level TEXT
        affiliation TEXT
        mpo_status TEXT

    Appropriate questions include:

    - How many institutions are in Dhaka?
    - Show colleges in Chattogram.
    - Find institution with EIIN 123456.
    - How many MPO institutions are there?
    - Show government institutions in Rajshahi.
    - Count institutions by division.

    Input must be one valid SQLite SELECT query.

    Never use INSERT, UPDATE, DELETE, DROP,
    ALTER or CREATE.
    """

    return execute_read_only_query(
        INSTITUTIONS_DB,
        sql
    )


# =========================================================
# HOSPITALS DATABASE TOOL
# =========================================================

@tool("hospitals_db_tool")
def hospitals_db_tool(sql: str) -> str:
    """
    Query the Bangladesh hospitals SQLite database.

    Use this tool for questions that can be answered
    using the All Bangladeshi Hospitals dataset.

    Table name:
        hospitals

    Available columns:

        id INTEGER
        name TEXT
        name_bangla TEXT
        code INTEGER
        agency TEXT
        type TEXT
        division TEXT
        district TEXT
        city_corporation TEXT
        upazila TEXT
        paurasava TEXT
        union_name TEXT
        private INTEGER

    private:
        1 means marked as private
        0 means not marked as private

    Appropriate questions include:

    - How many health facilities are in Dhaka?
    - Show hospitals in Chattogram.
    - Find private facilities in Sylhet.
    - How many DGHS facilities are in Dhaka?
    - Show Medical College Hospitals.
    - Count health facilities by division.

    IMPORTANT:

    This database DOES NOT contain:

    - number of beds
    - number of doctors
    - detailed medical facilities
    - treatment costs
    - opening hours

    Input must be a valid SQLite SELECT query.
    """

    return execute_read_only_query(
        HOSPITALS_DB,
        sql
    )


# =========================================================
# RESTAURANTS DATABASE TOOL
# =========================================================

@tool("restaurants_db_tool")
def restaurants_db_tool(sql: str) -> str:
    """
    Query the Bangladesh restaurants SQLite database.

    Table name:
        restaurants

    Available columns:

        place_id TEXT
        name TEXT
        latitude REAL
        longitude REAL
        rating REAL
        number_of_reviews INTEGER
        affluence REAL
        address TEXT

    Appropriate questions include:

    - Find highly rated restaurants in Dhaka.
    - Show restaurants with rating above 4.5.
    - Which restaurants have the most reviews?
    - Find restaurants whose address contains Gulshan.
    - Show restaurant coordinates.

    IMPORTANT:

    This database DOES NOT contain:

    - cuisine
    - menu
    - individual food items
    - food prices
    - opening hours

    Input must be a valid SQLite SELECT query.
    """

    return execute_read_only_query(
        RESTAURANTS_DB,
        sql
    )