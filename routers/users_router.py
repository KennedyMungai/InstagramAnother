"""The users router"""
from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserBase, UserDisplay
from services.user_services import create_user_service


users_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@users_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserDisplay
)
async def create_user_endpoint(user: UserBase) -> UserDisplay:
    """The endpoint to create a user in the database

    Args:
        user (UserBase): The data used to create the user

    Raises:
        HTTPException: A 500 is raised if there is any problem with the creation of the user

    Returns:
        UserDisplay: The user created in the database
    """
    try:
        return await create_user_service(user)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error creating user"
        )
