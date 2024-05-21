/*
SQL >> Selected query language >> SQL bir sorgu dilidir. Sirf databaza ile, datalar ile islemek ucundur. 
Arasdirmaq istesez (PL/SQL, SQL / NOSQL)
* DDL - data tanitmaq, elave etmek, yaratmaq ucundur
* DML - Data sorgular ile yoxlanilmasi, conf edilmesi
* DCL - Datalarin yoxlanilmasi.

DDL: CREATE, ALTER, DROP
DML: SELECT, INSERT, UPDATE, DELETE
DCL: GRANT, DENY, REVOKE

SQL sintaksis >> ister boyuk, ister kicik herflerle. Ister yan-yana ister alt alta kodlar yaza bilersiz. (Meslehetim boyuk herflerle yan yana yazmaginizdir)
    
SELECT: Databazada datalari secmek, isarelemek ucundur.
Ex: SELECT * FROM HR.EMPLOYEES;     /     select * from hr.employees;
SELECT 

FROM HR.EMPLOYEES;

-- * Butun datalari isaret edir.
-- HR.EMPLOYEES bizim databazamizin, table-mizin adidir.
-- SELECT * FROM HR.EMPLOYEES;
-- select * from hr.employees;
-- SELECT 
-- * 
-- FROM 
-- HR.EMPLOYEES;


-- SELECT * FROM HR.EMPLOYEES;
-- SELECT FIRST_NAME, LAST_NAME FROM HR.EMPLOYEES;

/*
SELECT-de ne kimi datalari filtirlemek ucun ozellikler, kodlar movcuddur:
WHERE - Table-da hansi datani secmek isteyirsen, is gormek isteyirsense onu isaret edirsen
ORDER BY - Secilen datani siralamaq ucundur(SORT)
GROUP BY - Datalarin gruplasdirilmasinda rol oynayir.
*/

-- ORDER BY:
-- SELECT * FROM HR.EMPLOYEES;
-- SELECT * FROM HR.EMPLOYEES ORDER BY SALARY; >> maasi kicikden boyuye dogru siralayir
-- SELECT * FROM HR.EMPLOYEES ORDER BY SALARY DESC; >> maasi boyukden kiciye dogru siralayir

-- WHERE:
-- SELECT * FROM HR.EMPLOYEES;
-- SELECT FIRST_NAME, SALARY FROM HR.EMPLOYEES WHERE SALARY BETWEEN 10000 AND 24000; >> Maasi [10min-24min] araliginda olan userleri goster
-- SELECT FIRST_NAME, SALARY FROM HR.EMPLOYEES WHERE SALARY BETWEEN 10000 AND 24000 ORDER BY SALARY;
-- SELECT * FROM HR.EMPLOYEES WHERE JOB_ID='IT_PROG' AND SALARY BETWEEN 5000 AND 10000 ORDER BY SALARY;
-- SELECT FIRST_NAME, SALARY FROM HR.EMPLOYEES WHERE SALARY BETWEEN 24000 AND 10000; >> reqem kicikden boyuye dogru irellemelidir

-- SELECT * FROM HR.EMPLOYEES WHERE FIRST_NAME LIKE '%xan%' >> Like operatoru include kimi fikirlese bilerik.
-- % onde olduqda sonlugu, sonda olduqda on hissede axtaris edir. Hem son hem evvelde olduqda datanin icerisinde axtaris edir.


-- GROUP BY
-- SELECT * FROM HR.EMPLOYEES;
SELECT JOB_ID, SUM(SALARY) AS TOTAL_SALARY FROM HR.EMPLOYEES HAVING SUM(SALARY) > 40000 GROUP BY JOB_ID ORDER BY TOTAL_SALARY;


task1)
İlk olaraq satışı reallaşmış məhsullar üçün bir cədvəl (tabel) 
yaradırıq və bu cədvəlimizin sütun olaraq məhsul idsi, sayı və
dəyəri (1 dənəsinin)  olacaq. Biz isə hər məhsul 
üçün ümumi olan qazancı gətirib sıralamaq lazımdır

task2)
işçilər adında cədvəlimiz olacaq. Sütun olaraq ad,maaş,
departament olacaq. Siz isə departamentinin adı satış olan 
və maaşı 600-dən çox olan şəxslərin maaşını azalan sıra ilə 
sıralıyın

task3)
kitablar cədvəlimiz olacaq. Sütunları: adı, janrı, nəşr ili
.2015-dən sonra nəşr olunmuş kitbaabları janrına görə artan
sıra ilə sıralıyın

task4)
filmlər adlı cədvəlimiz olacaq. Sütunları : ad, çıxış tarixi,
ratinq. Çıxış tarixi 2000-dən kiçik olanları artan sıra və 
ratingi 7-dən böyük olanları azalan sıra ilə sıralıyın
