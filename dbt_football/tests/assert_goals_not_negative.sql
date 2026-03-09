-- Test selže pokud existuje hráč se zápornými góly
SELECT *
FROM {{ ref('stg_top_scorers') }}
WHERE goals < 0