from flask import Flask, request
from movies import models
from movies import movie_fetcher
app = Flask(__name__)
models.start_mappers()


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

movie_fetcher.main()

