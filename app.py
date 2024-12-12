from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/score', methods=['POST'])
def get_score():
    # Récupère le texte envoyé dans la requête
    data = request.get_json()
    text = data.get('text', '')

    # Génère un score aléatoire entre 0 et 100
    score = random.randint(0, 100)

    # Retourne le score sous forme de réponse JSON
    return jsonify({'text': text, 'score': score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
