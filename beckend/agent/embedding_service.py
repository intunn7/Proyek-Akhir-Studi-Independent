
import json
import os
import shutil
from langchain_community.vectorstores.utils import filter_complex_metadata 
from langchain_core.documents import Document 
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

VECTOR_DB_PATH = "chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DATA_FILE_PATH = "data/data_kimia_final_indo.json" 

def initialize_embeddings():
    """Menginisialisasi dan mengembalikan HuggingFace Embeddings."""
    from langchain_community.embeddings import HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def run_ingestion() -> str:
    """Melaksanakan seluruh proses Ingestion dan menyimpan ke Vector DB."""
    try:
        if not os.path.exists(DATA_FILE_PATH):
             return f"Error: File JSON {DATA_FILE_PATH} tidak ditemukan di path."
             
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
            data_list = json.load(f)
            
        documents = []
        for item in data_list:
            content = item.get("content") or item.get("text") or item.get("deskripsi") or ""
            
            if content and len(content) > 50: 
                documents.append(Document(page_content=content, metadata=item)) 
        
        if not documents:
            return "Error: Gagal memuat dokumen. Periksa key konten utama di JSON Anda."
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.split_documents(documents)

        texts = filter_complex_metadata(texts)
        
        embeddings = initialize_embeddings()
        
        if os.path.exists(VECTOR_DB_PATH):
            shutil.rmtree(VECTOR_DB_PATH) 
        
        Chroma.from_documents(
            texts,
            embeddings,
            persist_directory=VECTOR_DB_PATH
        )
        return f"Ingestion berhasil! {len(texts)} chunks dari {len(documents)} dokumen telah disimpan ke Vector DB."

    except Exception as e:
        return f"Error saat menjalankan ingestion: {e}"