from src.tools.ingestion_tool import IngestionTool


class LanguageLoader(IngestionTool):
    def __init__(self, url: str):
        super().__init__(
            url=url
        )

    def run(self):
        pass