-- list a script that lists all records with a score >= 10 in the table.
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
