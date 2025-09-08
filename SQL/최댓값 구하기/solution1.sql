SELECT
    DATETIME
FROM
    ANIMAL_INS
WHERE 1 = 1
    AND DATETIME = (
        SELECT
            MAX(DATETIME)
        FROM
            ANIMAL_INS
    )
;