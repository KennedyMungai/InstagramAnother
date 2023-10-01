"""The schema file to communicate with the database"""
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """The base schema for the user data

    Args:
        BaseModel (Pydantic model): The base class for all schemas
    """
    username: str
    email: EmailStr
    password: str


class UserDisplay(BaseModel):
    """The schema being used to display data

    Args:
        BaseModel (Pydantic Model): The base model for all schemas
    """
    username: str
    email: EmailStr

    class Config:
        """The config for the model"""
        orm_mode = True
