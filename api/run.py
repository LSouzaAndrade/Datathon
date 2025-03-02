from uvicorn import run
from app.api import app


if __name__ == "__main__":
    run(
        "run:app",
        host="0.0.0.0",
        port=8000,
        workers=1,
    )