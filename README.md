📝 Novel Chemicals Discovery Agent

🧪 Deskripsi Proyek
Proyek ini adalah pengembangan Platform Penemuan Materi (Material Discovery) Berbasis Kecerdasan Buatan (AI) yang dirancang untuk mengatasi inefisiensi biaya dan waktu yang ekstrem dalam Riset & Pengembangan (R&D) materi baru di industri.

#### Menjalankan Backend #### 
Ikuti langkah-langkah berikut untuk menjalankan backend:

# 1. Instal Library Python
Karena sudah ada file requirements.txt, Anda dapat menginstal semua dependensi yang diperlukan  dengan satu perintah yaitu 
pip install -r requirements.txt 

jika terjadi masalah download manual 
pip install fastapi uvicorn chromadb sentence-transformers google-generativeai python-dotenv httpx
pip install langchain-community
pip install google-genai
pip install langchain-huggingface

# 2. Jalankan Server BackendNavigasikan ke direktori backend dan jalankan server menggunakan Uvicorn:

cd .\beckend\
uvicorn main:app --reload --host 0.0.0.0 --port 8000
    Server akan berjalan di http://0.0.0.0:8000 atau http://127.0.0.1:8000/.

# 3. Endpoint APIBackend menyediakan endpoint POST berikut:
POSThttp://127.0.0.1:8000/combine Untuk menggabungkan atau memproses data.
POSThttp://127.0.0.1:8000/generate Untuk generate senyawa menggunakan model AI.


#### Menjalankan Frontend ####
Frontend dikonfigurasi menggunakan Webpack, TypeScript, dan hot-reload untuk pengembangan.

# 1. Instal Dependensi Node.js
Navigasikan ke direktori frontend Anda (sesuaikan path) dan instal semua dependensi Node.js:

cd 'path/ke/direktori/frontend' 
npm install

# 2. Jalankan Server Pengembangan (Development Server)
Jalankan server pengembangan dengan hot-reload
npm run start-dev

# 3. Build Produksi
Untuk membuat versi production dari frontend yang dioptimalkan, jalankan perintah build:
npm run build

Hasil build akan berada di folder dist/.
Folder landing.page/ dan file kimia1.png disalin secara otomatis ke dist/ oleh copy-webpack-plugin


Backup Tutorial (FIX)

ChemisTry
NOVEL CHEMICAL DISCOVERY AGENT
ChemisTry adalah sebuah portal aplikasi berbasis web, pengguna dapat memasukkan kriteria senyawa yang diinginkan, seperti titik didih, kelarutan, atau menggabungkan senyawa. Dan sistem akan memberikan rekomendasi senyawa potensial beserta prediksi sifat kimianya. Selain itu, sistem dilengkapi dengan kemampuan untuk memberikan penjelasan singkat yang menggambarkan alasan ilmiah dibalik rekomendasi yang dihasilkan.

Fitur Utama dan cara penggunaan 
Generate Senyawa
Generate senyawa adalah fitur yang memungkinkan sistem untuk menghasilkan rekomendasi senyawa kimia berdasarkan kriteria fisik dan fungsional yang dimasukkan oleh pengguna, seperti jenis produk, titik didih, viskositas, dan kelarutan.
Langkah - langkah penggunaan : 
Setelah masuk pada web, anda berada pada tampilan awal, pilih tombol “Try Generate”
Anda akan menemui beberapa text box seperti jenis produk, tujuan/fungsi produk titik didih, dll
Silahkan input kriteria yang ingin anda masukan
Setelah mengisi silahkan tekan tombol “Generate”
Tunggu sebentar, ChemisTry sedang mencarikan senyawa yang cocok dengan input kriteria anda
Selamat, kriteria senyawa yang anda cari sudah muncul
Cek dan pelajari Senyawa tersebut beserta justifikasinya
Apabila hasil generate tidak cukup memuaskan silahkan isi perbaikan pada text box “Perlu Perbaikan?” 
Lalu tekan “Generate Ulang” tunggu sebentar, dan ChemisTry akan memberikan kriteria senyawa yang sesuai dengan kriteria input perbaikan anda.
Jika ingin menyimpan hasil generate senyawa, silahkan tekan simpan dan tunggu pop up akan muncul

Eksplorasi Senyawa Kimia
Eksplorasi senyawa kimia adalah fitur yang dimana user dapat menggabungkan maksimal 2 senyawa yang tersedia kemudian digabungkan dan menghasilkan senyawa baru beserta detail senyawanya. 
Langkah - langkah : 
Setelah masuk pada web, anda berada pada tampilan awal, pilih tombol “Try Combine”
Silahkan pilih senyawa yang sudah tersedia
Pilih maksimal 2 senyawa
Kemudian tekan “Combine”
Tunggu sebentar, Chemistry sedang memproses dan menggabungkan senyawa pilihan anda
Selamat, hasil combine senyawa anda sudah tersedia
Silahkan cek dan pelajari senyawa hasil combine tersebut pada tombol “Detail Senyawa”
Jika ingin menyimpan hasil gabungan senyawa, silahkan tekan simpan dan tunggu pop up akan muncul

Library Compound/Perpustakaan Senyawa
Perpustakaan Senyawa adalah fitur kumpulan semua senyawa, statistik data senyawa yang ada pada Chemistry. User dapat mencari dan mempelajari senyawa tersebut.
Langkah - langkah : 
Pada tampilan awal, bagian atas terdapat beberapa pilihan. Pilih tombol “Library Compound”
Cari senyawa yang ingin anda pahami dan tekan 
Kemudian pelajari senyawa tersebut
Apabila ingin melihat statistik distribusi data senyawa, silahkan pilih tombol “Lihat Statistik”

Tabel Periodik
Tabel periodik adalah fitur yang dimana user dapat belajar dan mengetahui suatu bentuk tabel yang berisi susunan unsur-unsur kimia berdasarkan nomor atom yang dimiliki.
Langkah - langkah : 
Pada tampilan awal scroll sedikit pada Explore dunia senyawa
Tekan tombol “Tabel Periodik”
Silahkan pelajari unsur unsur kimia yang sudah ada dalam tabel periodik


🛠️ Petunjuk Setup Environment
DATASET

Step 1: Setup Python Virtual Environment
Window : 
python -m venv venv
venv\Scripts\activate
Linux/Mac:
python3 -m venv venv
source venv/bin/activate

Step 2: Install Dependencies
Karena sudah ada file requirements.txt, Anda dapat menginstal semua dependensi yang diperlukan  dengan satu perintah yaitu
pip install --upgrade pip
pip install -r requirements.txt

Requirements.txt

pandas
numpy
tqdm
pubchempy
langchain
langchain-community
langchain-openai
chromadb
openai
flask
python-dotenv
chembl_webresource_client


jika terjadi masalah download manual
pip install pandas numpy tqdm requests pubchempy rdkit chembl_webresource_client langchain langchain-community chromadb sentence-transformers deep-translator 

Step 4: Download & Prepare Dataset
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

Agent AI


Step 1: Clone Repository
git clone https://github.com/MENSTRUE/novel-chemiscal

Step 2: Setup Python Virtual Environment
Window : 
python -m venv venv
venv\Scripts\activate
Linux/Mac:
python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
Karena sudah ada file requirements.txt, Anda dapat menginstal semua dependensi yang diperlukan  dengan satu perintah yaitu
pip install --upgrade pip
pip install -r requirements.txt

jika terjadi masalah download manual
pip install fastapi uvicorn chromadb sentence-transformers google-generativeai python-dotenv httpx
pip install langchain-community
pip install google-genai
pip install langchain-huggingface

Step 4: Setup Environment Variables
Buat file .env di root directory:
GEMINI_API_KEY=your_gemini_api_key_here
Cara Mendapatkan Gemini API Key:
Kunjungi Google AI Studio
Sign in dengan Google Account
Click "Get API Key" → "Create API Key"
Copy API Key dan paste ke .env
Step 5 : Cara Menjalankan Aplikasi
Terminal 1 - Backend Server
cd .\backend\
uvicorn main:app --reload --host 127.0.0.1 --port 8000
Terminal 2 - Frontend Server
Navigasikan ke direktori frontend Anda (sesuaikan path) dan instal semua dependensi Node.js:
cd 'path/ke/direktori/frontend'
npm install
Jalankan Server Pengembangan (Development Server)
npm run start-dev
Build Produksi
Untuk membuat versi production dari frontend yang dioptimalkan, jalankan perintah build:
npm run build
Hasil build akan berada di folder dist/. 
Folder landing.page/ dan file kimia1.png disalin secara otomatis ke dist/ oleh copy-webpack-plugin

Deployment
https://novel-chemiscal.vercel.app/
Note : ikuti langkah langkah berikut agar deployment berjalan
Pastikan Terminal 1 - Backend Server sudah berjalan 
Jika masih eror ulangi langkah langkah Terminal 1 - Backend Server

Apabila masih eror cukup gunakan dan nyalakan port Terminal 1 - Backend Server, hal ini terjadi karena deployment backend bersifat komersial hanya membaca Front end nya saja. 


