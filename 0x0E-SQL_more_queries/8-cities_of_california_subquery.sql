-- lists all cities of California that can be found in the database
SELECT id,name FROM hbtn_0d_cities 
WHERE state_id=
(SELECT id FROM hbtn_0d_states WHERE name='California')
ORDER BY id ASC;
