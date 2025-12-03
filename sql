CREATE DATABASE student_db;

USE student_db;

CREATE TABLE student_marks(
    roll INT PRIMARY KEY,
    name VARCHAR(50),
    gender VARCHAR(10),
    attendance FLOAT,
    maths INT,
    science INT,
    english INT,
    computer INT
);


INSERT INTO student_marks VALUES
(1, 'Aarav', 'Male', 92, 85, 78, 90, 88),
(2, 'Reva', 'Female', 88, 72, 68, 74, 95),
(3, 'Arjun', 'Male', 76, 90, 82, 65, 60),
(4, 'Sara', 'Female', 96, 95, 91, 89, 99),
(5, 'Rohan', 'Male', 59, 55, 60, 58, 70),
(6, 'Prisha', 'Female', 81, 70, 75, 88, 92),
(7, 'Ishan', 'Male', 85, 82, 80, 72, 68),
(8, 'Vani', 'Female', 91, 88, 86, 94, 90);
