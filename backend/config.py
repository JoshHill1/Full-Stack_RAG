import os
from dotenv import load_dotenv

load_dotenv()

# Anthropic
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = "claude-sonnet-4-20250514"

# Embeddings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# ChromaDB
CHROMA_PERSIST_DIR = "chroma_data"
COLLECTION_NAME = "documents"

# File upload limits
MAX_FILE_SIZE_MB = 10
MAX_FILES = 20

# Rate limiting
MAX_QUESTIONS_PER_MINUTE = 10