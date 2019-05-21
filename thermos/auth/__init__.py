from flask import Blueprint

auth = Blueprint("auth", __name__)

from thermos.auth import views