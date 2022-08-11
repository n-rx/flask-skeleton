import json
from build import db_status
from flask import Blueprint, jsonify, request
from utils.errors import raise_400, raise_not_found, raise_with_error
from IAPI.api.Models.api import Test

test_api = Blueprint("test_api", __name__)


@test_api.route("/api/test_api", methods=["GET"])
def test_get():
    return jsonify({"success": True, "msg": "Awesome"})


@test_api.route("/api/data", methods=["POST"])
def create_data():
    if db_status:
        if not request.data:
            return raise_with_error("Please provide request body")
        data_dict = json.loads(request.data.decode("utf-8"))
        data = data_dict.get("data")
        test = Test.create(data=data)
        return jsonify({"success": True, "data": Test.to_dict(test)})
    else:
        return jsonify({"success": False, "data": "Offline data"})


@test_api.route("/api/data", methods=["GET"])
def get_data():
    if db_status:
        test = Test.get_all()
        data = Test.to_dict_multy(test)
    else:
        data = "Data"
    return jsonify({
        "success": True,
        "Data": data
    })
