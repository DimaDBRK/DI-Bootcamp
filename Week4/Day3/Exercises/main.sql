-- Week4 Day3
-- Dmitry Dubrov
-- 🌟 Exercise 1: DVD Rental

-- Get a list of all film languages.
-- SELECT name FROM language

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
-- Get all films, even if they don’t have languages.
-- SELECT title, description, name
-- FROM film AS f
-- INNER JOIN language AS l
-- ON f.language_id = l.language_id

-- Get all languages, even if there are no films in those languages.
-- SELECT title, description, name
-- FROM film AS f
-- RIGHT JOIN language AS l
-- ON f.language_id = l.language_id

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- CREATE TABLE new_film (Hobbits
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100) NOT NULL
-- );

-- INSERT INTO new_film (title)
-- VALUES
-- ('select * from new_film'),
-- ('Titanics'),
-- ('Hobbits'),
-- ('Miss One'),

-- CREATE TABLE customer_review (
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER NOT NULL REFERENCES new_film(id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	language_id INTEGER NOT NULL REFERENCES language(language_id),
-- 	title VARCHAR(100) NOT NULL,
-- 	score INTEGER NOT NULL CHECK (score > 0 and score <= 10),
-- 	review TEXT,
-- 	last_update TIMESTAMPTZ DEFAULT NOW()
-- 	);

-- INSERT INTO customer_review (film_id, language_id, title, score, review)
-- VALUES
--  (1, 1, 'Review 1',3,'Good film with English'),
--  (3, 1, 'Review 2',10,'Very Very Good film with English')

-- SELECT * FROM customer_review
-- Make sure you link them to valid objects in the other tables.

-- SELECT nf.name, cr.title, score
-- FROM new_film AS nf
-- LEFT JOIN customer_review AS cr
-- ON nf.id = cr.film_id

-- SELECT review, name
-- FROM customer_review AS cr
-- LEFT JOIN language AS l
-- ON cr.language_id = l.language_id

-- 6. Delete a film that has a review from the new_film table, what happens 
-- to the customer_review table?

-- DELETE FROM new_film WHERE id = 1
-- RETURNING *
-- SELECT * FROM customer_review
-- Also Deleted

-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- SELECT * FROM language
-- 1	"English             "
-- 2	"Italian             "
-- 3	"Japanese            "
-- 4	"Mandarin            "
-- 5	"French              "
-- 6	"German              "

-- SELECT film_id,language_id FROM film 
-- ORDER BY title ASC
-- LIMIT 10

-- UPDATE film SET language_id = 3 WHERE (film_id >=2 AND film_id <= 10) 
-- SELECT film_id,language_id FROM film 
-- ORDER BY title ASC
-- LIMIT 15

-- 2. Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?
-- We had to pass this items.


-- 3. We created a new table called customer_review. Drop this table.
-- Is this an easy step, or does it need extra checking?

-- DROP TABLE customer_review

-- 4. Find out how many rentals are still outstanding 
-- (ie. have not been returned to the store yet).
-- 183 Pcs
-- SELECT COUNT(inventory_id) FROM rental 
-- WHERE return_date IS NULL

-- 5. Find the 30 most expensive movies which are outstanding (ie. have not been 
-- returned to the store yet)

-- SELECT f.film_id, f.title, f.rental_rate, return_date FROM inventory AS i
-- RIGHT JOIN rental AS r ON i.inventory_id = r.inventory_id
-- RIGHT JOIN film AS f ON i.film_id = f.film_id
-- WHERE return_date IS NULL
-- ORDER BY f.rental_rate DESC
-- LIMIT 30

-- 6. Your friend is at the store, and decides to rent a movie. He knows he wants to see
-- 4 movies, but he can’t remember their names. Can you help him find which movies he 
-- wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is
-- Penelope Monroe.

-- SELECT f.film_id, f.title, fa.actor_id, a.first_name, a.last_name, f.description FROM film AS f
-- LEFT JOIN film_actor AS fa ON f.film_id = fa.film_id
-- LEFT JOIN actor AS a ON fa.actor_id = a.actor_id
-- WHERE a.first_name ILIKE '%Penelope%' AND a.last_name ILIKE '%Monroe%' AND f.description ILIKE '%sumo%'

-- SELECT * FROM category

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- SELECT f.film_id, f.title, c.name, f.rating FROM film AS f
-- LEFT JOIN film_category AS fc ON f.film_id = fc.film_id
-- LEFT JOIN category AS c ON fc.category_id = c.category_id
-- WHERE f.length < 60  AND c.name ILIKE '%doc%' AND f.rating ='R'


-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 
-- for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
-- SELECT f.film_id, f.title, return_date::date, c.first_name, c.last_name,f.rental_rate    FROM inventory AS i
-- RIGHT JOIN rental AS r ON i.inventory_id = r.inventory_id
-- RIGHT JOIN film AS f ON i.film_id = f.film_id
-- RIGHT JOIN customer AS c ON r.customer_id = c.customer_id
-- WHERE return_date::date BETWEEN '2005-07-28' AND '2005-08-01' AND c.first_name ILIKE '%Matthew%'  AND c.last_name ILIKE '%Mahan%' AND f.rental_rate > 4


-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word
-- “boat” in the title or description, and it looked like it was a very expensive 
-- DVD to replace.

-- SELECT f.film_id, f.title, f.description, return_date::date, c.first_name, c.last_name, f.replacement_cost FROM inventory AS i
-- RIGHT JOIN rental AS r ON i.inventory_id = r.inventory_id
-- RIGHT JOIN film AS f ON i.film_id = f.film_id
-- RIGHT JOIN customer AS c ON r.customer_id = c.customer_id
-- WHERE rental_date IS NOT NULL AND c.first_name ILIKE '%Matthew%' AND c.last_name ILIKE '%Mahan%' AND (f.description  ILIKE '%boat%' OR f.title  ILIKE '%boat%')
-- ORDER BY replacement_cost DESC
-- LIMIT 1
