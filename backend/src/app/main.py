from importlib.metadata import version

from fastapi import FastAPI

from app.api.routes.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(title="DevForge API", version=version("app"))
    app.include_router(health_router)
    return app


app = create_app()
