from flask import Blueprint, jsonify

test_api = Blueprint("test_api", __name__)


@test_api.route("/api/v1.0/test_api", methods=["GET"])
def test_get():
    return jsonify({"success": True, "msg": "Awesome"})
