1. Attribute/column filtering

SELECT title, author from publication
-> ONLY SELECT TITLE AND AUTHOR 

SELECT col_a, ..., col_z FROM table_name;


2. Renaming things

SELECT title, year - year % 10 AS decade FROM publication

3. Distinct records

SELECT genre FROM publication;

SELECT DISTINCT genre FROM publication

4. Sorting results

SELECT * FROM publication order by COPIES DESC;

You can also filter my multiple criteria

SELECT * FROM publication ORDER BY genre, ASC, year DESC;


5. Limiting number of records

SELECT * FROM publications ORDER BY year DESC LIMIT 3

6. Filtering records with condition

SELECT * FROM publication WHERE year >= 1950 AND YEAR < 1960;

SELECT * FROM publication WHERE year BETWEEN 1950 AND 1959

NOTE: = for equality, <> for INEQUALITY

7. Pattern matching on string columns

SELECT * FROM publication WHERE title LIKE 'The%' OR genre LIKE '%fiction%';

% matches zero or more characters

_ matches exactly one characters


8. Updating record

add one more copy of booth 1984

UPDATE publications
SET copies = copies + 1
WHERE title = '1984'

in general:
UPDATE table_name SET c1 = v1, c2 = v2 WHERE condition

9. Deleting record

DELETE FROM publication WHERE copies < 4

10. Aggregate functions

SUM(COL)
AVG(COL)
MIN(COL)
MAX(COL)
COUNT(COL)

ROUND(x, n) -> n decimal places, 0 for nearest integer


11. SUBSETS

SELECT department, SUM(COST)
FROM patient_visit
GROUP BY department;

In SQL, the query is logically processed in this order (not the order you write it):

FROM
→ SQL reads the patient_visit table

GROUP BY
→ Rows are grouped by department

SUM(cost)
→ The SUM function is applied within each group

SELECT
→ The final columns (department and the summed cost) are returned


You can also do multiple

GROUP BY doctor_id, visit_date

But note, you need to then SELECT doctor_id, visit_date

12. HAVING

SELECT doctor_id, SUM(cost) AS total
FROM patient_visit
GROUP BY doctor_id HAVING SUM(cost) >= 500



13. WHERE VS HAVING

SELECT doctor_id, SUM(cost) AS total
FROM patient_visit
WHERE visit_date >= '....'
GROUP BY department;

NOTE: WHERE FILTERS RECORDS (BEFORE PARTITIONING)

HAVING filters partitions