from langchain_core.documents import Document
from .llm import get_llm_response
import json 

SYSTEM_PROMPT = (
    "Anda adalah asisten AI yang ahli dalam Kimia. "
    "Gunakan hanya konteks yang diberikan untuk menjawab pertanyaan. "
    "Jika jawaban tidak ditemukan dalam konteks, katakan 'Saya tidak dapat menemukan jawaban yang relevan dari dokumen yang tersedia.' "
    "Pastikan jawaban Anda akurat dan ringkas."
)

def generate_detailed_json_answer(user_query: str, compound_name: str, all_raw_data: str) -> str:
    """
    Mengambil nama senyawa yang direkomendasikan dan memintanya untuk membuat
    output JSON lengkap berdasarkan data mentah.
    """

    prompt = f"""
    Senyawa target yang direkomendasikan adalah '{compound_name}'.
    
    Data kriteria pengguna adalah: {user_query}.
    
    Berikut adalah seluruh dataset kimia Anda:
    {all_raw_data}
    
    **TUGAS:**
    1. Cari dan ekstrak HANYA objek JSON LENGKAP (termasuk semua field detail, data_unsur_penyusun) 
       dari dataset di atas untuk senyawa dengan 'nama_senyawa' yang paling mendekati '{compound_name}'.
    2. Tambahkan DUA field BARU ke objek JSON senyawa tersebut:
       - "skor_kecocokan": (Angka 1-100, nilai kecocokan terhadap kriteria pengguna).
       - "justifikasi_ringkas": (1-2 kalimat ringkas menjelaskan mengapa senyawa ini adalah yang terbaik untuk kriteria pengguna).
       
    **KELUARAN WAJIB JSON**
    Berikan HANYA satu objek JSON murni, tidak ada teks pengantar atau penutup. 
    Contoh output JSON yang diinginkan (WAJIB KETAT):
    {{
        "nama_senyawa": "CID-753",
        "rumus_molekul": "C3H8O3",
        // ... semua field data mentah lainnya ...
        "data_unsur_penyusun": [
            //...
        ],
        "skor_kecocokan": 95,
        "justifikasi_ringkas": "Senyawa ini dipilih karena Titik Didih yang sangat tinggi (>150C) dan Tingkat Risiko Rendah."
        "rumus_struktur_smiles": "OCC(O)CO"
    }}
    """
    
    answer = get_llm_response(prompt, force_json=True)
    return answer

def generate_answer(user_query: str, retrieved_documents: list[Document]) -> str:
    context = "\n---\n".join([doc.page_content for doc in retrieved_documents])
    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"KONTEKS:\n{context}\n\n"
        f"PERTANYAAN PENGGUNA: {user_query}"
    )
    answer = get_llm_response(prompt, force_json=False)
    return answer