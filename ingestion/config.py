import os
from dotenv import load_dotenv

load_dotenv()

# API
API_KEY = os.getenv("API_KEY")
API_BASE_URL = "https://v3.football.api-sports.io"

# Snowflake
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SNOWFLAKE_SCHEMA = "RAW"

# Pipeline
PREMIER_LEAGUE_ID = 39
CURRENT_SEASON = 2024