from fastapi import APIRouter, Depends

from fps.hooks import register_router

from emscripten_forge_server.mamba_api import (
    install as mamba_install
)
from emscripten_forge_server.config import get_config

r = APIRouter()

CHANNELS = ['/home/martin/micromamba/envs/xeus-python/conda-bld/', 'conda-forge']
# CHANNELS = ['emscipten-forge', 'conda-forge']


@r.get("/install")
async def install(
        env: str = "",
        specs: str = "",
        config=Depends(get_config)
        ):
    try:
        mamba_install(env, specs.split(","), CHANNELS, 'emscripten-32')
        return dict(msg="success", config=config)
    except RuntimeError as e:
        return dict(msg="error", message=str(e), config=config)


router = register_router(r)
