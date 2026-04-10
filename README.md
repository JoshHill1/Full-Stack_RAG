# Full-Stack RAG App

Phases: 
Phase 1 - Project Setup & Configuration. Set up the repo structure, virtual environment, requirements.txt, and config.py. You'll understand every dependency before installing it. We'll also set up the backend/frontend split from the start so you're not restructuring later. 
Phase 2 - File Parsing. Build parsers.py. Take in PDF, DOCX, TXT, and CSV files, get plain text out. No AI involved yet - just file I/O and libraries. You'll test it by parsing real files and printing the output.
Phase 3 - Chunking. Build chunker.py. Take the plain text from Phase 2 and split it into overlapping chunks. You'll learn why chunk size and overlap matter, and you'll be able to see and inspect every chunk your system produces.
Phase 4 - Embeddings. Build embeddings.py using sentence-transformers locally. Convert chunks into vectors. You'll test it by embedding a few sentences and checking that similar ones produce similar vectors.
Phase 5 - Vector Store. Build vector_store.py using ChromaDB. Store your embedded chunks and query them. By the end of this phase, you can feed in a document, ask a question, and get back the most relevant chunks - no LLM yet, just retrieval.
Phase 6 - Generation. Build generator.py. Take retrieved chunks, construct a prompt, call the Anthropic API, and return an answer. This is where the app starts "talking back." You'll understand exactly what goes into the prompt and why.
Phase 7 - Pipeline. Build pipeline.py. Wire Phases 2 through 6 into a clean interface: ingest(file) and ask(question). Test the full loop end-to-end through a simple CLI.
Phase 8 - Backend API. Build api.py using FastAPI. Expose two endpoints - one for uploading/ingesting files, one for asking questions. Test with Postman or curl. Deploy to Render.
Phase 9 - Frontend. Build the React app. A file upload area, a chat interface, and a clean design. Connect it to your backend API. Deploy to Netlify.
Phase 10 - Polish & Portfolio. Error handling, loading states, a README that explains the architecture, and any UI refinements. Make it something you're proud to show.