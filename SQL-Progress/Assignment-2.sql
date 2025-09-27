-- ASSIGNMENT 2

-- 1. NOT IN Operator
-- Q1. Get details of employees who are not working as CHEF, MANAGER, or SECURITY.
SELECT *
FROM EMPS
WHERE JOB NOT IN ('CHEF','MANAGER','SECURITY');

-- Q2. Find customers whose names are not ROHIT SHARMA, VIRAT KOHLI, or HARDIK PANDYA.
SELECT *
FROM CUSTOMERS
WHERE NAME NOT IN ('ROHIT SHARMA','VIRAT KOHLI','HARDIK PANDYA');

-- Q3. Show restaurants that are not located in DELHI, CHENNAI, or KOLKATA.
SELECT RESTAURANT_ID, NAME
FROM RESTAURANTS
WHERE CITY NOT IN ('DELHI','CHENNAI','KOLKATA');


-- 2. BETWEEN Operator
-- Q1. Get employees whose salary is in the range 30000 to 60000.
SELECT *
FROM EMPS
WHERE SAL BETWEEN 30000+0.01 AND 60000-0.01;

-- Q2. Find employees hired in the year 2016 to 2019.
SELECT *
FROM EMPS
WHERE DOJ BETWEEN '2016-01-01' AND '2019-12-31';

-- Q3. Show employees born in the year 1990 to March of 1993.
SELECT *
FROM EMPS
WHERE DOB BETWEEN '1990-01-01' AND '1993-03-31';
