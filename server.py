from flask import Flask, request
from flask import current_app
from flasgger import Swagger

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/myflaskapp')
def myflaskapp():
    return 'Hello, from My flask app!'

@app.route('/appwithparams')
def appwithparams():
    return 'Hello, from My flask app!'

