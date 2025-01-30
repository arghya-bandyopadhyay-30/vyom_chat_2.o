from dataclasses import dataclass

from pipeline.models.pipeline_config import PipelineConfig


@dataclass
class Config:
    pipeline: PipelineConfig
