"""The main running app for the project."""
from fastapi import FastAPI

app = FastAPI(
    title="Instagram Clone",
    description="A simple instagram clone"
)


@app.get("/")
async def root() -> dict[str, str]:
    """The root route for the app."""
    return {"message": "Hello World"}
