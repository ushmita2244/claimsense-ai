import fitz

class PDFLoader:

    def load_pdf(self, pdf_path: str):

        document = fitz.open(pdf_path)

        text = ""

        for page in document:

            text += page.get_text("text")

        return text