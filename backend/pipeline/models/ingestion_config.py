from pipeline.models.ingestion_tool import IngestionTool
from pipeline.models.stage import Stage
from tools.utils.tools_builder import tools_builder
from utils.string_constants import TYPE, TOOLS, STAGE_ERROR


class Ingestion(Stage):
    tools: list[IngestionTool]

    @classmethod
    def from_dict(cls, stage: dict):
        if TYPE not in stage:
            raise ValueError(STAGE_ERROR.format(config_key=TYPE))
        if TOOLS not in stage:
            raise ValueError(STAGE_ERROR.format(config_key=TOOLS))

        tools = [tools_builder(tool) for tool in stage[TOOLS]]



    def run(self):
        pass