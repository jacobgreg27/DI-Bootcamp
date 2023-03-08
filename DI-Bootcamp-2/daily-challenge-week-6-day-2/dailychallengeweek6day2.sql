CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT * FROM SecondTab;

-- Table1 – FirstTab
-- ID  Name
-- 5   Pawan
-- 6   Sharlee
-- 7   Krish
-- NULL    Avtaar


-- Table2 – SecondTab
-- ID
-- 5
-- NULL

-- Q1. What will be the OUTPUT of the following statement?
--  answer : return a count of 2 since there are two rows 
--           in FirstTab with non-null IDs that are not present in SecondTab
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );


-- Q2. What will be the OUTPUT of the following statement?
-- answer : return a count of 1 since there is only one 
--          row in FirstTab with an ID that is not equal to 5

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );


-- Q3. What will be the OUTPUT of the following statement?
-- answer :  return a count of 1 since there is only one 
--           row in FirstTab with an ID that is not present in SecondTab
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );


-- Q4. What will be the OUTPUT of the following statement?
-- answer :return a count of 1 since there is only one row 
--         in FirstTab with a non-null ID that is also present in SecondTab

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )