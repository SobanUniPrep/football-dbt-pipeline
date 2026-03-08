import snowflake.connector
import json
import logging
from datetime import datetime
from config import (
    SNOWFLAKE_USER,
    SNOWFLAKE_PASSWORD,
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_WAREHOUSE,
    SNOWFLAKE_DATABASE
)
from extract import get_standings, get_top_scorers, get_fixtures

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_snowflake_connection():
    logging.info("Připojuji se ke Snowflake")
    return snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE
    )

def setup_schema(cursor):
    logging.info("Vytvářím schema a tabulky pokud neexistují")
    cursor.execute("CREATE SCHEMA IF NOT EXISTS RAW")
    cursor.execute("USE SCHEMA RAW")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS STANDINGS (
            loaded_at TIMESTAMP,
            data VARIANT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS TOP_SCORERS (
            loaded_at TIMESTAMP,
            data VARIANT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS FIXTURES (
            loaded_at TIMESTAMP,
            data VARIANT
        )
    """)

def load_data(cursor, table_name, records):
    logging.info(f"Nahrávám {len(records)} záznamů do {table_name}")
    loaded_at = datetime.now().isoformat()
    rows = [(loaded_at, json.dumps(record)) for record in records]
    for record in records:
        cursor.execute(
            f"INSERT INTO {table_name} (loaded_at, data) SELECT %s, PARSE_JSON(%s)",
            (loaded_at, json.dumps(record))
        )
    logging.info(f"{table_name} nahráno úspěšně")

if __name__ == "__main__":
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    try:
        setup_schema(cursor)

        standings = get_standings()
        load_data(cursor, "STANDINGS", standings)

        scorers = get_top_scorers()
        load_data(cursor, "TOP_SCORERS", scorers)

        fixtures = get_fixtures()
        load_data(cursor, "FIXTURES", fixtures)

        conn.commit()
        logging.info("Vše nahráno, pipeline dokončena")

    except Exception as e:
        logging.error(f"Chyba: {e}")
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
        logging.info("Spojení se Snowflake uzavřeno")