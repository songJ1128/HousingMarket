from flask import Blueprint, jsonify

housing_blueprint = Blueprint('housing', __name__)

@housing_blueprint.route('/list', methods=['GET'])
def list_houses():
    return jsonify({"message": "List of houses"})
