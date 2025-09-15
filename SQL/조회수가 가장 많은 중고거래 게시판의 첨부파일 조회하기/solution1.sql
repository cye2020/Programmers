SELECT
    CONCAT('/home/grep/src/', file.BOARD_ID, '/', file.FILE_ID, file.FILE_NAME, file.FILE_EXT) AS FILE_PATH
FROM 
    USED_GOODS_FILE AS file,
    USED_GOODS_BOARD AS board
WHERE 1 = 1
    AND board.VIEWS = (
        SELECT
            MAX(VIEWS)
        FROM
            USED_GOODS_BOARD
    )
    AND file.BOARD_ID = board.BOARD_ID
ORDER BY
    file.FILE_ID DESC
;