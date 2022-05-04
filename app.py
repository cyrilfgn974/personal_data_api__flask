import sqlite3
import pandas as pd
import json
import wget
from flask import Flask
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)


def getProjectDatabase():
    url = "http://sqlite.gnmc3466.odns.fr/projects.sqlite"
    if os.path.exists("data/cfiguin_portfolio/projects.sqlite"):
        os.remove("data/cfiguin_portfolio/projects.sqlite")
    response = wget.download(url, "./data/cfiguin_portfolio/projects.sqlite")
    sqlCon = sqlite3.connect("./data/cfiguin_portfolio/projects.sqlite")
    df = pd.read_sql_query("SELECT * from project", sqlCon)
    dfj = df.to_json(orient='records')
    return dfj

@app.route('/')
def welcome():
    return "Bienvenue sur Data_API_CFIGUIN"


# Cfiguin_Portfolio
@app.route('/api/cfiguin_portfolio/getAllProjects', methods=["GET"])
def cfiguin_portfolio__allProjects():
    # file = open('./data/cfiguin_portfolio/projects.json')
    # data = json.load(file)
    # file.close()
    # print(data)
    return getProjectDatabase()
