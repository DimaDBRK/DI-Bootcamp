-- Week4 Day2
-- Dmitry Dubrov
-- Exercises XP

-- 🌟 Exercise 1 : Items And Customers
-- Instructions
-- We will work on the public database that we created yesterday.

-- Update data base
-- CREATE TABLE items (
-- 	item_id SERIAL PRIMARY KEY,
-- 	item_name VARCHAR (50) NOT NULL,
-- 	item_price INTEGER
-- );

-- CREATE TABLE customers
-- CREATE TABLE customers (
-- 	customer_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR (50) NOT NULL,
-- 	last_name VARCHAR (50) NOT NULL
-- );

-- INSERT INTO items(item_name, item_price)
-- VALUES
-- 	('Small Desk', 100),
-- 	('Large desk', 300),
-- 	('Fan', 80)
-- RETURNING * -- ->OK

-- INSERT INTO customers(first_name, last_name)
-- VALUES
-- 	('Greg', 'Jones'),
-- 	('Sandra', 'Jones'),
-- 	('Scott', 'Scott'),
-- 	('Trevor', 'Green'),
-- 	('Melanie', 'Johnson')
-- RETURNING * -- ->OK


-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- SELECT item_name, item_price AS price FROM items ORDER BY price ASC

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- SELECT item_name, item_price AS price FROM items 
-- WHERE item_price >= 80 
-- ORDER BY 2 DESC 

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the 
-- primary key column from the results.
-- SELECT first_name, last_name FROM customers 
-- ORDER BY first_name ASC
-- LIMIT 3

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
-- SELECT last_name FROM customers 
-- ORDER BY last_name DESC


-- 🌟 Exercise 2 : Dvdrental Database
--  + install a new sample database on our PostgreSQL servers

-- 1. In the dvdrental database write a query to select all the columns from the “customer” table.
-- All data
-- SELECT * FROM customer
-- Only columns name
-- SELECT *
--   FROM information_schema.columns
--  WHERE table_schema = 'dvdrental'
--    AND table_name   = 'customers'
--      ;

-- 2. Write a query to display the names (first_name, last_name) using an alias named “full_name”.
-- SELECT CONCAT(first_name, ' ', last_name) AS full_name  FROM customer

-- 3. Lets get all the dates that accounts were created. 
-- Write a query to select all the create_date from the “customer” table (there should be no duplicates).
-- SELECT DISTINCT create_date FROM customer

-- 4. Write a query to get all the customer details from the customer table, it should be displayed in 
-- descending order by their first name.
-- SELECT * FROM customer 
-- ORDER BY first_name DESC

-- 5. Write a query to get the film ID, title, description, year of release and rental rate in ascending 
-- order according to their rental rate.
-- SELECT film_ID, title, description, release_year, rental_rate FROM film
-- ORDER BY rental_rate ASC

-- 6. Write a query to get the address, and the phone number of all customers living in the Texas district, 
-- these details can be found in the “address” table.
-- SELECT address phone FROM address
-- WHERE district = 'Texas'

-- 7. Write a query to retrieve all movie details where the movie id is either 15 or 150.
-- SELECT * FROM film 
-- WHERE film_id IN (15,150)

-- -- 8. Write a query which should check if your favorite movie exists in the database. 
-- Have your query get the film ID, title, description, length and the rental rate, 
-- these details can be found in the “film” table.

-- SELECT film_id, title, description, length, rental_rate FROM film
-- WHERE title ILIKE '%love%'

-- 9. No luck finding your movie? Maybe you made a mistake spelling the name. 
-- Write a query to get the film ID, title, description, length and the rental rate of 
-- all the movies starting with the two first letters of your favorite movie.

-- SELECT film_id, title, description, length, rental_rate FROM film
-- WHERE title ILIKE 'lo%'

-- 10. Write a query which will find the 10 cheapest movies.
-- SELECT film_id, title, rental_rate FROM film
-- ORDER BY rental_rate ASC
-- LIMIT 10

-- 11. Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.
-- SELECT film_id, title, rental_rate
-- FROM film 
-- WHERE film_id NOT IN (SELECT film_id FROM film ORDER BY rental_rate ASC FETCH FIRST 10 ROWS ONLY)
-- ORDER BY  rental_rate ASC
-- FETCH FIRST 10 ROWS ONLY

-- 12. Write a query which will join the data in the customer table and the payment table. 
-- You want to get the first name and last name from the curstomer table, as well as the amount and the date 
-- of every payment made by a customer, ordered by their id (from 1 to…).

-- customer_id Added to table for tets reuslt
-- SELECT first_name, last_name, c.customer_id, amount, payment_date::date 
-- FROM customer AS c
-- LEFT JOIN payment AS p 
-- 	ON c.customer_id = p.customer_id
-- ORDER by c.customer_id

-- 13. You need to check your inventory. Write a query to get all the movies which are not in inventory.
-- SELECT film_id, title FROM film 
-- WHERE film_id NOT IN (SELECT DISTINCT film_id FROM inventory)

-- 14. Write a query to find which city is in which country.
-- SELECT DISTINCT city, country FROM city AS ct
-- LEFT JOIN country AS cn ON ct.country_id = cn.country_id 
-- ORDER BY city


-- 15. Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id,
-- names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them 
-- the dvd.

-- SELECT ct.customer_id, CONCAT(first_name, ' ', last_name), amount, payment_date::date AS name 
-- FROM customer AS ct
-- LEFT JOIN payment AS p ON ct.customer_id = p.customer_id
-- ORDER BY staff_id



