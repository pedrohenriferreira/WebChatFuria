from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

jogadores = [
    {
        'name': 'Gabriel Toledo',
        'nickname': 'Fallen',
        'position': 'AWper / In-game Leader',
        'country': 'Brasil' 
    },
    {
        'name': 'Yuri Santos',
        'nickname': 'yuurih',
        'position': 'Rifler',
        'country': 'Brasil'
    },
    {
        'name': 'Mareks Gaļinskis',
        'nickname': 'YEKINDAR',
        'position': 'Entry Fragger',
        'country': 'Letônia'
    },
    {
        'name': 'Kaike Cerato',
        'nickname': 'KSCERATO',
        'position': 'Lurker',
        'country': 'Brasil'
    },
    {
        'name': 'Danil Golubenko',
        'nickname': 'molodoy',
        'position': 'AWper',
        'country': 'Cazaquistão'
    } 
],

conquistas = [
    {
        'title': 'Elisa Masters Espoo 2023',
    },
    {
        'title': 'Elisa Invitational Summer 2021',
    },
    {
        'title': 'ESL Pro League Season 12: North America',
    },
    {
        'title': 'DreamHack Masters Spring 2020: North America',
    },
    {
        'title': 'Arctic Invitational 2019',
    }
]



@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_message = request.json.get('message', '').lower()
        
        if not user_message:
            return jsonify({"response": "Por favor, envie uma mensagem válida."}), 400

        jogador_encontrado = encontrar_jogador(user_message, jogadores)
        if jogador_encontrado:
            response = (
                f"{jogador_encontrado['name']} joga como {jogador_encontrado['position']} "
                f"e é do {jogador_encontrado['country']}."
            )
        elif "jogadores" in user_message:
            response = "Jogadores atuais da FURIA:\n"
            for jogador in jogadores[0]:
                response += f"- {jogador['name']} | Posição: {jogador['position']} | País: {jogador['country']}\n"
        elif "coach" in user_message or "treinador" in user_message:
            response = "O coach da FURIA é o Sid 'sidde' Macedo."
        elif "história" in user_message or "historia" in user_message:
            response = "A FURIA foi fundada em 2017 e logo ganhou notoriedade no cenário de Counter-Strike nacional"
        elif "ranking" in user_message:
            response = "A FURIA atualmente está na 17° colocação segundo a HTLV."
        elif "conquistas" in user_message: 
            conquistas_furia = [campeonatos['title'] for campeonatos in conquistas]
            response = f"As conquistas da Furia são: {', '.join(conquistas_furia)}"
        else:
            response = "Desculpe, não entendi sua pergunta sobre a FURIA."

        return jsonify({"response": response})

    except Exception as e:
        print(f"Erro no servidor: {str(e)}")
        return jsonify({"response": "Ocorreu um erro interno no servidor."}), 500

    
    
def encontrar_jogador(mensagem, jogadores):
    for nome_jogador in jogadores[0]:  # ou só "jogadores" se corrigir a vírgula
        nome_lower = nome_jogador['nickname'].lower()
        apelido = nome_lower.split('"')[1] if '"' in nome_lower else ""
        if apelido and apelido in mensagem:
            return nome_jogador
        elif nome_jogador['nickname'].lower() in mensagem:
            return nome_jogador
    return None


app.run(port=5000, host='localhost', debug=True)