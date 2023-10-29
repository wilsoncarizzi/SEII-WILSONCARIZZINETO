from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=["GET,"POST"])
def index():
    variavel = "Game: Adivinhe o numero correto"
    return render_template("index.html", variavel=variavel)
    numero = 0
    palpite = int(request.form.get("name"))
    if numero == palpite:
        return '<h1>Resultado: Voce ganhou</h1>'
    else:
        return '<h1>Resultado: Voce perdeu</h1>'
        

@app.route('/sobre')
def error(nome):
    return 'Sobre'