import pathlib
import sys
import tempfile
from uuid import uuid4

from fastapi import APIRouter, Depends

from fps.hooks import register_router

from emboa.file_packager import pack_python_core

# from mamba.api import install as mamba_install
from emscripten_forge_server.mamba_api import (
    install as mamba_install
)
from emscripten_forge_server.config import get_config

r = APIRouter()

CHANNELS = ['/home/martin/micromamba/envs/xeus-python/conda-bld/', 'conda-forge']
# CHANNELS = ['emscipten-forge', 'conda-forge']

ENVS_DIR = pathlib.Path(tempfile.mkdtemp())


@r.get("/install")
async def install(
        env: str = "",
        specs: str = "",
        config=Depends(get_config)
        ):
    try:
        mamba_install(
            env,
            specs.split(","),
            CHANNELS,
            target_platform='emscripten-32',
            base_prefix=ENVS_DIR
        )
        return dict(msg="success", config=config)
    except RuntimeError as e:
        return dict(msg="error", message=str(e), config=config)


@r.get("/pack_python")
async def pack_python(
        env: str = "",
        config=Depends(get_config)
        ):
    try:
        outname = uuid4()

        pack_python_core(
            ENVS_DIR / env,
            outname,
            # TODO Use Python version from the given env
            f"{sys.version_info.major}.{sys.version_info.minor}",
            "globalThis.Module"
        )

        with open(f"{outname}.js", "r") as f:
            js = f.read()

        with open(f"{outname}.data", "r") as f:
            data = f.read()

        return dict(
            msg="success",
            js=js,
            data=data,
            config=config
        )
    except RuntimeError as e:
        return dict(msg="error", message=str(e), config=config)


router = register_router(r)
