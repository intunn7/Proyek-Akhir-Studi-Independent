import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError
from google.genai import types 

load_dotenv()

GEMINI_MODEL_DEFAULT = "gemini-2.5-flash" 
GEMINI_MODEL_PRO = "gemini-2.5-pro" 

MAX_RETRIES = 5  
BASE_WAIT_TIME = 2 


def get_gemini_client():
    """Menginisialisasi dan mengembalikan klien Google GenAI."""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY tidak ditemukan di environment variables.")
        return genai.Client(api_key=api_key)
    except Exception as e:
        print(f"Error saat inisialisasi Gemini Client: {e}")
        return None

def get_llm_response(prompt: str, force_json: bool = False) -> str:
    """Mengambil respons dari Gemini LLM, opsional memaksa output JSON, dengan retry untuk 429."""
    client = get_gemini_client()
    if not client:
        return "Error: LLM client tidak dapat diinisialisasi."
        
    config_params = {"temperature": 0.2} 
    model_to_use = GEMINI_MODEL_DEFAULT
    
    if force_json:
        config_params['response_mime_type'] = "application/json" 
        model_to_use = GEMINI_MODEL_DEFAULT
    
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model=model_to_use,
                contents=[prompt],
                config=types.GenerateContentConfig(**config_params)
            )
            return response.text 
            
        except APIError as e:
            error_detail = str(e)

            if "429" in error_detail or "RESOURCE_EXHAUSTED" in error_detail:
                if attempt < MAX_RETRIES - 1:
                    wait_time = BASE_WAIT_TIME ** attempt 
                    print(f"RATE LIMIT HIT (429). Retrying in {wait_time}s (Attempt {attempt + 1}/{MAX_RETRIES}).")
                    time.sleep(wait_time)
                    continue 
                else:
                    return "API_ERROR_429: Kuota terlampaui setelah beberapa kali percobaan. Mohon tunggu 1 menit."
            
            return f"API_ERROR: {error_detail}" 
            
        except Exception as e:
            return f"Terjadi kesalahan LLM tak terduga: {e}"
            
    return "Error: Gagal memproses permintaan setelah semua percobaan."