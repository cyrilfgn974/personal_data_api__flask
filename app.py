import pandas as pd
import json

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return "Bievenue sur l'API CFIGUIN"


# Cfiguin_Portfolio
@app.route('/api/cfiguin_portfolio/getAllProjects', methods=["GET"])
def cfiguin_portfolio__allProjects():
    file = open('./data/cfiguin_portfolio/projects.json')
    data = json.load(file)
    file.close()
    print(data)
    return json.dumps(data)
