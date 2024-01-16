import os

# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helper import apology, login_required
import sqlite3


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure SQLIite to replace CS50 library
conn = sqlite3.connect('students.db', check_same_thread=False)
db = conn.cursor()
# db = SQL("sqlite:///students.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])  # Complete
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        db.execute(
            "SELECT * FROM students WHERE user_name = ?", (request.form.get("username"),)
        )
        rows = db.fetchall()
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0][4], request.form.get("password")):
            print('incorrect password')
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0][0]

        # Redirect user to home page
        flash("Welcome!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    # close database
    # conn.close()
    # Redirect user to login form
    return redirect("/")

@app.route("/")
@login_required
def index():
    """SHOW CLASS LIST AS A SELECTION"""
    db.execute("SELECT * FROM classes")
    classes = db.fetchall()
    return render_template("index.html", classes=classes)

@app.route("/punch_cards")
@login_required
def punch_cards():
    student_punchCards = db.execute("SELECT * FROM students WHERE student_id = ?", session.get("user_id")
    )
    attendance = db.execute("SELECT * FROM attendance JOIN classes ON classes.course_id = attendance.course_id WHERE student_id = ? AND punch_card = 1", session.get("user_id")
    )
    return render_template("punch_cards.html", attendance=attendance, student_punchCards=student_punchCards)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide user name")
        if not request.form.get("first_name"):
            return apology("must provide full name")
        if not request.form.get("last_name"):
            return apology("must provide full name")
        if not request.form.get("password"):
            return apology("must provide password")
        if not request.form.get("confirmation"):
            return apology("must provide confirmation")
        user_name = request.form.get("username")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # confirm that there is data in username field - form kept submitting on refresh without this
        
        print(f"this line: {user_name}, {first_name}, {last_name}, {password}, {confirmation}")
        if user_name == "":
            return apology("please enter a username")
        else:
            if user_name:
                db.execute("SELECT * FROM students WHERE user_name = ?", (user_name,))
                database = db.fetchone()
                # print(f"database response: {database}")
                if database == None:
                    # confirm password and confirmation match - feild is required in html so it cannot be blank
                    if password == confirmation:
                        hashpass = generate_password_hash(
                            password, method="pbkdf2", salt_length=16
                        )
                        db.execute(
                            "INSERT INTO students (user_name, student_firstname, student_lastname, hash) VALUES(?, ?, ?, ?)",
                            (
                            user_name,
                            first_name,
                            last_name,
                            hashpass
                        )
                        )
                        # print(counter,user_name, first_name, last_name, hashpass)
                        conn.commit()
                        flash("Registered!")
                        return redirect("/")
                    else:
                        return apology("Passwords DO NOT MATCH")
                else:
                    return apology("Check USERNAME OR PASSWORD")
    return render_template("register.html")

@app.route("/signup", methods=["POST"])
def signup():
    id = request.form.get("course_id")
    student_id = session.get("user_id")
    day = f"{datetime.now():%d}"
    month = f"{datetime.now():%m}"
    year = f"{datetime.now():%Y}"
    punch = request.form.get("punch")
    # db.execute("SELECT punch_card FROM students WHERE student_id = ?", (student_id,))
    # student_punches = db.fetchone()
    # print(student_punches)
    # current_punches = student_punches[0]["punch_card"]
    # print(f"punches used: {punch}")
    if id.isnumeric():
        if punch == '1':
            punch = int(punch)
            if current_punches > 0:
                # print(student_punches[0]["punch_card"])
                updated_punches = student_punches[0]["punch_card"] - 1
                # print(f"{updated_punches} entered into db")
                # db.execute("UPDATE students SET punch_card = ? Where student_id = ?;", updated_punches, student_id)
                # db.execute(
                    # "INSERT INTO attendance (course_id, student_id, day, month, year, punch_card) VALUES(?,?,?,?,?,?);",
                    # id,
                    # student_id,
                    # int(day),
                    # int(month),
                    # int(year),
                    # punch
                    # )
                flash("Signed In!")
                return redirect("/")
            else:
                return apology("No punches left")
        else:
            print(f"no punches, class entered into db")
            # db.execute(
            # "INSERT INTO attendance (course_id, student_id, day, month, year, punch_card) VALUES(?,?,?,?,?,?);",
            # id,
            # student_id,
            # int(day),
            # int(month),
            # int(year),
            # 0
            # )
            flash("Signed In!")
            return redirect("/")
    else:
        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # user = db.execute("SELECT * FROM users WHERE id = ?;", session.get("user_id"))
    table = db.execute(
        "SELECT * FROM attendance JOIN classes ON classes.course_id = attendance.course_id WHERE student_id = ? ORDER BY month DESC, day DESC;", session.get("user_id")
    )
    return render_template("/history.html", table=table)

@app.route("/descriptions") # Complete
@login_required
def description():
    db.execute("SELECT * FROM classes;")
    class_rows = db.fetchall()
    return render_template("/descriptions.html", class_rows=class_rows)

# ------ADMIN Pages -------------------
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
        """Log user in"""
        # Forget any user_id
        session.clear()

        # User reached route via POST (as by submitting a form via POST)
        if request.method == "POST":
            # Ensure username was submitted
            if not request.form.get("username"):
                return apology("must provide username", 403)

            # Ensure password was submitted
            elif not request.form.get("password"):
                return apology("must provide password", 403)

            # Query database for username
            rows = db.execute(
                "SELECT * FROM students WHERE user_name = ?", request.form.get("username")
            )

            # Ensure username exists and password is correct
            if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
                return apology("invalid username and/or password", 403)

            # Remember which user has logged in
            session["user_id"] = rows[0]["student_id"]

            # Validate that user is admin
            print(type(session["user_id"]))
            if session["user_id"] not in [1, 2]:
                return apology("not admin account", 403)

            # Redirect user to admin landing page
            flash("Welcome Admin!")
            return redirect("/admin")

        # User reached route via GET (as by clicking a link or via redirect)
        else:
            return render_template("/admin_login.html")

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    """SHOW CLASS LIST AS A SELECTION"""
    classes = db.execute("SELECT * FROM classes")
    students = db.execute("SELECT * FROM students")
    course = request.form.get("class")
    student = request.form.get("student")
    if request.method == "GET":
        return render_template("/admin.html", classes=classes, students=students)
    else:
        if course:
            print(course)
            course_search = db.execute("SELECT *, COUNT(attendance.student_id) as count FROM attendance JOIN students ON students.student_id = attendance.student_id JOIN classes ON classes.course_id = attendance.course_id WHERE classes.course_id = ? GROUP by attendance.day;", course)
            return render_template("/admin_search.html", course_search=course_search)
        elif student:
            print(student)
            student_search = db.execute("SELECT *, COUNT(attendance.day) AS count FROM attendance JOIN classes on classes.course_id = attendance.course_id WHERE attendance.student_id = ? GROUP BY attendance.course_id;", student)
            return render_template("/admin_search.html", student_search=student_search)
        else:
            return redirect("/admin")

@app.route("/admin_history")
@login_required
def admin_history():
    """Show history of transactions"""
    # user = db.execute("SELECT * FROM users WHERE id = ?;", session.get("user_id"))
    table = db.execute(
        "SELECT * FROM attendance JOIN classes ON classes.course_id = attendance.course_id JOIN students ON students.student_id = attendance.student_id ORDER BY month DESC, day DESC;")
    return render_template("/admin_history.html", table=table)


@app.route("/admin_punch_cards", methods=["GET", "POST"])
@login_required
def admin_punch_cards():
    students = db.execute("SELECT * FROM students;")
    if request.method == "GET":
        return render_template("/admin_punch_cards.html", students=students)
    else:
        id = request.form.get("student")
        punch = request.form.get("punches")
        db.execute("UPDATE students SET punch_card = (punch_card + ?) WHERE student_id = ?", punch, id)
        # return render_template("/admin_punch_cards.html", students=students)
        flash("updated")
        return redirect("/admin_punch_cards")

if __name__ == "__main__":
    app.run(debug=True)