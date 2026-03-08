import requests
import logging
from config import API_KEY, API_BASE_URL, PREMIER_LEAGUE_ID, CURRENT_SEASON

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_headers():
    return {
        "x-apisports-key": API_KEY
    }

def get_standings():
    logging.info("Stahuji standings z API")
    response = requests.get(
        f"{API_BASE_URL}/standings",
        headers=get_headers(),
        params={
            "league": PREMIER_LEAGUE_ID,
            "season": CURRENT_SEASON
        }
    )
    response.raise_for_status()
    data = response.json()
    logging.info(f"Standings staženy, počet záznamů: {len(data['response'])}")
    return data["response"]

def get_top_scorers():
    logging.info("Stahuji top scorers z API")
    response = requests.get(
        f"{API_BASE_URL}/players/topscorers",
        headers=get_headers(),
        params={
            "league": PREMIER_LEAGUE_ID,
            "season": CURRENT_SEASON
        }
    )
    response.raise_for_status()
    data = response.json()
    logging.info(f"Top scorers staženi, počet: {len(data['response'])}")
    return data["response"]

def get_fixtures():
    logging.info("Stahuji fixtures z API")
    response = requests.get(
        f"{API_BASE_URL}/fixtures",
        headers=get_headers(),
        params={
            "league": PREMIER_LEAGUE_ID,
            "season": CURRENT_SEASON,
            "status": "FT"
        }
    )
    response.raise_for_status()
    data = response.json()
    logging.info(f"Fixtures staženy, počet: {len(data['response'])}")
    return data["response"]

if __name__ == "__main__":
    standings = get_standings()
    scorers = get_top_scorers()
    fixtures = get_fixtures()
    logging.info("Extrakce dokončena")