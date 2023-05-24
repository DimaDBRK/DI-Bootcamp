-- Week4 Day3
-- Dmitry Dubrov
-- Daily Challenge : Items & Orders

-- 1. Create a table called product_orders and a table called items. You decide which fields should be
-- in each table, although make sure the items table has a column called price.
-- 2. There should be a one to many relationship between the product_orders table and the items table.
-- An order can have many items, but an item can belong to only one order.
-- 4. Bonus :
-- Create a table called users.
-- There should be a one to many relationship between the users table and the product_orders table.


-- CREATE TABLE items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50), 		
-- 	price DECIMAL DEFAULT 0,
-- 	);

-- SELECT * FROM items

-- "item_id"	"name"	"price"
-- 1	"item_a"	100.1
-- 2	"item_b"	200.1
-- 3	"item_c"	300.1
-- 4	"item_cd"	400.1
-- 5	"item_as"	150.1
-- 6	"item_sf"	250.1
-- 7	"item_jk"	30.1
-- 8	"item_fgh"	10.1


-- CREATE TABLE users (
-- 	user_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50)		
-- 	);

-- INSERT INTO users(name)
-- VALUES
-- ('Jon'),
-- ('Mary'),
-- ('Vano'),
-- ('Omer'),
-- ('Hover')

-- SELECT * FROM users

-- "user_id"	"name"
-- 1	"Jon"
-- 2	"Mary"
-- 3	"Vano"
-- 4	"Omer"
-- 5	"Hover"


-- CREATE TABLE product_orders (
--  	id SERIAL PRIMARY KEY,
-- 	order_num INTEGER,
-- 	date DATE,
--  	item_id INTEGER,
-- 	user_id INTEGER,
-- 	FOREIGN KEY (item_id) REFERENCES items(item_id),
-- 	FOREIGN KEY (user_id) REFERENCES users(user_id) 
-- 	);

-- INSERT INTO product_orders(order_num, date, item_id, user_id)
-- VALUES
-- (1,'2022-01-10',1,5),
-- (1,'2022-01-10',2,5),
-- (2,'2022-02-15',3,5),
-- (2,'2022-02-15',4,5),
-- (2,'2022-02-15',5,5),
-- (3,'2022-03-16',6,2),
-- (3,'2022-03-16',7,2),
-- (4,'2022-04-22',8,1)
-- RETURNING *

-- "id"	"order_num"	"date"	"item_id"	"user_id"
-- 1	1	"2022-01-10"	1	5
-- 2	1	"2022-01-10"	2	5
-- 3	2	"2022-02-15"	3	5
-- 4	2	"2022-02-15"	4	5
-- 5	2	"2022-02-15"	5	5
-- 6	3	"2022-03-16"	6	2
-- 7	3	"2022-03-16"	7	2
-- 8	4	"2022-04-22"	8	1
-- 3. Create a function that returns the total price for a given order.
-- DROP FUNCTION GetOrderTotalPrice(INT)

-- CREATE FUNCTION GetOrderTotalPrice(orderId INT) 
-- 	RETURNS DECIMAL(10, 2)
-- 	LANGUAGE plpgsql
-- AS $$
-- DECLARE 
-- 	totalPrice DECIMAL(10, 2);
-- BEGIN
-- 	SELECT SUM(price) INTO totalPrice
--   	FROM product_orders AS po
-- 	INNER JOIN items AS i ON po.item_id = i.item_id
--   	WHERE order_num = orderId;
--   	RETURN totalPrice;
-- END;
-- $$;

-- SELECT GetOrderTotalPrice(1) AS total_price;

-- Create a function that returns the total price for a given order of a given user.

-- DROP FUNCTION UserOrderTotalPrice(INT, INT)

-- CREATE FUNCTION UserOrderTotalPrice(usern INT, ordern INT) 
-- 	RETURNS DECIMAL(10, 2)
-- 	LANGUAGE plpgsql
-- AS $$
-- DECLARE
-- totalprice DECIMAL(10, 2);
-- BEGIN
--   	SELECT SUM(i.price) INTO totalPrice
--  	FROM items AS i
--   	INNER JOIN product_orders AS po ON i.item_id = po.item_id
--   	WHERE po.user_id = usern AND po.order_num = ordern;

--   	RETURN totalPrice;
-- END;
-- $$;

-- SELECT UserOrderTotalPrice(5, 2) AS total_price;

