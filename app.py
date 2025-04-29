# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Algumas informações básicas sobre a FURIA CS
informacoes = {
    "nome_time": "FURIA Esports",
    "jogadores": ["Fallen", "yuurih", "YEKINDAR", "KSCERATO", "molodoy"],
    "coach": "sidde",
    "ranking": "Top 17 mundial (HLTV)",
    "historia": "A FURIA Esports foi fundada em 2017 e rapidamente se destacou no cenário de CS:GO."
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message').lower()

    if "jogadores" in user_message:
        response = f"Os jogadores atuais da FURIA são: {', '.join(informacoes['jogadores'])}."
    elif "coach" in user_message or "treinador" in user_message:
        response = f"O coach da FURIA é o {informacoes['coach']}."
    elif "história" in user_message or "historia" in user_message:
        response = informacoes['historia']
    elif "ranking" in user_message:
        response = f"A FURIA atualmente está no {informacoes['ranking']}."
    else:
        response = "Desculpe, não entendi sua pergunta sobre a FURIA."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
