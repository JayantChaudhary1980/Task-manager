# Task Management System

A simple Task Management System developed using **Python (Flask)**, **SQLite**, **HTML**, and **CSS**.

---

## Features

- User Login Authentication
- Add New Tasks
- Assign Tasks to Employees
- Toggle Task Status (Completed / Pending)
- Delete Tasks
- SQLite Database Integration
- Separate Task Title Table
- Foreign Key Relationship
- SQL JOIN Implementation
- Clean and Responsive User Interface

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3

---

## Project Structure

```
TASK_MANAGEMENT/
│
├── app.py
├── task_management.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── login.html
│   └── tasks.html
│
└── static/
    └── style.css
```

---

## Database Tables

### 1. Login

Stores user credentials.

| Column | Type |
|---------|------|
| id | INTEGER |
| username | TEXT |
| password | TEXT |

---

### 2. Task Titles

Stores predefined task names.

| Column | Type |
|---------|------|
| title_id | INTEGER |
| title_name | TEXT |

---

### 3. Tasks

Stores employee task details.

| Column | Type |
|---------|------|
| task_id | INTEGER |
| employee_name | TEXT |
| title_id | INTEGER |
| completed | INTEGER |

Relationship:

```
task_titles (1)
        │
        │
        ▼
tasks (Many)
```

---

## How to Run

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

---

### 2. Install Flask

```
pip install flask
```

---

### 3. Run the Project

```
python app.py
```

---

### 4. Open in Browser

```
http://127.0.0.1:5000
```

---

## Default Login

Username

```
admin
```

Password

```
admin123
```

---

## Project Workflow

```
Login
   │
   ▼
Dashboard
   │
   ▼
Add Task
   │
   ▼
Store in SQLite Database
   │
   ▼
Display using SQL JOIN
   │
   ▼
Update/Delete Task
```

---

## Bonus Features Implemented

- Login Authentication
- Dropdown Task Selection
- Foreign Key Constraint
- SQL JOIN
- Toggle Task Status
- Delete Task
- Responsive User Interface

---

## Future Improvements

- Edit Task
- Search Tasks
- Filter by Status
- User Registration
- Multiple User Roles

---

## Developed By

Jayant Chaudhary