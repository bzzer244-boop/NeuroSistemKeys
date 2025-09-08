import random
import string
from flask import Flask, request, jsonify

app = Flask(__name__)

# banco de dados simples em memória (apaga ao reiniciar o server)
keys = {}

# função para gerar key aleatória de 30 caracteres
def gerar_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))

# rota inicial
@app.route("/")
def home():
    return "Servidor de Keys rodando no Render!"

# rota para gerar nova key
@app.route("/gen")
def gen():
    key = gerar_key()
    keys[key] = True  # salva como válida
    return jsonify({"key": key})

# rota para verificar se a key é válida
@app.route("/verify")
def verify():
    key = request.args.get("key")
    if key in keys and keys[key]:
        return jsonify({"valid": True})
    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
