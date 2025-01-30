import importlib

from pipeline.models.tool import Tool


def module(package: str):
    return importlib.import_module(package)

def tools_builder(tool: dict):
    tool = Tool.from_dict(tool)
    return getattr(module(tool.package), tool.name)(tool.url)
