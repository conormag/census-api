from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.config import app_configs, settings
from src.census.router import router as census_router


app = FastAPI(**app_configs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)

app.include_router(census_router, tags=["census"])

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> 'dict[str, str]':
    return {"status": "ok!"}

