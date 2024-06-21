from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from api import Film

app = Flask(__name__)
app.secret_key = "bacho123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Filmebiiii.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_title = db.Column(db.String(100), nullable=False)
    film_genre = db.Column(db.String(100), nullable=False)
    film_rating = db.Column(db.Float, nullable=False)
    film_plot = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # print("Form Data:", request.form)
        usr_inpt = request.form.get("user_input")
        if usr_inpt:
            movie = Film(usr_inpt)
            t = movie.title
            g = movie.genres
            r = movie.rating
            p = movie.plot()
            filmi = Movies(film_title=t, film_genre=g, film_rating=r, film_plot=p)
            db.session.add(filmi)
            db.session.commit()
            return redirect(url_for('result'))
        else:
            flash('No input received. Please enter a film name.')
            return redirect(url_for('home'))
    return render_template("indexx.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["user_email"]
        passwd = generate_password_hash(request.form["user_password"])
        usr1 = User(username=user, password=generate_password_hash(passwd))
        db.session.add(usr1)
        db.session.commit()
        session["user_email"] = user
        return redirect('/home')
    return render_template("loginn.html")


@app.route('/logout')
def logout():
    session.pop("user_email", None)
    return redirect('/login')


@app.route('/result')
def result():
    latest_movie = Movies.query.order_by(Movies.id.desc()).first()
    if latest_movie:
        movie_title = latest_movie.film_title
        movie_genres = latest_movie.film_genre
        movie_rating = latest_movie.film_rating
        movie_plot = latest_movie.film_plot
    else:
        movie_title = "No movies found."
        print(movie_title)
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)
