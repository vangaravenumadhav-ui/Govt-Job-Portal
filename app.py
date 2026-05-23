from flask import Flask, render_template, request, redirect, session
import sqlite3
from scraper import get_live_jobs
from ai import recommend_jobs

app = Flask(__name__)
app.secret_key = "govtjobportal"

# ---------------- DATABASE ----------------

def create_table():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()

# ---------------- LOGIN PAGE ----------------

@app.route("/")
def home():
    return render_template("login.html")

# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users(username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("register.html")

# ---------------- LOGIN ----------------

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    conn.close()

    if user:
        session["user"] = username
        return redirect("/dashboard")

    return "Invalid Username or Password"

# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")

# ---------------- AI JOBS ----------------

@app.route("/jobs", methods=["GET", "POST"])
def jobs():

    recommended_jobs = []

    if request.method == "POST":

        branch = request.form["branch"]

        recommended_jobs = recommend_jobs(branch)

    return render_template(
        "jobs.html",
        jobs=recommended_jobs
    )

# ---------------- LIVE JOBS ----------------

@app.route("/livejobs")
def livejobs():

    jobs = get_live_jobs()

    return render_template(
        "livejobs.html",
        jobs=jobs
    )

# ---------------- ROADMAP ----------------

@app.route("/roadmap/<job_name>")
def roadmap(job_name):

    skills = [
        "Aptitude",
        "Reasoning",
        "General Knowledge",
        "Technical Skills",
        "Communication Skills"
    ]

    books = [
        {
            "name": "Quantitative Aptitude",
            "link": "https://www.amazon.in/"
        },
        {
            "name": "General Knowledge 2025",
            "link": "https://www.amazon.in/"
        },
        {
            "name": "Reasoning Ability",
            "link": "https://www.amazon.in/"
        },
        {
            "name": "Technical Interview Guide",
            "link": "https://www.amazon.in/"
        }
    ]

    return render_template(
        "roadmap.html",
        job_name=job_name,
        skills=skills,
        books=books
    )

# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")

# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)