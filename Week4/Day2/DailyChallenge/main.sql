-- Week4 Day2
-- Dmitry Dubrov
-- Daily Challenge : SQL Puzzle

-- Instructions
-- In this puzzle you have to go through all the SQL queries and provide us the output of the requests before executing them (ie. make an assumption).
-- Then, execute them to make sure you were correct.

-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- 	(5,'Pawan'),
-- 	(6,'Sharlee'),
-- 	(7,'Krish'),
-- 	(NULL,'Avtaar')

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- 	(5),
-- 	(NULL)

-- SELECT * FROM SecondTab

-- Q1. What will be the OUTPUT of the following statement?
-- A: 3


-- SELECT COUNT(*) 
-- FROM FirstTab AS ft 
-- WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- A-OK: 0,  Null is not a value

-- Q2. What will be the OUTPUT of the following statement
-- A: 2
-- 	(6,'Sharlee'),
-- 	(7,'Krish'),
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- OK

-- Q3. What will be the OUTPUT of the following statement?
-- A: 3
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- A-OK: 0,  Null is not a value

-- Q4. What will be the OUTPUT of the following statement?
-- A: 2
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )