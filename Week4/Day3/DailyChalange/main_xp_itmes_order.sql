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

CREATE TABLE product_orders (
  	id SERIAL PRIMARY KEY,
	order_num INTEGER,
	date DATE,
  	item_id INTEGER,
	user_id INTEGER,
	FOREIGN KEY (item_id) REFERENCES items(item_id)
	FOREIGN KEY (user_id) REFERENCES users(user_id) 
	);

CREATE TABLE items (
	item_id SERIAL PRIMARY KEY,
	name VARCHAR(50), 		
	order_num INTEGER NOT NULL UNIQUE,
	price DECIMAL DEFAULT 0,
	FOREIGN KEY (order_num) REFERENCES product_orders(order_num) ON DELETE CASCADE ON UPDATE CASCADE
	);

CREATE TABLE users (
	user_id SERIAL PRIMARY KEY,
	name VARCHAR(50), 		
	FOREIGN KEY (user_id) REFERENCES product_orders(id) ON DELETE CASCADE ON UPDATE CASCADE
	);

-- 3. Create a function that returns the total price for a given order.
CREATE FUNCTION GetOrderTotalPrice(orderId INT) RETURNS DECIMAL(10, 2)
BEGIN
  DECLARE totalPrice DECIMAL(10, 2);

  SELECT SUM(price) INTO totalPrice
  FROM items
  WHERE order_num = orderId;

  RETURN totalPrice;
END;

SELECT UserOrderTotalPrice(1, 1) AS total_price;

-- Create a function that returns the total price for a given order of a given user.
CREATE FUNCTION UserOrderTotalPrice(user INT, order INT) RETURNS DECIMAL(10, 2)
BEGIN
	DECLARE totalprice DECIMAL(10, 2);

  	SELECT SUM(items.price) INTO totalPrice
 	FROM items AS i
  	INNER JOIN product_orders AS po ON i.order_num = po.order_num
  	WHERE po.user_id = userId AND i.order_id = orderId;

  	RETURN totalPrice;
END;

SELECT UserOrderTotalPrice(1, 1) AS total_price;

