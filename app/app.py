from flask import Flask, render_template, request, redirect
import sqlite3

app.run(host='0.0.0.0', port=5000)
def get_db():
    conn = sqlite3.connect("feedback.db")
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        feedback = request.form["feedback"]
        cursor.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, feedback))
        conn.commit()
        return redirect("/")

    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()
    conn.close()

    return render_template("index.html", feedback=data)

if __name__ == "__main__":
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, name TEXT, message TEXT)")
    conn.close()
    app.run(host="0.0.0.0", port=5000)