-- ASSIGNMENT 3

-- 1. NOT BETWEEN Operator
-- Q1. Get employees whose salary is not in the range 25000 to 50000.
SELECT * 
FROM EMPS
WHERE SAL NOT BETWEEN 25000 AND 50000;

-- Q2. Find employees who were not hired in the year 2015 to 2018.
SELECT * 
FROM EMPS
WHERE DOJ NOT BETWEEN '2015-01-01' AND '2018-12-31';

-- Q3. Show employees not born between 1990 and 1992.
SELECT * 
FROM EMPS
WHERE DOB NOT BETWEEN '1990-01-01' AND '1992-12-31';

-- Q4. List customers whose CID is in the range 2 to 6.
SLECT * 
FROM CUSTOMERS
WHERE CID BETWEEN 2 AND 6;

-- Q5. Get employees whose joining year is not between 2017 and 2020.
SELECT *
FROM EMPS
WHERE DOJ NOT BETWEEN '2017-01-01' AND '2020-12-31';


-- 2. IS (NULL / NOT NULL) Operator
-- Q1. Find employees who do not have a reporting manager.
SELECT * 
FROM EMPS 
WHERE MGR IS NULL;

-- Q2. Show employees who are also customers.
SELECT * 
FROM EMPS
WHERE CID IS NOT NULL;

-- Q3. Get employees who are earning commission.
SELECT * 
FROM EMPS 
WHERE COMM IS NOT NULL;

-- Q4. List customers who have not placed an order.
SELECT * 
FROM CUSTOMERS
WHERE ORDER_ID IS NULL;
