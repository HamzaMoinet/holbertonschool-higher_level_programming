
-- Script to list all cities in California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
