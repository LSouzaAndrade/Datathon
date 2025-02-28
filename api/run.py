from uvicorn import run
from app.api import app


if __name__ == "__main__":
    run(
        "run:app",
        host="localhost",
        port=8000,
        workers=1,
    )