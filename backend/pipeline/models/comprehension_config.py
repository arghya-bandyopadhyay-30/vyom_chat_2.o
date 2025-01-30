from pipeline.models.stage import Stage
from utils.string_constants import STAGE_ERROR, TYPE, TOOLS


class Comprehension(Stage):
    @classmethod
    def from_dict(cls, stage: dict):
        if TYPE not in stage:
            raise ValueError(STAGE_ERROR.format(config_key=TYPE))
        # if TOOLS not in stage:
        #     raise ValueError(STAGE_ERROR.format(config_key=TOOLS))

        return cls(
            stage_type=stage[TYPE]
        )

    def run(self):
        print("Comprehension")
