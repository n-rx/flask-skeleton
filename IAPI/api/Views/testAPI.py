import json

from flask import Blueprint, jsonify, request
from utils.errors import raise_400, raise_not_found, raise_with_error
from IAPI.api.Models.api import Test

test_api = Blueprint("test_api", __name__)


@test_api.route("/api/test_api", methods=["GET"])
def test_get():
    return jsonify({"success": True, "msg": "Awesome"})


@test_api.route("/api/data", methods=["POST"])
def create_data():
    if not request.data:
        return raise_with_error("Please provide request body")
    data_dict = json.loads(request.data.decode("utf-8"))
    data = data_dict.get("data")
    test = Test.create(data=data)
    return jsonify({"success": True, "data": Test.to_dict(test)})


@test_api.route("/api/data", methods=["GET"])
def get_data():
    test = Test.get_all()
    return jsonify({
        "success": True,
        "Data": Test.to_dict_multy(test)
    })
