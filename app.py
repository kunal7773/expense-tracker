from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route('/')
def dashboard():
    db = get_db()
    expenses = db.execute("SELECT * FROM expenses").fetchall()

    total = sum([e[2] for e in expenses])

    labels = [e[1] for e in expenses]
    values = [e[2] for e in expenses]

    return render_template(
        "dashboard.html",
        expenses=expenses,
        total=total,
        labels=labels,
        values=values
    )

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    amount = request.form['amount']
    db = get_db()
    db.execute("INSERT INTO expenses (title, amount) VALUES (?, ?)", (title, amount))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    db = get_db()
    db.execute("DELETE FROM expenses WHERE id=?", (id,))
    db.commit()
    return redirect('/')

@app.route('/expenses')
def expenses_page():
    db = get_db()
    expenses = db.execute("SELECT * FROM expenses").fetchall()
    return render_template("expenses.html", expenses=expenses)

@app.route('/reports')
def reports():
    db = get_db()
    expenses = db.execute("SELECT * FROM expenses").fetchall()
    total = sum([e[2] for e in expenses])
    return render_template("reports.html", total=total)

app.run(debug=True)