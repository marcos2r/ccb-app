import json
from flask import Flask, Response
from flask_cors import CORS

# Dados no formato JSON
dados = [
    {
        "cod": "BR 10-0054",
        "igreja": "VILA PLANALTO (Central)",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "19:30",
        "quinta": "--",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0563",
        "igreja": "ALDEIA BORORÓ",
        "domingo": "18:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0577",
        "igreja": "ALDEIA BORORÓ II",
        "domingo": "---",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0322",
        "igreja": "ALDEIA JAGUAPIRU",
        "domingo": "09:30",
        "segunda": "---",
        "terca": "---",
        "quarta": "19:30",
        "quinta": "---",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0467",
        "igreja": "ALTOS DO INDAIÁ",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "---",
        "sexta": "19:30",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0538",
        "igreja": "DISTRITO DE ITAHUM",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0244",
        "igreja": "DISTRITO INDÁPOLIS",
        "domingo": "---",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "19:30",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0258",
        "igreja": "DISTRITO MACAÚBA",
        "domingo": "---",
        "segunda": "---",
        "terca": "---",
        "quarta": "19:30",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0055",
        "igreja": "DISTRITO PANAMBI",
        "domingo": "---",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0062",
        "igreja": "DISTRITO VILA VARGAS",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "19:30",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0149",
        "igreja": "JARDIM ÁGUA BOA",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "19:30",
        "quarta": "---",
        "quinta": "---",
        "sexta": "19:30",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0312",
        "igreja": "JARDIM CARISMA",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "19:30",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0060",
        "igreja": "JARDIM CLÍMAX",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "19:30",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0341",
        "igreja": "JARDIM COLIBRI",
        "domingo": "---",
        "segunda": "---",
        "terca": "19:30",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0205",
        "igreja": "JARDIM DOS ESTADOS",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "---",
        "sexta": "19:30",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0490",
        "igreja": "JARDIM GUAICURUS",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "19:30",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0335",
        "igreja": "JARDIM LARANJA DOCE",
        "domingo": "---",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:00"
    },
    {
        "cod": "BR 10-0320",
        "igreja": "JARDIM MÁRCIA",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "19:30",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0382",
        "igreja": "JARDIM NOVA ESPERANÇA",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "19:30",
        "quinta": "---",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0319",
        "igreja": "JARDIM NOVO HORIZONTE",
        "domingo": "---",
        "segunda": "---",
        "terca": "19:30",
        "quarta": "---",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0488",
        "igreja": "JARDIM SYRIA RASSELEN",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "19:30",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0227",
        "igreja": "JÓQUEI CLUB",
        "domingo": "---",
        "segunda": "---",
        "terca": "---",
        "quarta": "19:30",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0064",
        "igreja": "PARQUE DAS NAÇÕES II",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "---",
        "sexta": "19:30",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0243",
        "igreja": "PARQUE NOVA DOURADOS",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "19:30",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0242",
        "igreja": "PARQUE RESIDENCIAL MORADA DO SALTO",
        "domingo": "---",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "19:30",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0513",
        "igreja": "RESIDENCIAL OLIVEIRA",
        "domingo": "---",
        "segunda": "---",
        "terca": "---",
        "quarta": "19:30",
        "quinta": "---",
        "sexta": "---",
        "sabado": "19:30"
    },
    {
        "cod": "BR 10-0515",
        "igreja": "SITIOCAS CAMPINA VERDE",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "19:30",
        "quinta": "---",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0578",
        "igreja": "SITIOCAS CAMPO BELO III",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "19:30",
        "sexta": "---",
        "sabado": "---"
    },
    {
        "cod": "BR 10-0056",
        "igreja": "VILA SÃO FRANCISCO",
        "domingo": "19:00",
        "segunda": "---",
        "terca": "---",
        "quarta": "---",
        "quinta": "19:30",
        "sexta": "---",
        "sabado": "---"
    }
]

def obter_dados():
    return dados


def criar_app():
    app = Flask(__name__)
    CORS(app) # Habilita CORS para o aplicativo

    @app.route("/dados", methods=["GET"])
    def get_data():
        try:
            response_data = json.dumps(obter_dados())
            return Response(response_data, content_type="application/json", status=200)
        except Exception as e:
            error_message = {"error": str(e)}
            return Response(json.dumps(error_message), content_type="application/json", status=500)

    return app
