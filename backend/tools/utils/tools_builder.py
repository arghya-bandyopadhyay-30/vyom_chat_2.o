import importlib

from utils.string_constants import TOOL_ERROR, URL, PACKAGE, NAME


def module(package: str):
    return importlib.import_module(package)

def tools_builder(tool: dict):
    if PACKAGE not in tool:
        raise ValueError(TOOL_ERROR.format(config_key=PACKAGE))
    if NAME not in tool:
        raise ValueError(TOOL_ERROR.format(config_key=NAME))
    if URL not in tool:
        raise ValueError(TOOL_ERROR.format(config_key=URL))

    return getattr(module(tool[PACKAGE]), tool[NAME])(tool[URL])
