SELECT
    DISTINCT FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
FROM
    REST_INFO AS ri
WHERE 1 = 1
    AND FAVORITES = (
        SELECT
            MAX(FAVORITES)
        FROM
            REST_INFO
        WHERE 1 = 1
            AND ri.FOOD_TYPE = FOOD_TYPE
        GROUP BY
            FOOD_TYPE
    )
ORDER BY
    FOOD_TYPE DESC
;