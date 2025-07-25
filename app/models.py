from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    operand1 = Column(Float)
    operand2 = Column(Float)
    result = Column(Float)
