-- Task Management System - Database Schema

CREATE DATABASE IF NOT EXISTS task_management_db;
USE task_management_db;

-- 1) LOGIN TABLE
CREATE TABLE IF NOT EXISTS login (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Sample credentials (change/add your own)
INSERT INTO login (username, password) VALUES
    ('admin', 'admin123'),
    ('employee1', 'pass123');

-- 2) TASK TITLES TABLE (Bonus: separate lookup table for dropdown)
CREATE TABLE IF NOT EXISTS task_titles (
    title_id INT AUTO_INCREMENT PRIMARY KEY,
    title_name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO task_titles (title_name) VALUES
    ('Design UI'),
    ('Backend Development'),
    ('Database Setup'),
    ('Testing'),
    ('Deployment'),
    ('Documentation');

-- 3) TASK MANAGEMENT TABLE
-- Task ID (Auto Increment PK), Employee Name, Task Title (via FK), Completed
CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    title_id INT NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (title_id) REFERENCES task_titles(title_id)
);

-- Sample tasks (optional, remove if not needed)
INSERT INTO tasks (employee_name, title_id, completed) VALUES
    ('Rahul Sharma', 1, FALSE),
    ('Priya Verma', 2, TRUE);
