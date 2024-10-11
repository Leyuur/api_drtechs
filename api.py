from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def gerar_numero():
    data = {"message": "Eu sou universal"}
    return jsonify(data)


app.run(host='0.0.0.0')
