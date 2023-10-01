"""The main running app for the project."""
from fastapi import FastAPI

from routers.users_router import users_router

app = FastAPI(
    title="Instagram Clone",
    description="A simple instagram clone"
)


@app.get(
    "/",
    name="Root",
    description="The root endpoint for the application",
    tags=["Root"]
)
async def root() -> dict[str, str]:
    """The root route for the app."""
    return {"message": "Hello World"}


app.include_router(users_router)
