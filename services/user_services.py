"""The user services file for the application"""
from fastapi import Depends
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.user_schema import UserBase, UserDisplay


async def create_user_service(
    _user: UserBase,
    _db: Session = Depends(get_db)
) -> UserDisplay:
    """The function to add a use to the database

    Args:
        _user (UserBase): The user data
        _db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        UserDisplay: _description_
    """
    await _db.Add(_user)
    await _db.commit()
    await _db.refresh(_user)

    return await _user
