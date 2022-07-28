from flask import jsonify


def raise_not_found(obj):
	return jsonify({"success": False, "error": "{} not found".format(obj.__name__)}), 404


def raise_400():
	return jsonify({"success": False, "error": "Bad request"}), 400


def raise_with_error(error):
	return jsonify({"success": False, "message": error}), 400
