-- lists all tables of a database in MySQL server
USE '&1';
GO;
SELECT * FROM INFORMATION_SCHEMA.TABLES;
GO;
