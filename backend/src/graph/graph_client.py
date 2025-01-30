class GraphClient:
    def __init__(self, neo4j_uri: str, auth: tuple[str, str], db_name: str):
        self.neo4j_uri = neo4j_uri
        self.auth = auth
        self.db_name = db_name

