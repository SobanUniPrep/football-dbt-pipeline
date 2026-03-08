WITH source AS (
    SELECT data
    FROM {{ source('raw', 'STANDINGS') }}
),

flattened AS (
    SELECT f.value AS team_data
    FROM source,
    LATERAL FLATTEN(input => data:league:standings[0]) f
)

SELECT
    team_data:rank::INTEGER         AS rank,
    team_data:team:name::STRING     AS team_name,
    team_data:points::INTEGER       AS points,
    team_data:all:played::INTEGER   AS played,
    team_data:all:win::INTEGER      AS wins,
    team_data:all:draw::INTEGER     AS draws,
    team_data:all:lose::INTEGER     AS losses,
    team_data:all:goals:for::INTEGER        AS goals_for,
    team_data:all:goals:against::INTEGER    AS goals_against,
    team_data:goalsDiff::INTEGER    AS goal_difference,
    team_data:description::STRING   AS european_competition
FROM flattened
ORDER BY rank