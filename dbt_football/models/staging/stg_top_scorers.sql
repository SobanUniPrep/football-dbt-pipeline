WITH source AS (
    SELECT data
    FROM {{ source('raw', 'TOP_SCORERS') }}
)

SELECT
    data:player:id::INTEGER         AS player_id,
    data:player:name::STRING        AS player_name,
    data:player:nationality::STRING AS nationality,
    data:player:age::INTEGER        AS age,
    data:statistics[0]:team:name::STRING    AS team_name,
    data:statistics[0]:goals:total::INTEGER AS goals,
    data:statistics[0]:goals:assists::INTEGER AS assists,
    data:statistics[0]:games:appearences::INTEGER AS appearances,
    data:statistics[0]:shots:total::INTEGER AS shots_total,
    data:statistics[0]:shots:on::INTEGER    AS shots_on_target
FROM source