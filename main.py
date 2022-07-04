from flask import Flask, jsonify, render_template
from random import randint

app = Flask(__name__) #Padrão

@app.route("/")
def inicio():
  return render_template("index.html")


@app.route("/<escolha>")
def calcula_signo(escolha):
  resultado = []
  quantidade = int(escolha[0 : escolha.index("d")])
  lados = int(escolha[escolha.index("d")+1 : ])

  for i in range(quantidade):
    resultado.append(randint(1, lados))

  total = sum(resultado)
  return jsonify({"quant":resultado, "total":total})

app.run(host="0.0.0.0")