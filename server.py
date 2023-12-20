from flask import Flask, request

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
