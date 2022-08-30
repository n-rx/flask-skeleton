import json
from config import Config
from flask import Blueprint, jsonify, request
from utils.errors import raise_400, raise_not_found, raise_with_error
from API.test_api.Models.api import Test

test_api = Blueprint("test_api", __name__)


@test_api.route("/api/test_api", methods=["GET"])
def test_get():
    return jsonify({"msg": "Awesome"}), 200


@test_api.route("/api/data", methods=["POST"])
def create_data():
    print(Config.DB_STATUS)
    if Config.DB_STATUS:
        if not request.data:
            return raise_with_error("Please provide request body")
        data_dict = json.loads(request.data.decode("utf-8"))
        data = data_dict.get("data")
        test = Test.create(data=data)
        return jsonify({"data": Test.to_dict(test)}), 200
    else:
        return jsonify({"data": "Cannot create new data without DB connection"}), 200


@test_api.route("/api/data", methods=["GET"])
def get_data():
    if Config.DB_STATUS:
        test = Test.get_all()
        data = Test.to_dict_multy(test)
    else:
        data = "Data obtained without a database"

    return jsonify({"Data": data}), 200
