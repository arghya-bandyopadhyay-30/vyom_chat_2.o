from abc import abstractmethod


class IngestionTool:
    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def run(self):
        pass