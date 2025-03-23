from dotenv import load_dotenv

from utils.string_constants import PIPELINE, CONFIG_ERROR
from utils.load_yaml import load_yaml
from pipeline.models.pipeline_config import PipelineConfig


class PipelineConfigService:
    def __init__(self, config_path: str):
        load_dotenv()
        self.config = load_yaml(config_path)

    def get_config(self):
        if PIPELINE not in self.config:
            raise ValueError(CONFIG_ERROR.format(config_key=PIPELINE))

        pipeline = PipelineConfig.from_dict(
            self.config[PIPELINE]
        )

        return pipeline
