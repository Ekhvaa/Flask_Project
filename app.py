from flask import Flask, redirect, url_for, render_template, request, session, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from api import Film

app = Flask(__name__)
app.secret_key = "bacho123"


@app.route('/', methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        print("Form Data:", request.form)
        if "user_input" in request.form:
            usr_inpt = request.form["user_input"]
            movie = Film(usr_inpt)

            movie_data = movie.response
            session['movie_data'] = movie_data

            return redirect(url_for('result'))
        else:
            flash('No input received. Please enter a film name.')
            return redirect(url_for('home'))
    return render_template("indexx.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["user_email"]
        passwd = request.form["user_password"]
        session["user_email"] = user
        return redirect('/home')
    return render_template("loginn.html")


@app.route('/logout')
def logout():
    session.pop("user_email", None)
    session.pop("movie_data", None)
    return redirect('/login')


@app.route('/result')
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)

