from flask import Flask, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os


mongodb_uri = os.getenv("MONGODB_URI")

client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

database = client["ccb"]
collection = database["igrejas"]

def create_app():
    app = Flask(__name__)

    @app.route("/api/igrejas")
    def get_igrejas():
        try:
            igrejas = list(collection.find({}, {"_id": 0}))
            return jsonify({"igrejas": igrejas})
        except Exception as e:
            return jsonify({"erro": str(e)})

    return app

app = create_app()