-- Test selže pokud existuje hráč se zápornými starty
SELECT *
FROM {{ ref('stg_top_scorers') }}
WHERE appearances < 0