import sqlite3
import pandas as pd

conn = sqlite3.connect("data/healthcare.db")


def show_tables():
    df = pd.read_sql("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name
    """, conn)
    print(df)


def describe(table):
    df = pd.read_sql(f"PRAGMA table_info({table})", conn)
    print(df)


def query(sql):
    df = pd.read_sql(sql, conn)
    print(df)


show_tables()

describe("patients")

query("SELECT * FROM patients LIMIT 5")

conn.close()