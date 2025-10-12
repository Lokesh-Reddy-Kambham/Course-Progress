-- 1. Find employees whose first name contains at least two occurrences of the letter ‘A’.
SELECT * FROM EMPS WHERE FNAME LIKE "%A%A%";

-- 2. List customers whose names have a space followed by a word starting with ‘R’.  
SELECT * FROM EMPS WHERE FNAME LIKE "% %R";

-- 3. Find employees whose last name ends with either ‘RAJ’ or ‘NAIK’ using only LIKE.  
SELECT * FROM EMPS WHERE LNAME LIKE "%RAJ" OR LNAME LIKE "%NAIK";

-- 4. List menu items whose description contains the word ‘CURRY’
SELECT NAME FROM MENU_ITEMS WHERE DESCRIPTION LIKE "%CURRY%";

-- 5. Get employees whose job title has exactly 6 characters.  
SELECT * FROM EMPS WHERE JOB LIKE "______";

-- 6. Find customers whose email has a dot (.) before @gmail.com.  
SELECT * FROM CUSTOMERS WHERE EMAIL LIKE "%.%@GMAIL.COM";

-- 7. List employees whose first name starts and ends with the same letter. 
SELECT * 
FROM EMPS
WHERE 
FNAME LIKE 'A%A' OR FNAME LIKE 'B%B' OR FNAME LIKE 'C%C' OR
FNAME LIKE 'D%D' OR FNAME LIKE 'E%E' OR FNAME LIKE 'F%F' OR
FNAME LIKE 'G%G' OR FNAME LIKE 'H%H' OR FNAME LIKE 'I%I' OR
FNAME LIKE 'J%J' OR FNAME LIKE 'K%K' OR FNAME LIKE 'L%L' OR
FNAME LIKE 'M%M' OR FNAME LIKE 'N%N' OR FNAME LIKE 'O%O' OR
FNAME LIKE 'P%P' OR FNAME LIKE 'Q%Q' OR FNAME LIKE 'R%R' OR
FNAME LIKE 'S%S' OR FNAME LIKE 'T%T' OR FNAME LIKE 'U%U' OR
FNAME LIKE 'V%V' OR FNAME LIKE 'W%W' OR FNAME LIKE 'X%X' OR
FNAME LIKE 'Y%Y' OR FNAME LIKE 'Z%Z';

-- 8. Find menu items whose names contain at least one repeating letter (like “SS”, “EE”).  
SELECT *
FROM MENU
WHERE 
NAME LIKE '%AA%' OR NAME LIKE '%BB%' OR NAME LIKE '%CC%' OR
NAME LIKE '%DD%' OR NAME LIKE '%EE%' OR NAME LIKE '%FF%' OR
NAME LIKE '%GG%' OR NAME LIKE '%HH%' OR NAME LIKE '%II%' OR
NAME LIKE '%JJ%' OR NAME LIKE '%KK%' OR NAME LIKE '%LL%' OR
NAME LIKE '%MM%' OR NAME LIKE '%NN%' OR NAME LIKE '%OO%' OR
NAME LIKE '%PP%' OR NAME LIKE '%QQ%' OR NAME LIKE '%RR%' OR
NAME LIKE '%SS%' OR NAME LIKE '%TT%' OR NAME LIKE '%UU%' OR
NAME LIKE '%VV%' OR NAME LIKE '%WW%' OR NAME LIKE '%XX%' OR
NAME LIKE '%YY%' OR NAME LIKE '%ZZ%' ;

-- 9. List employees whose last name has exactly 4 characters 
SELECT * FROM EMPS WHERE LNAME LIKE "____";

-- 10. Find customers whose names have both ‘A’ and ‘I’ in them (any order).--  
SELECT NAME FROM CUSTOMERS WHERE NAME LIKE "%A%I%" OR NAME LIKE "%I%A%";
