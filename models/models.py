"""The models for the application"""
from sqlalchemy import Column, Integer, String

from database.db import Base


class DbUser(Base):
    """The model for the users of the application.

    Args:
        Base (DbObject): Some database object
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
