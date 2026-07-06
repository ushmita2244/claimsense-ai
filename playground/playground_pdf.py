import fitz  # PyMuPDF

PDF_PATH = "data/raw/2024-guide-to-preventing-cancer-web.pdf"

doc = fitz.open(PDF_PATH)

# print("=" * 80)
# print(f"Total Pages: {len(doc)}")
# print("=" * 80)

# for page_number, page in enumerate(doc, start=1):
#     print(f"\nPAGE {page_number}")
#     print("-" * 40)

#     text = page.get_text()

#     print(text[:500])  # Show first 500 characters



# for page in doc:
#     print(page.get_text("blocks"))


for page in doc:
    print(page.get_text("words"))