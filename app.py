from flask import Flask, request, jsonify

app = Flask(__name__)

# rota inicial só pra teste
@app.route("/")
def home():
    return "Servidor Flask no Render rodando!"

# rota para gerar key
@app.route("/gen")
def gen():
    return jsonify({"key": "ABC-123-XYZ"})

# rota para verificar key
@app.route("/verify")
def verify():
    key = request.args.get("key")
    if key == "ABC-123-XYZ":
        return jsonify({"valid": True})
    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
