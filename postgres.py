'''
instalacja postgres na windowsie
SQL Shell

\l >> list all databases

CREATE DATABASE name;
\c name >>>> connection
DROP DATABASE name 

\d >>>> display tables
\d nametable >>>displays atble

\i 'c:?users/ja' >>> imports db
SELECT * FROM table >>. wyswietla zawartosc tabeli
SELECT * FROM table WHERE column1='female' AND column2='Poland' >>>>filtr
SELECT * FROM table WHERE email LIKE '%.com';
SELECT * FROM table ORDER BY column1 DESC, 
DISTINCT - bez duplikatów
OFFSET 5 LIMIT 5 >>> wyswietla 6-10


CREATE TABLE tablename(xolumnname, datatype, constraints)

\? help

NOT NULL
VARCHAR(40)







'''