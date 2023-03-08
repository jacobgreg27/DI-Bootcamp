CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL
);

INSERT INTO students (first_name, last_name, birth_date) VALUES ('Marc', 'Benichou', '1998-11-02');
INSERT INTO students (first_name, last_name, birth_date) VALUES ('Yoan', 'Cohen', '2010-12-03');
INSERT INTO students (first_name, last_name, birth_date) VALUES ('Lea', 'Benichou', '1987-07-27');
INSERT INTO students (first_name, last_name, birth_date) VALUES ('Amelia', 'Dux', '1996-04-07');
INSERT INTO students (first_name, last_name, birth_date) VALUES ('David', 'Grez', '2003-06-14');
INSERT INTO students (first_name, last_name, birth_date) VALUES ('Omer', 'Simpson', '1980-10-03');

SELECT * FROM students;

SELECT first_name, last_name FROM students;

SELECT first_name, last_name FROM students WHERE id = 2;

SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';

SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';

SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';

SELECT first_name, last_name FROM students WHERE first_name LIKE 'a%';

SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';

SELECT first_name, last_name FROM students WHERE first_name LIKE '_a%a';

SELECT first_name, last_name FROM students WHERE id IN (1, 3);

SELECT * FROM students WHERE birth_date >= '2000-01-01';