from flask import Flask, jsonify
from bson import json_util
import pymongo
import os

mongodb_uri = os.environ['MONGODB_URI']

client = pymongo.MongoClient(mongodb_uri)
database = client["ccb"]
collection = database["igrejas"]

app = Flask(__name__)

@app.route("/api/igrejas")
def get_igrejas():
    try:
        # Utilize json_util para serializar o ObjectId para JSON
        igrejas = list(collection.find({}, {"_id": 0}))
        return jsonify({"igrejas": json_util.dumps(igrejas)})
    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)