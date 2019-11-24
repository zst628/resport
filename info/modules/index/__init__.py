from flask import Blueprint

index_blu = Blueprint("index", __name__)
register_blu = Blueprint("register", __name__)
login_blu = Blueprint("login", __name__)


from . import view