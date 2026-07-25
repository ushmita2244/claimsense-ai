from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
DATABASE_PATH = PROJECT_ROOT / "data" / "healthcare.db"

TABLES = [
    "patients",
    "conditions",
    "encounters",
    "medications",
    "observations",
    "procedures",
]


def main():
    conn = sqlite3.connect(DATABASE_PATH)

    try:
        for table in TABLES:
            csv_path = RAW_DATA_DIR / f"{table}.csv"

            print(f"Importing {table}...")

            df = pd.read_csv(csv_path)

            df.to_sql(
                name=table,
                con=conn,
                if_exists="replace",
                index=False,
            )

            print(f"✓ {table}: {len(df)} rows")

        print("\nDatabase created successfully!")
        print(DATABASE_PATH)

    finally:
        conn.close()


if __name__ == "__main__":
    main()