SELECT
    player_id,
    player_name,
    goals,
    appearances,
    shots_on_target,
    appearances * 90 / goals AS minutes_per_goal,
    CASE 
        WHEN shots_on_target > 0 THEN ROUND(goals * 100.0 / shots_on_target, 1)
        ELSE NULL
    END AS shot_conversion_pct
FROM {{ ref('stg_top_scorers') }}
ORDER BY goals DESC