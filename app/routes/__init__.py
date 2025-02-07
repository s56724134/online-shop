from flask import Blueprint
from .home_page import homepage_bp
from .login import login_bp


def register_routes(app):
    app.register_blueprint(homepage_bp)
    app.register_blueprint(login_bp)
    