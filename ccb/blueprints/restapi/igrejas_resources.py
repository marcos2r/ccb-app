from flask import abort, json, Response
from flask_restful import Resource
from bson import json_util
import json

from ccb.services.igreja_service import IgrejaService


class IgrejasResource(Resource):
    def __init__(self):
        self.service = IgrejaService()

    def get(self):
        documents = self.service.get_all() or abort(204)
        response_data = json.dumps(documents, default=json_util.default)
        return Response(response_data, content_type='application/json', status=200)
