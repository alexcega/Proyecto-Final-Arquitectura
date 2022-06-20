from distutils.log import debug
from flask import Flask, request, render_template, redirect, url_for, g
from movies import models
from movie_fetcher import session
import pandas as pd


orden = None
magic_number = None
username = None
app = Flask(__name__)
models.start_mappers()
app.run(debug=True)


# !The Open Closed Principle:
# Tener distintas rutas nos ayuda a probar los elementos agregados sin que se empalmen unos con otros
#* Sign up view y seleccion de categorias
@app.route("/sign_up", methods = ['GEt','POST'])
def mySignUp():
    global magic_number, username
    if request.method == 'POST':
        username = request.form['username']
        cat1  = int(request.form['first'])
        cat2  = int(request.form['second'])
        cat3  = int(request.form['tres'])
        magic_number = ( (cat1 * cat2 * cat3) % 5 ) +1
        return redirect(url_for('myProfile'))
    return render_template("sign_up.html")

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

#* Seleccion de visualizacion asc o desc
@app.route('/profile',methods = ['GEt','POST'])
def myProfile():
    global orden
    print('numero', magic_number)
    g.username = username
    if request.method == 'POST':
        orden = request.form['orden']
        return redirect(url_for('recomendation'))
    return render_template('profile.html')

#* 10 recomendaciones
@app.route("/recomendation")
def recomendation():  
    df = pd.read_csv('/src/movies/entrypoints/movie_results.csv')
    movie = df[df['preference_key'] == magic_number]
    if orden == 1:
        movie = movie.head(10)
    else:
        movie = movie.tail(10)
    return(movie.to_html(), 200)







    