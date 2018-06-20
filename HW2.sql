DROP TABLE book CASCADE;
DROP TABLE faculty CASCADE;
DROP TABLE student CASCADE;
DROP TABLE course CASCADE;
DROP TABLE enroll CASCADE;
DROP TABLE book_checkout CASCADE;

CREATE TABLE book
(
	bookid			numeric(2, 0),
	title			varchar(20),
	price			numeric(4, 2),
 	total_copies	numeric(2, 0),
	PRIMARY KEY (bookid)
);

CREATE TABLE faculty
(
	facultyid		numeric(2, 0), 
	name			varchar(20),  
	salary			numeric(6, 0),
	PRIMARY KEY (facultyid)
);

CREATE TABLE student
(
 	studentid		numeric(2, 0), 
	name			varchar(10), 
	gpa 			numeric(2, 1),
	PRIMARY KEY (studentid)
);

CREATE TABLE course
(
	courseid		numeric(2, 0), 
	title			varchar(20), 
	instructorid	numeric(2,0),
	textbookid		numeric(2, 0),
	PRIMARY KEY (courseid),
	FOREIGN KEY (instructorid) REFERENCES faculty
		ON DELETE SET NULL,
	FOREIGN KEY (textbookid) REFERENCES book
		ON DELETE SET NULL
);

CREATE TABLE enroll
(
    studentid		numeric(2, 0), 
    courseid		numeric(2, 0),
 	PRIMARY KEY (studentid, courseid),
 	FOREIGN KEY (studentid) REFERENCES student
		ON DELETE CASCADE,
	FOREIGN KEY (courseid) REFERENCES course
		ON DELETE CASCADE
);

CREATE TABLE book_checkout
(
 	dateout			date, 
	bookid			numeric(2, 0),
	studentid		numeric(2, 0), 
	PRIMARY KEY (bookid, studentid),
	FOREIGN KEY (bookid) REFERENCES book
		ON DELETE CASCADE,
	FOREIGN KEY (studentid) REFERENCES student
		ON DELETE CASCADE
);


DELETE FROM book;
DELETE FROM course;
DELETE FROM student;
DELETE FROM faculty;
DELETE FROM enroll;
DELETE FROM book_checkout;
INSERT INTO book VALUES ('1', 'Algo', '84.66', '4');
INSERT INTO book VALUES ('2', 'DSC', '74.99', '5');
INSERT INTO book VALUES ('3', 'F1', '41.02', '3');
INSERT INTO book VALUES ('4', 'F2', '55.22', '3');

INSERT INTO student VALUES ('1', 'Tom', '3.3');
INSERT INTO student VALUES ('2', 'John', '3.8');
INSERT INTO student VALUES ('3', 'Mary', '3.0');
INSERT INTO student VALUES ('4', 'Kris', '3.6');
INSERT INTO student VALUES ('5', 'Alex', '3.5');

INSERT INTO faculty VALUES ('1', 'James', '70000');
INSERT INTO faculty VALUES ('2', 'Sarah', '60000');
INSERT INTO faculty VALUES ('3', 'Jay', '80000');
INSERT INTO faculty VALUES ('4', 'Rachel', '70000');
INSERT INTO faculty VALUES ('5', 'Paul', '85000');

INSERT INTO course VALUES ('1', 'Algo', '1', '1');
INSERT INTO course VALUES ('2', 'DB', '2', '2');
INSERT INTO course VALUES ('3', 'ADB', '3', '2');
INSERT INTO course VALUES ('4', 'F1', '1', '3');
INSERT INTO course VALUES ('5', 'F2', '4', '4');

INSERT INTO enroll VALUES ('1', '1');
INSERT INTO enroll VALUES ('1', '2');
INSERT INTO enroll VALUES ('2', '1');
INSERT INTO enroll VALUES ('4', '3');
INSERT INTO enroll VALUES ('4', '4');
INSERT INTO enroll VALUES ('5', '5');

INSERT INTO book_checkout VALUES ('2017-08-29', '1', '1');
INSERT INTO book_checkout VALUES ('2017-09-02', '4', '4');
INSERT INTO book_checkout VALUES ('2017-09-07', '1', '4');




























