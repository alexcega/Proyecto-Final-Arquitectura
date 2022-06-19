from crypt import methods
from distutils.log import debug
from xml.etree.ElementTree import tostring
# from tkinter.tix import Select
from flask import Flask, request, render_template, redirect, url_for
from movies import models
from movie_fetcher import session
import pandas as pd


desc = False
magic_number = 1

app = Flask(__name__)
models.start_mappers()
app.run(debug=True)
# !The Open Closed Principle:
# Tener distintas rutas nos ayuda a probar los elementos agregados sin que se empalmen unos con otros

# @app.route("/hello", methods=["GET"])
# def hello_world():
#     return "Hello World!", 200

@app.route("/fin")
def fin():
    # !The Interface Segregation Principle
    # Se renderiza en la pantalla solo la informacion necesaria
    Obj1 = session.query(models.Movie).all()
    return render_template('add_user.html', Obj1 = Obj1)

@app.route("/post_user")
def post_user():
    user = models.Movie(request.form['preference_key'], request.form['movie_title'])
    session.add(user)
    session.commit()
    return redirect(url_for(fin))

@app.route("/login", methods = ['GEt','POST'])
def startUser():
    if request.method == 'POST':
        session.pop('user_id', None)
        usarname = request.form['username']
        password = request.form['password']
    return render_template('login.html')

@app.route('/profile')
def myProfile():
    return render_template('profile.html')

@app.route("/recom")
def recomendation():  
    df = pd.read_csv('/src/movies/entrypoints/movie_results.csv')
    movie = df[df['preference_key'] == 1]
    movie = movie.head(10)
    # movie = movie.tail(10)
    return(movie.to_html(), 200)







    