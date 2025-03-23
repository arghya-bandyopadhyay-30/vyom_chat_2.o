from abc import abstractmethod

from utils.string_constants import CONFIG_ERROR, TYPE, STAGE_TYPE_ERROR


class Stage:
    stage_type: str

    def __init__(self, stage_type: str):
        self.stage_type = stage_type

    @classmethod
    def from_dict(cls, config: dict):
        if TYPE not in config:
            raise ValueError(CONFIG_ERROR.format(config_key=TYPE))

        return cls(stage_type=config[TYPE])

    @abstractmethod
    def run(self):
        raise ValueError(STAGE_TYPE_ERROR.format(type=self.stage_type))