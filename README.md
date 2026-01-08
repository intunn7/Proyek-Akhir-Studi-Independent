📝 **Novel Chemicals Discovery Agent**

---

## 🧪 Deskripsi Proyek

**Novel Chemicals Discovery Agent (ChemisTry)** adalah platform *Material Discovery* berbasis **Artificial Intelligence (AI)** yang dirancang untuk mengatasi inefisiensi biaya dan waktu dalam proses **Riset & Pengembangan (R&D)** senyawa kimia. Platform ini memungkinkan pengguna untuk:

* Menghasilkan (generate) rekomendasi senyawa baru
* Menggabungkan (combine) senyawa yang ada
* Mengeksplorasi pustaka senyawa dan statistik data
* Mempelajari unsur melalui tabel periodik interaktif

---

## 🔄 Data Preprocessing & Dataset

Proses *preprocessing* data merupakan fondasi utama sistem AI pada ChemisTry. Dataset kimia dikumpulkan, diperkaya, dan diproses sebelum digunakan oleh *vector database* dan model AI.

### 📦 Sumber Dataset

Dataset utama diperoleh dan dikembangkan dari repository berikut:

🔗 (https://github.com/intunn7/Dataset-Proyek-Akhir-Studi-Independent.git)

### ⚙️ Alur Preprocessing Dataset

1. **Download Dataset Kimia**

   * Mengambil data senyawa dari **PubChem** dan **ChEMBL**

2. **Enrichment Data**

   * Perhitungan properti molekuler menggunakan **RDKit**
   * Pengambilan properti eksperimen tambahan dari PubChem

3. **Vectorization**

   * Konversi deskripsi senyawa menjadi embedding vektor
   * Penyimpanan embedding ke dalam **ChromaDB**

4. **Integrasi Data Unsur**

   * Penggabungan data unsur kimia
   * Translasi data ke Bahasa Indonesia

### ▶️ Menjalankan Pipeline Preprocessing

```bash
# Step 1: Download dari PubChem & ChEMBL
python 01_download_datasets.py

# Step 2: Enrich dengan RDKit calculations
python 02_enrich_dataset.py

# Step 2b: Fetch experimental properties
python 02b_fetch_pubchem_properties.py

# Step 3: Build vector database
python 03_build_vector_database.py

# Step 4: Merge dengan data unsur & translate
python 04_merge_elements_with_chemicals.py
```

---

## 🚀 Menjalankan Backend

### 1️⃣ Install Library Python

Pastikan file `requirements.txt` tersedia, lalu jalankan:

```bash
pip install -r requirements.txt
```

Jika terjadi masalah, instal manual:

```bash
pip install fastapi uvicorn chromadb sentence-transformers google-generativeai python-dotenv httpx
pip install langchain-community
pip install google-genai
pip install langchain-huggingface
```

### 2️⃣ Jalankan Server Backend

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Server akan berjalan di:

* [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 3️⃣ Endpoint API

* **POST** `/generate` → Generate senyawa menggunakan AI
* **POST** `/combine` → Menggabungkan senyawa

---

## 💻 Menjalankan Frontend

Frontend dibangun menggunakan **TypeScript + Webpack**.

### 1️⃣ Install Dependensi

```bash
cd frontend
npm install
```

### 2️⃣ Development Server

```bash
npm run start-dev
```

### 3️⃣ Build Production

```bash
npm run build
```

Hasil build akan berada di folder:

```
dist/
```

📌 **Catatan Penting**:

* Folder **frontend/** adalah *landing page* dan UI utama aplikasi
* Tidak ada folder `landing.page/`
* Seluruh aset frontend akan dibundel ke dalam `dist/`

---

## 🧠 Fitur Utama & Cara Penggunaan

### 🔬 Generate Senyawa

Fitur untuk menghasilkan rekomendasi senyawa berdasarkan kriteria fisik dan fungsional.

**Langkah-langkah**:

1. Klik **Try Generate**
2. Isi kriteria (fungsi, titik didih, kelarutan, dll)
3. Klik **Generate**
4. Pelajari hasil dan justifikasi ilmiahnya
5. Gunakan **Generate Ulang** jika perlu perbaikan

---

### ⚗️ Combine Senyawa

Menggabungkan maksimal 2 senyawa untuk menghasilkan senyawa baru.

**Langkah-langkah**:

1. Klik **Try Combine**
2. Pilih maksimal 2 senyawa
3. Klik **Combine**
4. Lihat detail hasil senyawa

---

### 📚 Library Compound

Menampilkan seluruh senyawa beserta statistik distribusinya.

**Langkah-langkah**:

1. Klik **Library Compound**
2. Cari senyawa
3. Lihat detail atau statistik

---

### 🧪 Tabel Periodik

Media pembelajaran unsur kimia interaktif.

**Langkah-langkah**:

1. Scroll ke bagian eksplorasi
2. Klik **Tabel Periodik**
3. Pelajari unsur-unsur kimia

---

## 🛠️ Setup Environment (Agent AI)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/MENSTRUE/novel-chemiscal
```

### 2️⃣ Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Environment Variables

Buat file `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

### 🔑 Cara Mendapatkan Gemini API Key (Google AI Studio)

Ikuti langkah berikut untuk mendapatkan **Gemini API Key** resmi dari Google:

1. Buka **Google AI Studio**

   * Kunjungi: [https://aistudio.google.com](https://aistudio.google.com)

2. Login menggunakan **Google Account**

3. Klik menu **Get API Key**

   * Pilih **Create API Key**
   * Pilih atau buat project Google Cloud (jika diminta)

4. Salin (**Copy**) API Key yang dihasilkan

5. Tempelkan API Key ke dalam file `.env`:

```env
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxx
```

📌 **Catatan Keamanan**:

* Jangan meng-*commit* file `.env` ke repository publik
* Gunakan `.gitignore` untuk mengecualikan `.env`

---

---

## 🌐 Deployment

🔗 **Frontend**: [https://novel-chemiscal.vercel.app/](https://novel-chemiscal.vercel.app/)

📌 **Catatan**:

* Backend **tidak dideploy secara publik** (komersial)
* Backend harus dijalankan **secara lokal**
* Frontend hanya membaca response dari backend lokal

---

✨ *Novel Chemicals Discovery Agent — Accelerating Chemical Innovation with AI*
