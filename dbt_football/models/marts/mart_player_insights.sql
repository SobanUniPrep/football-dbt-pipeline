SELECT
    player_name,
    goals,
    appearances,
    minutes_per_goal,
    shot_conversion_pct,
    SNOWFLAKE.CORTEX.COMPLETE(
        'mistral-7b',
        'Analyze this Premier League player in one sentence based on stats: ' ||
        'Name: ' || player_name ||
        ', Goals: ' || goals ||
        ', Appearances: ' || appearances ||
        ', Minutes per goal: ' || ROUND(minutes_per_goal, 1) ||
        ', Shot conversion: ' || shot_conversion_pct || '%'
    ) AS ai_insight
FROM {{ ref('mart_top_scorers') }}