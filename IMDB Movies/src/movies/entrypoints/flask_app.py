from distutils.log import debug
# from tkinter.tix import Select
from flask import Flask, request, render_template, redirect, url_for
from movies import models
from movie_fetcher import session
# import pandas as pd




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

@app.route("/post_user", methods=["POST"])
def post_user():
    user = models.User(request.form['user_id'], request.form['user_name'])
    session.add(user)
    session.commit()
    return redirect(url_for(fin))






    