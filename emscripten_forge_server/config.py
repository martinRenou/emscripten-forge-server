from fps.config import PluginModel
from fps.config import get_config as fps_get_config
from fps.hooks import register_config, register_plugin_name


class EmsciptenServerConfig(PluginModel):
    pass

def get_config():
    return fps_get_config(EmsciptenServerConfig)


c = register_config(EmsciptenServerConfig)
n = register_plugin_name("emscripten_forge_server")
