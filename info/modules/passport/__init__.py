from . import views
from flask import Blueprint
passport_blu = Blueprint("passport", __name__, url_prefix='/passport')