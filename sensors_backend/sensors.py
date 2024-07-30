from flask import Flask, request, Blueprint
import json

bp = Blueprint("sensors", __name__, url_prefix='/sensors')

@bp.route("/<string:name>", methods=["POST"])
def receive_data(name):
    response = dict()
    if name == 'temphumid':
        # data = request.get_data(as_text=True)
        data = request.get_json()
        response["endpoint"] = name

    response["status"] = "success"
    response["action"] = "Data added to database"
    return response
