SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'items');

-- CREATE TABLE items (
--   id SERIAL PRIMARY KEY,
--   name VARCHAR(50) NOT NULL,
--   price INTEGER NOT NULL
-- );

-- CREATE TABLE customers (
--   id SERIAL PRIMARY KEY,
--   firstname VARCHAR(50) NOT NULL,
--   lastname VARCHAR(50) NOT NULL
-- );

INSERT INTO items (name, price) VALUES ('Small Desk', 100);
INSERT INTO items (name, price) VALUES ('Large Desk', 300);
INSERT INTO items (name, price) VALUES ('Fan', 80);

INSERT INTO customers (firstname, lastname) VALUES ('Greg', 'Jones');
INSERT INTO customers (firstname, lastname) VALUES ('Sandra', 'Jones');
INSERT INTO customers (firstname, lastname) VALUES ('Scott', 'Scott');
INSERT INTO customers (firstname, lastname) VALUES ('Trevor', 'Green');
INSERT INTO customers (firstname, lastname) VALUES ('Melanie', 'Johnson');

SELECT * FROM items;

SELECT * FROM items WHERE price > 80;

SELECT * FROM items WHERE price <= 300;

SELECT * FROM customers WHERE lastname = 'Smith';

SELECT * FROM customers WHERE lastname = 'Jones';

SELECT * FROM customers WHERE firstname != 'Scott';

SELECT * FROM items ORDER BY price ASC;

SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;

SELECT firstname, lastname FROM customers ORDER BY firstname ASC LIMIT 3;

SELECT lastname FROM customers ORDER BY lastname DESC;
