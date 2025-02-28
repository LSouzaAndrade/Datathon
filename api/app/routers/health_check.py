from fastapi import APIRouter


router = APIRouter()


@router.get("/health-check")
def api_check():
    return {"message": "OK"}