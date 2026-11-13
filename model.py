from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(100),unique=True,index=True,nullable=False)
    email = Column(String(255),unique=True,index=True,nullable=False)
    mobilenumber = Column(String(20),nullable=False)
    hased_password = Column(String(255),nullable=False)

    todos = relationship('Todo',back_populates='owner',cascade='all,delete-orphan')

class Todo(Base):
    __tablename__ = 'todo'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255),nullable=False)
    complete = Column(Boolean,default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User",back_populates='todos')

