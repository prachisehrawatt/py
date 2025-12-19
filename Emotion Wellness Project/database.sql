CREATE DATABASE wellness_db;
USE wellness_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(30),
    class VARCHAR(10)
);

CREATE TABLE daily_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    log_date DATE,
    mood VARCHAR(10),
    study_hours INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);