from flask import Flask, jsonify
from dotenv import load_dotenv
from bson import json_util
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

load_dotenv()

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
            # Utilize json_util para serializar o ObjectId para JSON
            igrejas = list(collection.find({}, {"_id": 0}))
            return jsonify({"igrejas": json_util.dumps(igrejas)})
        except Exception as e:
            return jsonify({"erro": str(e)})

    return app

app = create_app()