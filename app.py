from flask import Flask, render_template

app = Flask(__name__)

entradas = [{

    'titulo': 'Primeiro Post do Blog',
    'texto': 'aqui vem o texto...'
},
{
    'titulo': 'segundo Post do Blog',
    'texto': 'outro texto do Blog'
}]


@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html",entradas=entradas)
