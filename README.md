# emscripten-forge-server

Mamba server exposing endpoint for creating environments, install and access packages from the emscripten-forge channel.

## Installation

```
pip install -e .
```

Run it

```
emscripten_forge_server
```

Making a mamba install request:

```
http://127.0.0.1:8000/install?packages=ipycanvas,jupyterlab&channels=conda-forge
```
