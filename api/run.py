from uvicorn import run
from app.api import app


if __name__ == "__main__":
    run(
        "run:app",
        host="localhost",
        port=80,
        workers=1,
    )