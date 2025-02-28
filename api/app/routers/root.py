from fastapi import APIRouter
from fastapi.responses import RedirectResponse


router = APIRouter()


@router.get("/")
def documentacao():
    return RedirectResponse(url="/docs")