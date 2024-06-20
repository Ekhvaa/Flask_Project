from flask import Flask, redirect, url_for, render_template, request, session, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "bacho123"

@app.route('/')
@app.route("/home")
def home():
    return render_template("indexx.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["user_email"]
        passwd = request.form["user_password"]
        session["user_email"] = user
        return redirect('/home')
    return render_template("loginn.html")


if __name__ == "__main__":
    app.run(debug=True)

