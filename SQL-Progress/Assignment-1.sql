-- ASSIGNMENT 1

-- 1. AND Operator
-- Q1. Find employees who are AVAILABLE and earn more than 50000.
SELECT FNAME
FROM EMPS
WHERE SAL > 50000 AND STATUS = 'AVAILABLE';

-- Q2. Get employees who joined after 2015-01-01 and job is DELIVERY.
SELECT FNAME, LNAME
FROM EMPS
WHERE DOJ > '2015-01-01' AND JOB = 'DELIVERY';

-- Q3. List payments where method is Card and status is Completed.
SELECT *
FROM PAYMENTS
WHERE METHOD = 'Card' AND STATUS = 'Completed';

-- Q4. Show employees who are BUSY and have salary less than 50000.
SELECT FNAME
FROM EMPS
WHERE STATUS = 'BUSY' AND SAL < 50000;

-- Q5. Find employees with job WAITER and status not OFFLINE.
-- Option-1
SELECT FNAME FROM EMPS WHERE JOB = 'WAITER' AND STATUS IN ('AVAILABLE','BUSY');
-- Option-2
SELECT FNAME FROM EMPS WHERE JOB = 'WAITER' AND NOT STATUS = 'OFFLINE';
-- Option-3
SELECT FNAME FROM EMPS WHERE JOB = 'WAITER' AND STATUS != 'OFFLINE';


-- 2. OR Operator
-- Q1. List employees who are either MANAGER or CHEF.
-- Option-1
SELECT FNAME
FROM EMPS
WHERE JOB IN ('MANAGER','CHEF');

-- Option-2
SELECT FNAME
FROM EMPS
WHERE JOB = 'MANAGER' OR JOB = 'CHEF';

-- Q2. Show payments where status is Pending or method is COD.
SELECT *
FROM PAYMENTS
WHERE STATUS = 'Pending' OR METHOD = 'COD';

-- Q3. Get employees who joined before 2012-01-01 or earn above 90000.
SELECT *
FROM EMPS
WHERE DOJ < '2012-01-01' OR SAL > 90000;

-- Q4. Find employees whose job is DELIVERY or CASHIER.
-- Way-1
SELECT *
FROM EMPS
WHERE JOB = 'DELIVERY' OR JOB = 'CASHIER';

-- Way-2
SELECT *
FROM EMPS
WHERE JOB IN ('DELIVERY','CASHIER');

-- Q5. List payments where amount is less than 200 or greater than 300.
SELECT *
FROM PAYMENTS
WHERE AMOUNT < 200 OR AMOUNT > 300;


-- 3. IN Operator
-- Q1. Get employees who are working as WAITER, DELIVERY or CASHIER.
SELECT *
FROM EMPS
WHERE JOB IN ('WAITER','DELIVERY','CASHIER');

-- Q2. Find payments where method is either UPI or CARD.
SELECT *
FROM PAYMENTS
WHERE METHOD IN ('UPI','CARD');

-- Q3. Show employees whose status is either AVAILABLE or BUSY.
SELECT *
FROM EMPS
WHERE STATUS IN ('AVAILABLE','BUSY');

-- Q4. Get employees with salary 20000, 40000 or 100000.
SELECT *
FROM EMPS
WHERE SAL IN (20000,40000,100000);

-- Q5. List employees whose first name is PRIYA, MURALI or ARJUN.
SELECT *
FROM EMPS
WHERE FNAME IN ('PRIYA','MURALI','ARJUN');
