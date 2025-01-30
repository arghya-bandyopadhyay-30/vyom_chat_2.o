from dataclasses import dataclass

from pipeline.models.database_config import DatabaseConfig
from pipeline.models.ingestion_config import Ingestion
from pipeline.models.stage import Stage
from utils.string_constants import DATABASE_CONFIG, CONFIG_ERROR, STAGES, TYPE, INGESTION, COMPREHENSION

@dataclass
class PipelineConfig:
    database: DatabaseConfig
    stages: list[Stage]

    @classmethod
    def from_dict(cls, config: dict):
        if DATABASE_CONFIG not in config:
            raise ValueError(CONFIG_ERROR.format(config_key=DATABASE_CONFIG))
        if STAGES not in config:
            raise ValueError(CONFIG_ERROR.format(config_key=STAGES))

        database = DatabaseConfig.from_dict(config[DATABASE_CONFIG])

        stages = [cls.stage_builder(stage) for stage in config[STAGES]]

        return cls(
            database=database,
            stages=stages
        )

    @staticmethod
    def stage_builder(stage: dict):
        if stage[TYPE] == INGESTION:
            return Ingestion.from_dict(stage)
        elif stage[TYPE] == COMPREHENSION:
            return COMPREHENSION
        else:
            return Stage.from_dict(stage)