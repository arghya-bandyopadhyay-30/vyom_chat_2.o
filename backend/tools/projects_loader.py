from tools.ingestion_tool import IngestionTool


class ProjectsLoader(IngestionTool):
    def __init__(self, url: str):
        super().__init__(
            url=url
        )

    def run(self):
        pass