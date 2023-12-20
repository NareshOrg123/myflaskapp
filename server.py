from flask import Flask, request
from flask import current_app
from flasgger import Swagger

app = Flask(__name__)

@app.route('/')
def hello():
    '''Function hello returns a string'''
    return 'Hello, World!'

@app.route('/myflaskapp')
def myflaskapp():
    '''Function myflaskapp returns a string'''
    return 'Hello, from My flask app!'

@app.route('/appwithparams')
def appwithparams():
    '''Function appwithparams returns a string'''
    return 'Hello, from My flask app!' + request.args.get('name')
