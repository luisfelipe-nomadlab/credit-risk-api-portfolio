from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api.core.config import settings
from app.api.utils.logger import logger
from app.api.v1 import healt, fraud  # verifique se o arquivo realmente se chama 'healt.py'

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# Middleware de CORS (sempre adicione antes das rotas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware para log de requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info({"event": "request_start", "path": request.url.path})
    response = await call_next(request)
    logger.info({"event": "request_end", "path": request.url.path, "status_code": response.status_code})
    return response

# Rotas raiz
@app.get("/")
def root():
    return {"message": "API de Detecção de Fraude está rodando!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Inclusão de routers
app.include_router(healt.router, prefix=settings.API_V1_STR)
app.include_router(fraud.router, prefix=settings.API_V1_STR)

# Evento de startup
@app.on_event("startup")
async def startup_event():
    logger.info({"event": "startup", "message": "API iniciada"})

# Evento de shutdown
@app.on_event("shutdown")
async def shutdown_event():
    logger.info({"event": "shutdown", "message": "API finalizada"})
