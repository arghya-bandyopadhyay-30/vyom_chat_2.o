from dataclasses import dataclass

from pipeline.models.stage import Stage
from tools.ingestion_tool import IngestionTool
from tools.utils.tools_builder import tools_builder
from utils.string_constants import TYPE, TOOLS, STAGE_ERROR


@dataclass
class Ingestion(Stage):
    tools: list[IngestionTool]

    @classmethod
    def from_dict(cls, stage: dict):
        if TYPE not in stage:
            raise ValueError(STAGE_ERROR.format(config_key=TYPE))
        if TOOLS not in stage:
            raise ValueError(STAGE_ERROR.format(config_key=TOOLS))

        tools = [tools_builder(tool) for tool in stage[TOOLS]]

        return cls(
            stage_type=stage[TYPE],
            tools=tools
        )


    def run(self):
        for tool in self.tools:
            tool.run()
