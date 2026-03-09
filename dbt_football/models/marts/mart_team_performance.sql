WITH standings AS (
    SELECT * FROM {{ ref('stg_standings') }}
),

home_stats AS (
    SELECT
        home_team AS team_name,
        SUM(home_goals) AS goals_scored,
        SUM(away_goals) AS goals_conceded,
        COUNT(*) AS home_games
    FROM {{ ref('stg_fixtures') }}
    GROUP BY home_team
),

away_stats AS (
    SELECT
        away_team AS team_name,
        SUM(away_goals) AS goals_scored,
        SUM(home_goals) AS goals_conceded,
        COUNT(*) AS away_games
    FROM {{ ref('stg_fixtures') }}
    GROUP BY away_team
)

SELECT
    s.team_name,
    s.rank,
    s.points,
    s.wins,
    s.draws,
    s.losses,
    h.goals_scored AS home_goals_scored,
    a.goals_scored AS away_goals_scored
FROM standings s
LEFT JOIN home_stats h ON s.team_name = h.team_name
LEFT JOIN away_stats a ON s.team_name = a.team_name
ORDER BY s.rank