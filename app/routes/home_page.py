from flask import render_template
from flask import Blueprint

homepage_bp = Blueprint('homepage', __name__)


@homepage_bp.route("/")
def index():
    return render_template("index.html")