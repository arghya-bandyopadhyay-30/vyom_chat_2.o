from dataclasses import dataclass

from utils.string_constants import NEO4J_URI, CONFIG_ERROR, NEO4j_USERNAME, NEO4J_PASSWORD, NEO4J_DATABASE

@dataclass
class DatabaseConfig:
    neo4j_uri: str
    neo4j_username: str
    neo4j_password: str
    neo4j_database: str

    @classmethod
    def from_dict(cls, config: dict):
        if NEO4J_URI not in config:
            raise ValueError(CONFIG_ERROR.format(config_key=NEO4J_URI))
        if NEO4j_USERNAME not in config:
            raise ValueError(CONFIG_ERROR.format(config_key=NEO4j_USERNAME))
        if NEO4J_PASSWORD not in config:
            raise ValueError(CONFIG_ERROR.format(config_key=NEO4J_PASSWORD))
        if NEO4J_DATABASE not in config:
            raise ValueError(CONFIG_ERROR.format(config_key=NEO4J_DATABASE))

        return cls(
            neo4j_uri=config[NEO4J_URI],
            neo4j_username=config[NEO4j_USERNAME],
            neo4j_password=config[NEO4J_PASSWORD],
            neo4j_database=config[NEO4J_DATABASE]
        )
