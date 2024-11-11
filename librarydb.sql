CREATE TABLE library_user(
	user_id BIGSERIAL PRIMARY KEY ,
	user_name varchar(50),
	department varchar(30),
	email varchar(50) UNIQUE,
	mobile_number bigint UNIQUE,
	CONSTRAINT check_mobile_number CHECK(mobile_number BETWEEN 1000000000 AND 9999999999),
	CONSTRAINT department_check CHECK (department IN ('Computer Science', 'Electronics', 'Electrical', 'Mechanical', 'Robotics', 'Civil', 'B.Arch'))
);

CREATE TABLE faculty(
	user_id bigint PRIMARY KEY,
	faculty_id varchar(10) UNIQUE,
	designation varchar(30),
	FOREIGN KEY (user_id) REFERENCES library_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE student(
	user_id bigint PRIMARY KEY,
	admission_no varchar(10) UNIQUE,
	student_year int,
	roll_no int,
	CONSTRAINT check_student_year CHECK(student_year BETWEEN 1 AND 5),
	FOREIGN KEY (user_id) REFERENCES library_user(user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE book(
	book_id bigserial PRIMARY KEY UNIQUE,
	title varchar(50),
	author varchar(50),
	category varchar(25),
	lending_status varchar(20) DEFAULT 'Available',
	edition int,
	CONSTRAINT category_check CHECK (category IN ('Novel', 'Story', 'Poem', 'Biography', 'Drama', 'Philosophy', 'Autobiography', 'Children’s Literature', 'Textbook', 'Research', 'Reference')),
	CONSTRAINT lending_status_check CHECK (lending_status IN ('Available', 'Not Available'))
);

CREATE TABLE publish
(
	title varchar(50),
	author varchar(50),
	edition int,
	publisher varchar(50),
	publish_date date,
	primary key(title,author,edition)
);

CREATE TABLE borrow(
	user_id bigint,
	book_id bigint,
	issue_date date DEFAULT CURRENT_DATE,
	due_date date DEFAULT (CURRENT_DATE + INTERVAL '14 days'),
	return_date date,
	book_damage varchar(100) DEFAULT 'No Damage',
	return_damage varchar(100),
	fine_amount integer DEFAULT 0,
	PRIMARY KEY(user_id, book_id, issue_date)
);

ALTER SEQUENCE library_user_user_id_seq RESTART WITH 1000;
ALTER SEQUENCE book_book_id_seq RESTART WITH 10000;

INSERT INTO library_user (user_name, department, email, mobile_number) VALUES
('Rajesh Kumar', 'Computer Science', 'rajesh.kumar@university.edu', 9876543210),
('Anjali Menon', 'Electronics', 'anjali.menon@university.edu', 9765432109),
('Deepak Sharma', 'Mechanical', 'deepak.sharma@university.edu', 9988776655),
('Kavya Reddy', 'Civil', 'kavya.reddy@university.edu', 9876543298),
('Sunil Narayan', 'Electrical', 'sunil.narayan@university.edu', 9765432108),
('Madhuri Patil', 'B.Arch', 'madhuri.patil@university.edu', 9856543210),
('Lakshmi Iyer', 'Robotics', 'lakshmi.iyer@university.edu', 9765432188),
('Vinay Raj', 'Computer Science', 'vinay.raj@university.edu', 9876543234),
('Priya Thakur', 'Civil', 'priya.thakur@university.edu', 9765432177),
('Amit Mehta', 'Electronics', 'amit.mehta@university.edu', 9856743211);

INSERT INTO faculty (user_id, faculty_id, designation) VALUES
(1000, 'FAC1001', 'Professor'),
(1001, 'FAC1002', 'Assistant Professor'),
(1003, 'FAC1003', 'Associate Professor'),
(1006, 'FAC1004', 'Lecturer'),
(1008, 'FAC1005', 'Professor');

INSERT INTO student (user_id, admission_no, student_year, roll_no) VALUES
(1002, 'AD202301', 2, 51),
(1004, 'AD202302', 1, 23),
(1005, 'AD202303', 3, 32),
(1007, 'AD202304', 4, 15),
(1009, 'AD202305', 1, 48);

INSERT INTO book (title, author, category, lending_status, edition) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Novel', 'Available', 3),
('In Search of Lost Time', 'Marcel Proust', 'Story', 'Available', 1),
('To Kill a Mockingbird', 'Harper Lee', 'Drama', 'Not Available', 2),
('War and Peace', 'Leo Tolstoy', 'Novel', 'Available', 5),
('The Art of War', 'Sun Tzu', 'Philosophy', 'Not Available', 4),
('Moby Dick', 'Herman Melville', 'Novel', 'Available', 2),
('Crime and Punishment', 'Fyodor Dostoevsky', 'Drama', 'Not Available', 3),
('The Little Prince', 'Antoine de Saint-Exupéry', 'Children’s Literature', 'Not Available', 1),
('The Republic', 'Plato', 'Philosophy', 'Not Available', 2),
('A Brief History of Time', 'Stephen Hawking', 'Research', 'Available', 3);

INSERT INTO publish (title, author, edition, publisher, publish_date) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 3, 'Scribner', '1925-04-10'),
('In Search of Lost Time', 'Marcel Proust', 1, 'Grasset', '1913-11-14'),
('To Kill a Mockingbird', 'Harper Lee', 2, 'J.B. Lippincott & Co.', '1960-07-11'),
('War and Peace', 'Leo Tolstoy', 5, 'The Russian Messenger', '1869-01-01'),
('The Art of War', 'Sun Tzu', 4, 'Oxford University Press', '2003-05-01'),
('Moby Dick', 'Herman Melville', 2, 'Harper & Brothers', '1851-10-18'),
('Crime and Punishment', 'Fyodor Dostoevsky', 3, 'The Russian Messenger', '1866-01-01'),
('The Little Prince', 'Antoine de Saint-Exupéry', 1, 'Reynal & Hitchcock', '1943-04-06'),
('The Republic', 'Plato', 2, 'Penguin Classics', '2003-01-01'),
('A Brief History of Time', 'Stephen Hawking', 3, 'Bantam Books', '1988-04-01');

INSERT INTO borrow (user_id, book_id, issue_date, due_date, return_date, book_damage, return_damage, fine_amount) VALUES
(1002, 10000, '2024-10-01', '2024-10-15', '2024-10-14', 'No Damage', 'No Damage', 0),
(1003, 10001, '2024-10-05', '2024-10-19', '2024-10-18', 'No Damage', 'Slightly Worn Cover', 0),
(1004, 10002, '2024-10-07', '2024-10-21', NULL, 'No Damage', NULL, 0),
(1005, 10003, '2024-10-10', '2024-10-24', '2024-10-22', 'No Damage', 'No Damage', 0),
(1006, 10004, '2024-10-12', '2024-10-26', NULL, 'No Damage', NULL, 0),
(1007, 10005, '2024-10-15', '2024-10-29', '2024-10-30', 'No Damage', 'No Damage', 10),
(1008, 10006, '2024-10-18', '2024-11-01', NULL, 'No Damage', NULL, 0),
(1009, 10007, '2024-10-20', '2024-11-03', NULL, 'No Damage', NULL, 0),
(1003, 10008, '2024-10-22', '2024-11-05', NULL, 'No Damage', NULL, 0),
(1005, 10009, '2024-10-24', '2024-11-07', '2024-11-06', 'No Damage', 'No Damage', 0);


select * from library_user;
select * from faculty;
select * from student;
select * from book;
select * from publish;
select * from borrow;

DROP TABLE borrow;
DROP TABLE publish;
DROP TABLE book;
DROP TABLE student;
DROP TABLE faculty;
DROP TABLE library_user;