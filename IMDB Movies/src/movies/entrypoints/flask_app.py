from flask import Flask, render_template, request
from movies import models
from movies import movie_fetcher
import pandas as pd
app = Flask(__name__)
models.start_mappers()


# @app.route("/hello", methods=["GET"])
# def hello_world():
#     return "Hello mundo!", 200


@app.route("/login")
def myLogin():
    return render_template("login.html")


@app.route("/recomendation")
def myRecomended():
    df = pd.read_csv('./movie_results.csv')
    ans = df.head()
    return "hola", 200

