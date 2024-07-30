from flask import request, Blueprint, abort
import json

bp = Blueprint("sensors", __name__, url_prefix='/sensors')

@bp.route("/<string:name>", methods=["POST"])
def receive_data(name):
    response = dict()
    if name == 'temphumid':
        data = request.get_json()
        response["endpoint"] = name
    elif name == 'vibration':
        data = request.get_json()
        response["endpoint"] = name
    elif name == 'geolocation':
        data = request.get_json()
        response['endpoint'] = name
    else:
        abort(400)

    response["status"] = "success"
    response["action"] = "Data added to database"
    return response
