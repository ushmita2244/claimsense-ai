from pathlib import Path
from typing import List

from services.document_processing.pdf_loader import PDFLoader
from services.document_processing.text_chunker import TextChunker
from services.embeddings.embedding_service import EmbeddingService
from services.vector_db.chroma_service import ChromaService


class IngestionService:

    def __init__(self):

        self.pdf_loader = PDFLoader()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.vector_db = ChromaService()

    def ingest_pdf(self, pdf_path: str) -> dict:
        """
        Ingest a PDF into the vector database.

        Steps:
        1. Load PDF
        2. Extract text
        3. Split into chunks
        4. Generate embeddings
        5. Store in ChromaDB

        Returns:
            Dictionary containing ingestion statistics.
        """

        # Load PDF

        text = self.pdf_loader.load_pdf(pdf_path)
        
        print(f"Loaded {len(text)} characters.")

        # Split into chunks

        chunks = self.chunker.chunk_text(text)

        # Extract file name

        file_name = Path(pdf_path).name

        # Store each chunk
        
        embeddings = self.embedding_service.generate_embeddings(chunks)
        
        for index, (chunk, embedding) in enumerate( zip(chunks, embeddings), start=1 ):

            self.vector_db.add_document(
            doc_id=f"{file_name}_{index}",
            text=chunk,
            embedding=embedding,
            metadata={
            "source": file_name,
            "chunk_number": index
            }
            )


        # Return summary
        return {
            "file_name": file_name,
            "characters_loaded": len(text),
            "chunks_created": len(chunks),
            "documents_in_collection": self.vector_db.count()
        }
        
    def ingest_directory( self, directory_path: str) -> list[dict]:
        
        directory = Path(directory_path)
        
        pdf_files = list( directory.glob("*.pdf"))
        
        results = []
        
        print(f"\nFound {len(pdf_files)} PDF(s).\n")
        
        for pdf_number, pdf_file in enumerate(pdf_files, start=1):
            
            print("=" * 80)
            print(f"Processing PDF {pdf_number}/{len(pdf_files)}")
            print(f"File: {pdf_file.name}")
            print("=" * 80)
            
            summary = self.ingest_pdf(str(pdf_file))
            results.append(summary)
            
        return results
        
        