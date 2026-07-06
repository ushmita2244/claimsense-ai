import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load PDF
doc = fitz.open("data/raw/2024-guide-to-preventing-cancer-web.pdf")

# Extract complete text
full_text = ""

for page in doc:
    full_text += page.get_text("text") + "\n"

print("=" * 80)
print(f"Total Characters: {len(full_text)}")
print("=" * 80)

# Create splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_text(full_text)

print("\nStatistics")

print(f"\nTotal Chunks: {len(chunks)}")

print(f"Average Chunk Length: {sum(len(c) for c in chunks) / len(chunks):.2f}")

print(f"Largest Chunk: {max(len(c) for c in chunks)}")

print(f"Smallest Chunk: {min(len(c) for c in chunks)}")

for i, chunk in enumerate(chunks[:5], start=1):
    print("\n" + "=" * 80)
    print(f"CHUNK {i}")
    print("=" * 80)
    print(chunk)
    print("=" * 80)


