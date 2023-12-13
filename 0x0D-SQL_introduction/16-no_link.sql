-- list records that don't include NULL
SELECT score, name FROM second_table
WHERE name != ""
ORDER BY score DESC;
