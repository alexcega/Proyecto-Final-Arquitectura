from crypt import methods
from distutils.log import debug
from xml.etree.ElementTree import tostring
# from tkinter.tix import Select
from flask import Flask, request, render_template, redirect, url_for
from movies import models
from movie_fetcher import session
import pandas as pd




app = Flask(__name__)
models.start_mappers()

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
    html = """<style>
@import "https://fonts.googleapis.com/css?family=Montserrat:300,400,700";
.rwd-table {
  margin: 1em 0;
  min-width: 300px;
}
.rwd-table tr {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #ddd;
}
.rwd-table th {
  display: none;
}
.rwd-table td {
  display: block;
}
.rwd-table td:first-child {
  padding-top: .5em;
}
.rwd-table td:last-child {
  padding-bottom: .5em;
}
.rwd-table td:before {
  content: attr(data-th) ": ";
  font-weight: bold;
  width: 6.5em;
  display: inline-block;
}
@media (min-width: 480px) {
  .rwd-table td:before {
    display: none;
  }
}
.rwd-table th, .rwd-table td {
  text-align: left;
}
@media (min-width: 480px) {
  .rwd-table th, .rwd-table td {
    display: table-cell;
    padding: .25em .5em;
  }
  .rwd-table th:first-child, .rwd-table td:first-child {
    padding-left: 0;
  }
  .rwd-table th:last-child, .rwd-table td:last-child {
    padding-right: 0;
  }
}
 
 
h1 {
  font-weight: normal;
  letter-spacing: -1px;
  color: #34495E;
}
 
.rwd-table {
  background: #34495E;
  color: #fff;
  border-radius: .4em;
  overflow: hidden;
}
.rwd-table tr {
  border-color: #46637f;
}
.rwd-table th, .rwd-table td {
  margin: .5em 1em;
}
@media (min-width: 480px) {
  .rwd-table th, .rwd-table td {
    padding: 1em !important;
  }
}
.rwd-table th, .rwd-table td:before {
  color: #dd5;
}
</style>
<script>
  window.console = window.console || function(t) {};
</script>
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>"""
    
    df = pd.read_csv('/src/movies/entrypoints/movie_results.csv')
    df=  df.head(10)
    # df.to_html('/templates/recomend.html')
    # with open('/templates/recomend.html', 'w') as file:
    #     file = file.read()
    # with open('/templates/recomend.html') as file_to_write:
    #     file_to_write.write(html+file)
    # os.startfile("/templates/recomend.html")
    # return render_template('recomend.html')
    return(df.to_html(), 200)







    