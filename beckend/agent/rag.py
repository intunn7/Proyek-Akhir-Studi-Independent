from .retriever_service import retrieve_documents
from .generator_service import generate_answer

class RAGEngine:
    def __init__(self):
        self.is_indexed = False 
        print("RAGEngine initialized.")

    def index_data(self):
        """Melakukan indexing/ingestion data. Dipanggil saat startup main.py."""

        self.is_indexed = True 

    def query(self, user_query: str) -> str:
        """Menjalankan alur RAG (Retrieve -> Generate)."""

        print(f"RAG Pipeline: Running retrieval for query: {user_query}")
        
        retrieved_docs = retrieve_documents(user_query) 
        
        if not retrieved_docs:
            return "Gagal melakukan retrieval dokumen. Pastikan data sudah di-ingest dan server stabil."
            
        print(f"RAG Pipeline: Found {len(retrieved_docs)} relevant documents.")

        final_answer = generate_answer(user_query, retrieved_docs)
        
        return final_answer