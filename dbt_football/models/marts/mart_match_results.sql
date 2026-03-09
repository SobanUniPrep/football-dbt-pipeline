SELECT
    fixture_id,
    home_team,
    away_team,
    home_goals,
    away_goals,
    match_date,
    WINNER,
    case
        when WINNER = 'Draw' then TRUE
        else FALSE
    end as was_draw
FROM {{ ref('stg_fixtures') }}
ORDER BY match_date