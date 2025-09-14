WITH a AS (
    SELECT
        APNT_NO,
        PT_NO,
        MDDR_ID,
        MCDP_CD,
        APNT_YMD
    FROM
        APPOINTMENT
    WHERE 1 = 1
        AND DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
        AND APNT_CNCL_YN = 'N'
        AND MCDP_CD = 'CS'
)

SELECT
    a.APNT_NO,
    p.PT_NAME,
    a.PT_NO,
    a.MCDP_CD,
    d.DR_NAME,
    a.APNT_YMD
FROM
    a
LEFT JOIN PATIENT AS p
ON 1 = 1
    AND p.PT_NO = a.PT_NO
LEFT JOIN DOCTOR AS d
ON 1 = 1
    AND d.DR_ID = a.MDDR_ID
ORDER BY a.APNT_YMD
;