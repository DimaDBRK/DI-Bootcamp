-- Week4 Day4
-- Dmitry Dubrov
-- Exercise 1 : Restaurant Menu Manager

-- Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns

-- item_id : SERIAL PRIMARY KEY
-- item_name : VARCHAR(30) NOT NULL
-- item_price : SMALLINT DEFAULT 0
-- CREATE TABLE Menu_Items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	item_name VARCHAR(30) NOT NULL,
-- 	item_price SMALLINT DEFAULT 0
-- )

SELECT * FROM Menu_Items

-- INSERT INTO Menu_Items (item_name, item_price)
-- VALUES ('Soap', 10)