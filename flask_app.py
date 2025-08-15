from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>Hello World!</h1><h2>Disciplina PTBDSWS</h2>'

@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route('/contextorequisicao')
def contextoRequisicao():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/codigostatusdiferente')
def codigosStatus():
    return 'Bad request', 400

@app.route('/objetoresposta')
def objetoresposta():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    
@app.route('/redirecionamento')
def redirecionamento():
    return redirect('https://ptb.ifsp.edu.br/')

@app.route('/abortar')
def abortar():
    abort(404)