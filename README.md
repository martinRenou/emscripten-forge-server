# This is still under development and not ready to be used

# emscripten-forge-server

Mamba server exposing endpoint for creating environments, install and access packages from the emscripten-forge channel.

## Installation

You will first need to [install micromamba](https://github.com/mamba-org/mamba#micromamba) and create a micromamba environment for "host" environment (the environment containing subenvironments for emscripten-32, created dynamically using the proper server endpoints):

```bash
micromamba create -n emscripten-forge-server -c conda-forge mamba pip python=3.10 fps emscripten emboa
micromamba activate emscripten-forge-server
```

Install emsdk:
```bash
git clone https://github.com/emscripten-core/emsdk

pushd emsdk

./emsdk install 3.1.2
./emsdk activate 3.1.2

export FILE_PACKAGER=$(pwd)/upstream/emscripten/tools/file_packager.py

popd
```

Install emboa:
```bash
pip install git+https://github.com/emscripten-forge/emboa
```

Then install the server:

```
pip install -e .
```

Run it:

```
emscripten_forge_server
```

Making package install request in the "custom" env:

```
http://127.0.0.1:8000/install?env=custom&specs=xeus-python,matplotlib
```

Making a pack request to pack everything with emscripten:

```
http://127.0.0.1:8000/pack?env=custom
```
