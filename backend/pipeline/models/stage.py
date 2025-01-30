from abc import abstractmethod
from dataclasses import dataclass

from utils.string_constants import CONFIG_ERROR, TYPE, STAGE_TYPE_ERROR

@dataclass
class Stage:
    stage_type: str

    @classmethod
    def from_dict(cls, stage: dict):
        if TYPE not in stage:
            raise ValueError(CONFIG_ERROR.format(config_key=TYPE))

        return cls(stage_type=stage[TYPE])

    @abstractmethod
    def run(self):
        raise ValueError(STAGE_TYPE_ERROR.format(type=self.stage_type))