from flask import *
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.extensions import db

# 註冊login_bp
login_bp = Blueprint('login', __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login_or_register():
    if request.method == "POST":
        
        # if login request call login function
        if "login" in request.form:
            return login(request.form)
        # if register request call register function
        elif "register" in request.form:
            return register(request.form)
    
    # render login page  
    return render_template("login.html")

def login(form):
    pass

def register(form):
    # check wheather user exist?
    try:
        if form["sign-up-password"] == form["sign-up-confirm-password"]:
            # create user
            user = User(
                username=form["sign-up-username"],
                password=form["sign-up-password"]
            )
            db.session.add(user)
            db.session.commit()
            
            return redirect(url_for("login.login_or_register"))
        
    except IntegrityError as e:
        # catch IntegrityError error
        db.session.rollback()  # roll back
        # 可以根據需要自定義錯誤消息
        flash("Username already exists. Please choose another one.", "error")
        
        return redirect(url_for("login.login_or_register"))
    # check confirm password == password
    