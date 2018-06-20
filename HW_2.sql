#2.2.1
SELECT studentid
FROM book_checkout b
WHERE CURRENT_DATE - b.dateout > 30;

#2.2.2
SELECT studentid, name
FROM student s
WHERE avg(s.gpa) < s.gpa;

#2.2.3
SELECT facultyid, name
FROM faculty f
WHERE f.salary > 80000
	AND f.facultyid NOT IN (SELECT instructorid FROM course);
#2.2.4
SELECT DISTINCT b.title, textbookid
FROM course c RIGHT JOIN book b ON c.textbookid = b.bookid
WHERE c.textbookid IN (SELECT textbookid
		FROM course c
		GROUP BY c.textbookid
		HAVING COUNT(textbookid) > 1)
##
SELECT bookid, title
FROM (
		SELECT bookid, b.title, COUNT(bookid) as c
		FROM book b, course  WHERE textbookid = bookid
GROUP by bookid)
		AS cb
WHERE c >1

#2.2.5
SELECT DISTINCT s.studentid , s.name
FROM book_checkout bc NATURAL  JOIN student s
WHERE s.studentid = (
	SELECT studentid
	FROM book_checkout bc
	GROUP BY bc.studentid
	HAVING COUNT(bc.studentid) > 1)

#2.2.6
SELECT DISTINCT name
from book_checkout bc, enroll e, course c, student s
WHERE bc.studentid = e.studentid
AND	c.courseid = e.courseid
AND	c.textbookid != bc.bookid
AND s.studentid = bc.studentid

#2.2.7



#2.2.9
SELECT courseid, c.title
FROM course c, book b
WHERE c.textbookid = b.bookid AND price = (SELECT MAX(price) FROM book) 