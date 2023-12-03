from fastapi import APIRouter

router = APIRouter(
    prefix="/sum",
    tags=["sum"],
    responses={404: {"message": "Not found"}}
)

@router.get("/")
async def sum_page():
    return {"result": "Hello sum"}

@router.get("/{x}/{y}")
async def sum_num(x: int, y: int):
    return {"result": x + y}