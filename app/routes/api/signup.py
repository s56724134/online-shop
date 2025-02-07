from flask import *
from app.models.user import User
from app.extensions import db

api_signup_bp = Blueprint("signup", __name__)


@api_signup_bp.route("/signup", method=["GET", "POST"])
def signup():
    if request.method == "POST":
        
        try:
            # check wheather user exist?
            if request.form["sign-up-password"] == request.form["sign-up-confirm-password"]:
                # create user
                user = User(
                    username=request.form["sign-up-username"],
                    password=request.form["sign-up-password"]
                )
                db.session.add(user)
                db.session.commit()
                # pop sucess text
                # redirect to loginpage
                return redirect(url_for("login.login_or_register"))
            
        except IntegrityError as e:
            # catch IntegrityError error
            db.session.rollback()  # roll back
            # 可以根據需要自定義錯誤消息
            flash("Username already exists. Please choose another one.", "error")
            
            return jasonify({"false":False})