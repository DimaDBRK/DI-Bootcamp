-- Week4 Day3
-- Dmitry Dubrov
-- Daily Challenge: Tables Relationships
-- Part I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- CREATE TABLE Customer (
-- 	id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50),
-- 	last_name VARCHAR(50) NOT NULL
-- 	);


-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)
-- CREATE TABLE Customer_profile (
-- 	id SERIAL PRIMARY KEY,
-- 	isLoggedIn Boolean DEFAULT FALSE,
-- 	customer_id INTEGER,
-- 	FOREIGN KEY (customer_id) REFERENCES Customer(id)
-- 	);
	
-- 2. Insert those customers

-- John, Doe
-- Jerome, Lalu
-- Lea, Rive
-- INSERT INTO Customer (first_name, last_name)
-- VALUES 
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive')
-- ;

-- SELECT * FROM Customer
-- 3.Insert those customer profiles, use subqueries

-- John is loggedIn
-- Jerome is not logged in

-- INSERT INTO Customer_profile (isLoggedIn, customer_id)
-- VALUES 
-- (True, (SELECT id FROM Customer WHERE first_name = 'John')),
-- (False, (SELECT id FROM Customer WHERE first_name = 'Jerome'))
-- ;

-- SELECT * FROM Customer_profil	e

-- 4. Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers
-- SELECT first_name FROM Customer AS C
-- INNER JOIN Customer_profile AS CP ON C.id = CP.customer_id
-- WHERE isLoggedIn = true;

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
-- SELECT first_name, isLoggedIn
-- FROM Customer AS C
-- LEFT JOIN Customer_profile AS CP ON C.id = CP.customer_id;
-- The number of customers that are not LoggedIn
-- SELECT COUNT(*) AS notlogin FROM Customer AS C
-- LEFT JOIN Customer_profile AS CP ON C.id = CP.customer_id
-- WHERE isLoggedIn != true;

-- Part II:

-- 1. Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
-- CREATE TABLE Book (
--   book_id SERIAL PRIMARY KEY,
--   title VARCHAR(100) NOT NULL,
--   author VARCHAR(100) NOT NULL
-- );

-- 2. Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee

-- INSERT INTO Book (title, author)
-- VALUES 
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K. Rowling'),
-- ('To Kill a Mockingbird', 'Harper Lee');


-- 3. Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. 
-- Make sure that the age is never bigger than 15 (Find an SQL method);

-- CREATE TABLE Student (
--   student_id SERIAL PRIMARY KEY,
--   name VARCHAR(100) NOT NULL UNIQUE,
--   age INT CHECK (age <= 15)
-- );

-- 4. Insert those students
-- INSERT INTO Student (name, age)
-- VALUES 
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- 5. Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : 
-- A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

-- CREATE TABLE Library (
-- 	book_fk_id INTEGER,
-- 	student_fk_id INTEGER,
-- 	borrowed_date DATE,
-- 	PRIMARY KEY (book_fk_id, student_fk_id),
-- 	FOREIGN KEY (book_fk_id) REFERENCES Book (book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	FOREIGN KEY (student_fk_id) REFERENCES Student (student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );


-- 6. 
-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021

-- SET DateStyle TO European;

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES 
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'),'15/02/2022'),
-- ((SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'),'03/03/2021'),
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'),'23/05/2021'),
-- ((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '12/08/2021');
-- SET datestyle = default;

-- 7.Display the data
-- Select all the columns from the junction table
-- SET DateStyle TO European;

-- SELECT * FROM Library

-- Select the name of the student and the title of the borrowed books
-- SELECT name, title
-- FROM Library AS l
-- JOIN Student AS s ON l.student_fk_id = s.student_id
-- JOIN Book AS b ON l.book_fk_id = b.book_id;

-- Select the average age of the children, that borrowed the book Alice in Wonderland
-- SELECT ROUND(AVG(age)) AS average_age
-- FROM Student AS s
-- LEFT JOIN Library AS l ON student_id = student_fk_id
-- LEFT JOIN Book AS b ON l.book_fk_id = b.book_id
-- WHERE title = 'Alice In Wonderland';


-- Delete a student from the Student table, what happened in the junction table ?
-- DELETE FROM Student WHERE name = 'John';
-- corresponding records in the "Library" table will be auto deleted -> CASCADE



