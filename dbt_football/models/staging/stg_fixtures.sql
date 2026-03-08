WITH source AS (
    SELECT data
    FROM {{ source('raw', 'FIXTURES') }}
)

SELECT
    data:fixture:id::INTEGER                    AS fixture_id,
    data:fixture:date::TIMESTAMP                AS match_date,
    data:fixture:venue:name::STRING             AS venue_name,
    data:fixture:venue:city::STRING             AS venue_city,
    data:fixture:referee::STRING                AS referee,
    data:league:round::STRING                   AS round,
    data:teams:home:name::STRING                AS home_team,
    data:teams:away:name::STRING                AS away_team,
    data:goals:home::INTEGER                    AS home_goals,
    data:goals:away::INTEGER                    AS away_goals,
    data:score:halftime:home::INTEGER           AS halftime_home,
    data:score:halftime:away::INTEGER           AS halftime_away,
    CASE 
        WHEN data:teams:home:winner::BOOLEAN = TRUE THEN data:teams:home:name::STRING
        WHEN data:teams:away:winner::BOOLEAN = TRUE THEN data:teams:away:name::STRING
        ELSE 'Draw'
    END                                         AS winner
FROM source