import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

if settings.BACKEND_CORS_ORIGINGS:
    app.add_middleware(
        CORSMiddleware,
        allow_origings=[str(origin) for origin in settings.BACKEND_CORS_ORIGINGS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
