CREATE PROCEDURE merge_students
AS
BEGIN

MERGE students AS target
USING (
    SELECT *
    FROM stg_students
    WHERE last_modified > (
        SELECT ISNULL(last_load_time,'1900-01-01')
        FROM metadata_table
        WHERE table_name = 'students'
    )
) AS source
ON target.student_id = source.student_id

WHEN MATCHED THEN
    UPDATE SET 
        target.name = source.name,
        target.last_modified = source.last_modified

WHEN NOT MATCHED THEN
    INSERT (student_id, name, last_modified)
    VALUES (source.student_id, source.name, source.last_modified);

-- Update watermark
UPDATE metadata_table
SET last_load_time = (
    SELECT MAX(last_modified) FROM students
)
WHERE table_name = 'students';

END;