# backend/app/routes.py
from flask import Blueprint, jsonify

bp = Blueprint("api", __name__)

@bp.route("/")
def index():
    return jsonify(message="Welcome to the CMS API!")
