from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/myflaskapp')
def myflaskapp():
    return 'Hello, from My flask app!'

