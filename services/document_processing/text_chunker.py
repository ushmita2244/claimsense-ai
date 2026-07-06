
from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.config.settings import settings


class TextChunker:

    def __init__(self):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

    def chunk_text(self, text: str) -> list[str]:

        return self.text_splitter.split_text(text)