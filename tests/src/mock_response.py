import asyncio


class MockResponse:
    def __init__(self, text, status):
        super().__init__()
        self._text = text
        self.status = status

    async def text(self):
        return self._text

    async def get(self, url):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self
