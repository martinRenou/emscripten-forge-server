from fastapi import APIRouter, Depends

from fps.hooks import register_router

from emscripten_forge_server.mamba_api import (
    install as mamba_install
)
from emscripten_forge_server.config import get_config

r = APIRouter()


@r.get("/install")
async def install(
        packages: str = "",
        channels: str = "",
        config=Depends(get_config)
        ):
    logs = mamba_install(packages.split(","), channels.split(","))

    return dict(msg="installed", logs=logs, config=config)


router = register_router(r)
