from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Use Base as init Model
class Base(DeclarativeBase):
  	pass

db = SQLAlchemy(model_class=Base)