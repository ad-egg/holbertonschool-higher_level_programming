-- lists all tables of a database in MySQL server
SELECT * FROM information_schema.tables WHERE IF EXISTS table_schema='&1';
