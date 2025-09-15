WITH mi AS (
    SELECT
        DISTINCT CART_ID
    FROM
        CART_PRODUCTS
    WHERE 1 = 1
        AND NAME = 'Milk'
), yo AS (
    SELECT
        CART_ID
    FROM
        CART_PRODUCTS
    WHERE 1 = 1
        AND NAME = 'Yogurt'
)

SELECT
    DISTINCT mi.CART_ID
FROM
    mi
INNER JOIN yo
ON 1 = 1
    AND mi.CART_ID = yo.CART_ID
ORDER BY
    mi.CART_ID ASC
;