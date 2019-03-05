-- lists all tables of a database in MySQL server
SELECT TABLE_NAME FROM information_schema.tables WHERE table_schema='&1';
