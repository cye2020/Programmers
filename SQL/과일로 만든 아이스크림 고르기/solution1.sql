WITH fh AS (
    SELECT
        FLAVOR,
        TOTAL_ORDER
    FROM
        FIRST_HALF
    WHERE 1 = 1
        AND TOTAL_ORDER > 3000
), info AS (
    SELECT
        FLAVOR
    FROM
        ICECREAM_INFO
    WHERE 1 = 1
        AND INGREDIENT_TYPE = 'fruit_based'
)

SELECT
    fh.FLAVOR
FROM
    fh
INNER JOIN info
ON 1 = 1
    AND fh.FLAVOR = info.FLAVOR
ORDER BY
    fh.TOTAL_ORDER DESC
;