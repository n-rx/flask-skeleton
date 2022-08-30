from flask import jsonify


def raise_not_found(obj):
	return jsonify({"error": "{} not found".format(obj.__name__)}), 404


def raise_400():
	return jsonify({"error": "Bad request"}), 400


def raise_with_error(error):
	return jsonify({"message": error}), 400
