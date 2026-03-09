# Football Analytics Pipeline

End-to-end data pipeline pro analýzu Premier League dat.

## Architektura
```
API-Football → Python → Snowflake RAW → dbt Staging → dbt Marts
```

## Stack

- **Python** — extrakce dat z API-Football a načtení do Snowflake
- **Snowflake** — cloudový datový sklad
- **dbt** — transformace dat, testy, dokumentace

## Struktura projektu
```
football-dbt-pipeline/
├── ingestion/
│   ├── config.py       # konfigurace a konstanty
│   ├── extract.py      # volání API-Football
│   └── load.py         # načtení do Snowflake RAW
└── dbt_football/
    ├── models/
    │   ├── staging/    # views, parsování JSON, čištění
    │   └── marts/      # tabulky, business metriky
    └── tests/          # singular testy
```

## Data

**Zdroj:** API-Football (Premier League 2024/25)

**RAW vrstva:**
- `STANDINGS` — ligová tabulka
- `TOP_SCORERS` — statistiky střelců
- `FIXTURES` — výsledky zápasů

**Staging vrstva:**
- `stg_standings` — pořadí týmů s body
- `stg_top_scorers` — statistiky hráčů
- `stg_fixtures` — výsledky zápasů s vítězem

**Marts vrstva:**
- `mart_top_scorers` — střelci s minutami na gól a conversion rate
- `mart_team_performance` — výkonnost týmů, góly doma vs venku
- `mart_match_results` — výsledky zápasů s draw flag

## Spuštění

### Python pipeline
```bash
cd ingestion
pip install -r requirements.txt
python load.py
```

### dbt transformace
```bash
cd dbt_football
dbt run
dbt test
dbt docs serve
```