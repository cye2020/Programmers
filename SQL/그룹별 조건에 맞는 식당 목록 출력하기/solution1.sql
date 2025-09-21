WITH mr AS (
    SELECT
        MEMBER_ID,
        RANK() OVER(
            ORDER BY
                COUNT(*) DESC
        ) AS rnk
    FROM
        REST_REVIEW
    GROUP BY MEMBER_ID
)


SELECT
    mp.MEMBER_NAME,
    rr.REVIEW_TEXT,
    DATE_FORMAT(rr.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM
    REST_REVIEW rr
INNER JOIN mr
ON 1 = 1
    AND rr.MEMBER_ID = mr.MEMBER_ID
INNER JOIN MEMBER_PROFILE AS mp
ON 1 = 1
    AND mp.MEMBER_ID = rr.MEMBER_ID
WHERE 1 = 1
    AND mr.rnk = 1
ORDER BY
    REVIEW_DATE,
    rr.REVIEW_TEXT
;