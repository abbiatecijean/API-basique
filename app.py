from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
import flask_cors
import random

app = Flask(__name__)
CORS(app)  # Active les CORS pour toutes les routes

@app.route('/score', methods=['POST'])
def get_score():
    data = request.get_json()
    text = data.get('text', '')

    # Génère un score aléatoire entre 0 et 100
    score = random.randint(0, 100)

    return jsonify({'text': text, 'score': score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
