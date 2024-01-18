from flask import Flask, jsonify
from dotenv import load_dotenv
from bson import json_util
import pymongo
import os

load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")

client = pymongo.MongoClient(mongodb_uri)
database = client["ccb"]
collection = database["igrejas"]

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route("/api/igrejas")
def get_igrejas():
    try:
        # Utilize json_util para serializar o ObjectId para JSON
        igrejas = list(collection.find({}, {"_id": 0}))
        return jsonify({"igrejas": json_util.dumps(igrejas)})
    except Exception as e:
        return jsonify({"erro": str(e)})