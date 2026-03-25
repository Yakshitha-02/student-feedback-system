from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database connection
def get_db():
    conn = sqlite3.connect("feedback.db")
    return conn

# Main route
@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    cursor = conn.cursor()

    # Handle form submission
    if request.method == "POST":
        name = request.form["name"]
        feedback = request.form["feedback"]

        cursor.execute(
            "INSERT INTO feedback (name, message) VALUES (?, ?)",
            (name, feedback)
        )
        conn.commit()
        return redirect("/")

    # Fetch feedback
    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()
    conn.close()

    return render_template("index.html", feedback=data)


# Run app
if __name__ == "__main__":
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            message TEXT
        )
    """)
    conn.close()

    app.run(host="0.0.0.0", port=5000)