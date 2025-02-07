from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from  app.extensions import db

class User(db.Model):
    __tablename__ = 'users'  # 資料表名稱
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    photo_path = mapped_column(String(200), nullable=True)




