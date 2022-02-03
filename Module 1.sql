-- 1st questions

create database training;

use training;

-- 2nd question

CREATE TABLE demography (
    CustID INT AUTO_INCREMENT,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(1),
    PRIMARY KEY (CustID)
);

-- 3rd question

INSERT INTO demography(
	name,
    age,
    gender) 
values("John",25,"M");

-- 4th question

INSERT INTO demography(
	name,
    age,
    gender) 
values("Pavan",26,"M"),
	  ("Hema",31,"F");

-- 5th question

INSERT INTO demography(
	name,
    gender) 
values("Rekha","F");

-- 6th question

SELECT 
    *
FROM
    demography;

-- 7th question

UPDATE demography 
SET 
    age = NULL
WHERE
    name = 'John';

-- 8th question

SELECT 
    *
FROM
    demography
WHERE
    age IS NULL;

-- 9th question

DELETE FROM demography;

-- 10th question

drop table demography;