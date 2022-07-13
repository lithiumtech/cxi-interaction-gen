from fastapi import APIRouter

router = APIRouter(
    prefix="/cdqa"
)


@router.get("/healthcheck",
    status_code=200
)
async def healthcheck(): 
    return{"message":"cdqa is alive"}