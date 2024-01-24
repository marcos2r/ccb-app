from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import os

mongodb_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongodb_uri)

try:
    client.admin.command('ping')
except Exception as e:
    print(f"Erro ao se conectar ao MongoDB: {e}")

db = client["ccb"]
collection = db["igrejas"]

def create_app():
    
    app = Flask(__name__)

    CORS(app)

    app.config['JSON_AS_ASCII'] = False
    
    @app.route("/igrejas")
    def get_igrejas():
        try:
            igrejas = list(collection.find({}, {"_id": 0}))
            return jsonify({"igrejas": igrejas})
        except Exception as e:
            return jsonify({"erro": str(e)})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))