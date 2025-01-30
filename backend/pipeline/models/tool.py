from abc import ABC
from dataclasses import dataclass

from utils.string_constants import PACKAGE, TOOL_ERROR, NAME, URL


@dataclass
class Tool(ABC):
    package: str
    name: str
    url: str

    @classmethod
    def from_dict(cls, tool: dict):
        if PACKAGE not in tool:
            raise ValueError(TOOL_ERROR.format(config_key=PACKAGE))
        if NAME not in tool:
            raise ValueError(TOOL_ERROR.format(config_key=NAME))
        if URL not in tool:
            raise ValueError(TOOL_ERROR.format(config_key=URL))

        return cls(
            package=tool[PACKAGE],
            name=tool[NAME],
            url=tool[URL]
        )

