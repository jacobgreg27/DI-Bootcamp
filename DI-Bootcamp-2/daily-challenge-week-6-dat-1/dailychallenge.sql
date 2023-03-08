CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','1970-08-10', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','1961-06-05', 2);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Meryl','Streep','1949-06-22', 3);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Cate','Blanchett','1969-05-14', 2);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES 
  ('Brad','Pitt','1963-12-18', 1),
  ('Leonardo','DiCaprio','1974-11-11', 1),
  ('Tom','Hanks','1956-07-09', 2);

SELECT COUNT(*) FROM actors;

