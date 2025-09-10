from fastapi import APIRouter
from app.api.core.config import settings
from app.api.utils.logger import logger

router = APIRouter()

@router.get("/healt")
async def healt_check():

    redis_status = "checagem ok"
    logger.info({"event":"healt_check", "status": "Ok"})

    return{
        "app":settings.APP_NAME,
        "status":"ok",
        "debug":settings.DEBUG,
        "redis":redis_status
    }