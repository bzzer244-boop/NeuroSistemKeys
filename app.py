from flask import Flask, request
import random
import string
import os

app = Flask(__name__)

# Rota para gerar key
@app.route("/gen", methods=["GET"])
def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    return {"key": key}

# Rota para verificar key (agora é /validate)
@app.route("/validate", methods=["GET"])
def validate_key():
    key = request.args.get("key")
    if key and len(key) == 30:
        return {"valid": True}
    return {"valid": False}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render usa variável de ambiente
    app.run(host="0.0.0.0", port=port)
