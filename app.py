from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from scraper import get_live_jobs

app = Flask(__name__)
app.secret_key = "secret123"


# ================= DATABASE ================= #

def create_table():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        age TEXT,
        qualification TEXT,
        branch TEXT
    )
    """)

    conn.commit()
    conn.close()


create_table()


# ================= LOGIN ================= #

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):

            session["username"] = username

            return redirect("/jobs")

        else:
            return "Invalid Login ❌"

    return render_template("login.html")


# ================= REGISTER ================= #

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        try:

            username = request.form["username"]

            password = generate_password_hash(
                request.form["password"]
            )

            age = request.form["age"]

            qualification = request.form["qualification"]

            branch = request.form["branch"]

            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO users(
                username,
                password,
                age,
                qualification,
                branch
            )
            VALUES(?,?,?,?,?)
            """, (
                username,
                password,
                age,
                qualification,
                branch
            ))

            conn.commit()
            conn.close()

            return redirect("/")

        except Exception as e:
            return f"Database Error: {e}"

    return render_template("register.html")


# ================= AI JOBS ================= #

@app.route("/jobs")
def jobs():

    if "username" not in session:
        return redirect("/")

    username = session["username"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT qualification, branch FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    qualification = user[0]
    branch = user[1]

    jobs = []

    if qualification == "BTech":

        if branch == "CSE":
            jobs = [
                {
                    "title": "NIC Scientist B",
                    "link": "https://www.nielit.gov.in/"
                },
                {
                    "title": "ISRO Scientist",
                    "link": "https://www.isro.gov.in/"
                },
                {
                    "title": "DRDO Engineer",
                    "link": "https://www.drdo.gov.in/"
                }
            ]

        elif branch == "ECE":
            jobs = [
                {
                    "title": "BSNL Junior Engineer",
                    "link": "https://www.bsnl.co.in/"
                },
                {
                    "title": "ISRO Technical Assistant",
                    "link": "https://www.isro.gov.in/"
                }
            ]

        elif branch == "EEE":
            jobs = [
                {
                    "title": "Power Grid Engineer",
                    "link": "https://www.powergrid.in/"
                },
                {
                    "title": "BHEL Engineer",
                    "link": "https://www.bhel.com/"
                }
            ]

        else:
            jobs = [
                {
                    "title": "SSC JE",
                    "link": "https://ssc.nic.in/"
                }
            ]

    elif qualification == "Degree":

        jobs = [
            {
                "title": "SSC CGL",
                "link": "https://ssc.nic.in/"
            },
            {
                "title": "Bank PO",
                "link": "https://www.ibps.in/"
            }
        ]

    elif qualification == "Intermediate":

        jobs = [
            {
                "title": "Railway Clerk",
                "link": "https://www.rrbcdg.gov.in/"
            },
            {
                "title": "Police Constable",
                "link": "https://www.tslprb.in/"
            }
        ]

    else:

        jobs = [
            {
                "title": "Group D",
                "link": "https://www.rrbcdg.gov.in/"
            }
        ]

    return render_template("jobs.html", jobs=jobs)


# ================= LIVE JOBS ================= #

@app.route("/livejobs")
def livejobs():

    live_jobs = get_live_jobs()

    return render_template(
        "livejobs.html",
        live_jobs=live_jobs
    )


# ================= ROADMAP ================= #

@app.route("/roadmap/<job_name>")
def roadmap(job_name):

    skills = [
        "Aptitude",
        "Reasoning",
        "General Knowledge",
        "Technical Skills"
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
        }
    ]

    return render_template(
        "roadmap.html",
        job_name=job_name,
        skills=skills,
        books=books
    )


# ================= LOGOUT ================= #

@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")


# ================= RUN ================= #

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)