from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "change_this_to_a_random_secret_key"

DATABASE = "task_management.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS login(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS task_titles(
        title_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title_name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS tasks(
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_name TEXT NOT NULL,
        title_id INTEGER NOT NULL,
        completed INTEGER DEFAULT 0,
        FOREIGN KEY(title_id) REFERENCES task_titles(title_id)
    );
    """)

    cursor.execute("SELECT COUNT(*) FROM login")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO login(username,password) VALUES(?,?)",
            [
                ("admin", "admin123"),
                ("employee1", "pass123")
            ]
        )

    cursor.execute("SELECT COUNT(*) FROM task_titles")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO task_titles(title_name) VALUES(?)",
            [
                ("Design UI",),
                ("Backend Development",),
                ("Database Setup",),
                ("Testing",),
                ("Deployment",),
                ("Documentation",)
            ]
        )

    conn.commit()
    conn.close()


@app.route("/")
def index():
    if "username" in session:
        return redirect(url_for("tasks"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM login WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            session["username"] = username
            return redirect(url_for("tasks"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/tasks", methods=["GET", "POST"])
def tasks():

    if "username" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        employee_name = request.form["employee_name"]
        title_id = request.form["title_id"]

        cursor.execute(
            """
            INSERT INTO tasks(employee_name,title_id,completed)
            VALUES(?,?,?)
            """,
            (employee_name, title_id, 0)
        )

        conn.commit()

    cursor.execute("""
        SELECT title_id,title_name
        FROM task_titles
        ORDER BY title_name
    """)

    task_titles = cursor.fetchall()

    cursor.execute("""
        SELECT
            t.task_id,
            t.employee_name,
            tt.title_name,
            t.completed
        FROM tasks t
        JOIN task_titles tt
            ON t.title_id = tt.title_id
        ORDER BY t.task_id DESC
    """)

    all_tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "tasks.html",
        tasks=all_tasks,
        task_titles=task_titles,
        username=session["username"]
    )


@app.route("/toggle/<int:task_id>")
def toggle(task_id):

    if "username" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET completed =
            CASE
                WHEN completed=0 THEN 1
                ELSE 0
            END
        WHERE task_id=?
    """, (task_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("tasks"))


@app.route("/delete/<int:task_id>")
def delete(task_id):

    if "username" not in session:
        return redirect(url_for("login"))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE task_id=?",
        (task_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("tasks"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)