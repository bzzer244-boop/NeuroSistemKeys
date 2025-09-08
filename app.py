from flask import Flask, request
import random
import string
import os

app = Flask(__name__)

# Banco de dados em memória (perde se reiniciar Render)
KEYS = {}  # { "keyGerada": "userId" }

# Rota para gerar key
@app.route("/gen", methods=["GET"])
def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    return {"key": key}

# Rota para validar key
@app.route("/validate", methods=["GET"])
def validate_key():
    key = request.args.get("key")
    user = request.args.get("user")  # userId do Roblox ou outro identificador

    if not key or not user:
        return {"valid": False, "error": "faltando parâmetros"}

    # Se a key nunca foi usada → ativar agora
    if key not in KEYS:
        KEYS[key] = user
        return {"valid": True, "msg": "primeiro uso, key vinculada"}

    # Se já estiver vinculada ao mesmo usuário → ainda é válida
    if KEYS[key] == user:
        return {"valid": True, "msg": "key já vinculada a você"}

    # Se já estiver vinculada a outro → inválida
    return {"valid": False, "msg": "key já usada em outro dispositivo"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
