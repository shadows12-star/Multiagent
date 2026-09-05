from pathlib import Path

import pandas as pd
from datasets import load_dataset


# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)


# =========================================================
# HELPER FUNCTION
# =========================================================

def save_dataframe_to_sqlite(
    dataframe,
    database_path,
    table_name,
    dtype
):
    import sqlite3

    print(f"\nCreating {database_path.name}...")

    connection = sqlite3.connect(database_path)

    try:
        dataframe.to_sql(
            name=table_name,
            con=connection,
            if_exists="replace",
            index=False,
            dtype=dtype
        )

        connection.commit()

    finally:
        connection.close()

    print(f"Database created: {database_path}")
    print(f"Table: {table_name}")
    print(f"Rows: {len(dataframe):,}")
    print(f"Columns: {list(dataframe.columns)}")
# =========================================================
# INSTITUTIONS DATABASE
# =========================================================

def build_institutions_database():

    print("\n" + "=" * 60)
    print("DOWNLOADING INSTITUTIONS DATASET")
    print("=" * 60)

    dataset = load_dataset(
        "Mahadih534/Institutional-Information-of-Bangladesh",
        split="train"
    )

    df = dataset.to_pandas()

    # Rename original dataset columns to meaningful SQL names
    df = df.rename(
        columns={
            "INSTITUTE NAME": "name",
            "EIIN": "eiin",
            "INSTITUTE_TYPE": "institute_type",
            "DIVISION_ID": "division_id",
            "DIVISION": "division",
            "DISTRICT_ID": "district_id",
            "DISTRICT": "district",
            "THANA_ID": "thana_id",
            "THANA": "thana",
            "UNION_ID": "union_id",
            "UNION_NAME": "union_name",
            "MAUZA_ID": "mauza_id",
            "MAUZA_NAME": "mauza_name",
            "AREA_STATUS": "area_status",
            "GEOGRPYCAL_STATUS": "geographical_status",
            "ADDRESS": "address",
            "POST": "post",
            "MANAGEMENT_TYPE": "management_type",
            "MOBILE": "mobile",
            "STUDENT_TYPE": "student_type",
            "EDUCATION_LEVEL": "education_level",
            "AFFILIATION": "affiliation",
            "MPO_STATUS": "mpo_status",
        }
    )

    # Make numeric columns nullable integers
    integer_columns = [
        "eiin",
        "division_id",
        "district_id",
        "thana_id",
        "union_id",
        "mauza_id",
    ]

    for column in integer_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            ).astype("Int64")

    dtype = {
        "name": "TEXT",
        "eiin": "INTEGER",
        "institute_type": "TEXT",
        "division_id": "INTEGER",
        "division": "TEXT",
        "district_id": "INTEGER",
        "district": "TEXT",
        "thana_id": "INTEGER",
        "thana": "TEXT",
        "union_id": "INTEGER",
        "union_name": "TEXT",
        "mauza_id": "INTEGER",
        "mauza_name": "TEXT",
        "area_status": "TEXT",
        "geographical_status": "TEXT",
        "address": "TEXT",
        "post": "TEXT",
        "management_type": "TEXT",
        "mobile": "TEXT",
        "student_type": "TEXT",
        "education_level": "TEXT",
        "affiliation": "TEXT",
        "mpo_status": "TEXT",
    }

    save_dataframe_to_sqlite(
        dataframe=df,
        database_path=DATA_DIR / "institutions.db",
        table_name="institutions",
        dtype=dtype
    )


# =========================================================
# HOSPITALS DATABASE
# =========================================================

def build_hospitals_database():

    print("\n" + "=" * 60)
    print("DOWNLOADING HOSPITALS DATASET")
    print("=" * 60)

    dataset = load_dataset(
        "Mahadih534/all-bangladeshi-hospitals",
        split="train"
    )

    df = dataset.to_pandas()

    df = df.rename(
        columns={
            "Id": "id",
            "Name": "name",
            "Name (Bangla)": "name_bangla",
            "Code": "code",
            "Agency": "agency",
            "Type": "type",
            "Division": "division",
            "District": "district",
            "City Corporation": "city_corporation",
            "Upazila": "upazila",
            "Paurasava": "paurasava",
            "Union": "union_name",
            "Private": "private",
        }
    )

    integer_columns = [
        "id",
        "code",
        "private"
    ]

    for column in integer_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            ).astype("Int64")

    dtype = {
        "id": "INTEGER",
        "name": "TEXT",
        "name_bangla": "TEXT",
        "code": "INTEGER",
        "agency": "TEXT",
        "type": "TEXT",
        "division": "TEXT",
        "district": "TEXT",
        "city_corporation": "TEXT",
        "upazila": "TEXT",
        "paurasava": "TEXT",
        "union_name": "TEXT",
        "private": "INTEGER",
    }

    save_dataframe_to_sqlite(
        dataframe=df,
        database_path=DATA_DIR / "hospitals.db",
        table_name="hospitals",
        dtype=dtype
    )


# =========================================================
# RESTAURANTS DATABASE
# =========================================================

def build_restaurants_database():

    print("\n" + "=" * 60)
    print("DOWNLOADING RESTAURANT DATASET")
    print("=" * 60)

    dataset = load_dataset(
        "Mahadih534/Bangladeshi-Restaurant-Data",
        split="train"
    )

    df = dataset.to_pandas()

    # Numeric cleanup
    df["latitude"] = pd.to_numeric(
        df["latitude"],
        errors="coerce"
    )

    df["longitude"] = pd.to_numeric(
        df["longitude"],
        errors="coerce"
    )

    df["rating"] = pd.to_numeric(
        df["rating"],
        errors="coerce"
    )

    df["number_of_reviews"] = pd.to_numeric(
        df["number_of_reviews"],
        errors="coerce"
    ).round().astype("Int64")

    df["affluence"] = pd.to_numeric(
        df["affluence"],
        errors="coerce"
    )

    dtype = {
        "place_id": "TEXT",
        "name": "TEXT",
        "latitude": "REAL",
        "longitude": "REAL",
        "rating": "REAL",
        "number_of_reviews": "INTEGER",
        "affluence": "REAL",
        "address": "TEXT",
    }

    save_dataframe_to_sqlite(
        dataframe=df,
        database_path=DATA_DIR / "restaurants.db",
        table_name="restaurants",
        dtype=dtype
    )


# =========================================================
# MAIN
# =========================================================

def main():

    print("\n")
    print("=" * 60)
    print("BANGLADESH AI AGENT - DATABASE BUILDER")
    print("=" * 60)

    build_institutions_database()
    build_hospitals_database()
    build_restaurants_database()

    print("\n" + "=" * 60)
    print("ALL DATABASES CREATED SUCCESSFULLY")
    print("=" * 60)

    print("\nGenerated files:")

    print(
        "1.",
        DATA_DIR / "institutions.db"
    )

    print(
        "2.",
        DATA_DIR / "hospitals.db"
    )

    print(
        "3.",
        DATA_DIR / "restaurants.db"
    )


if __name__ == "__main__":
    main()