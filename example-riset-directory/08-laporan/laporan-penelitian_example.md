# Laporan Penelitian

**Judul:** Analisis Sentimen dan Ekstraksi Topik Keluhan Usability pada Aplikasi SeaBank Menggunakan Algoritma K-NN dan Latent Dirichlet Allocation (LDA)

**Peneliti:** Efan Aryanto Addli
**Target Publikasi:** Sinta 5
**Status Penelitian:** Tahap 1–4 selesai; Tahap 5 (draf naskah jurnal) sedang berjalan ([../07-manuskrip/](../07-manuskrip/))

---

## 1. Ringkasan Eksekutif

Penelitian ini merancang, mengimplementasikan, dan mengevaluasi secara empiris arsitektur komputasional hibrida berupa Filter Sentimen K-Nearest Neighbors (K-NN) yang dilanjutkan dengan Latent Dirichlet Allocation (LDA) untuk mengekstrak topik keluhan pengguna secara otomatis. Evaluasi dilakukan melalui eksperimen prapemrosesan teks (menggunakan Sastrawi dan TF-IDF) pada data ulasan mentah aplikasi SeaBank yang ditarik dari Google Play Store. Pembagian data uji dan latih dilakukan dengan rasio 80:20, diikuti pemodelan topik spesifik dari ulasan bernada negatif.

**Temuan utama:**

- K-NN berfungsi sangat efisien sebagai gatekeeper (penyaring awal), mencetak akurasi klasifikasi sebesar 88,89% dengan waktu komputasi yang sangat ringan (0,09 detik).
- Ekstraksi LDA terhindar dari ambiguitas (percampuran kata pujian dan keluhan) karena data telah difilter. Ditemukan 2 klaster masalah utama: Layanan Customer Service dan Kendala Fitur Pinjaman.
- Ditemukan boundary condition (batasan sistem): Pustaka prapemrosesan Sastrawi gagal mendeteksi dan menghapus bahasa slang (seperti gua, udah, yg). Kegagalan ini muncul sebagai noise pada probabilitas tertinggi distribusi kata LDA, membuktikan urgensi pengembangan Custom Stopword Dictionary khusus bahasa informal Indonesia.


---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang

Aplikasi perbankan digital seperti SeaBank menerima ribuan ulasan pengguna setiap hari, yang memuat wawasan krusial mengenai masalah usability antarmuka dan layanan pelanggan. Pada implementasi naif pemodelan topik, algoritma langsung "menelan" seluruh ulasan mentah. Akibatnya, sentimen positif dan negatif sering tercampur dalam satu klaster topik, mengaburkan konteks keluhan. Pengembang kesulitan mencari tahu akar masalah secara spesifik akibat penumpukan data tak terstruktur ini.

### 2.2 Rumusan Masalah

1. Seberapa besar tingkat akurasi algoritma K-NN berbasis TF-IDF dalam mengklasifikasikan dan menyaring sentimen ulasan secara otomatis?
2. Apa saja klaster topik keluhan usability spesifik yang berhasil diekstrak oleh LDA setelah asupan data dibatasi hanya pada sentimen negatif?
3. Bagaimana dampak kelemahan alat prapemrosesan teks baku (Sastrawi) terhadap hasil akhir koherensi topik, dan bagaimana failure analysis-nya?  

### 2.3 Tujuan Penelitian

1. Mengimplementasikan dan mengukur tingkat akurasi algoritma K-NN berbasis TF-IDF sebagai filter pemisah sentimen ulasan secara otomatis.
2. Mengekstraksi klaster topik keluhan usability secara spesifik menggunakan algoritma LDA dari asupan data yang telah difilter.
3. Merumuskan failure analysis terkait kelemahan pustaka Sastrawi dalam memproses bahasa slang atau informal.

---

## 3. Metodologi dan Pelaksanaan

Penelitian dilaksanakan dalam 5 tahap.

### 3.1 Tahap 1 — Perancangan Arsitektur & Skema Database

**Status: Selesai.** Pustaka google-play-scraper digunakan untuk menarik 50 ulasan dari Google Play Store. Data melewati case folding, pembersihan simbol (Regex), dan stemming/stopword removal menggunakan pustaka Sastrawi. Menyisakan 44 data teks bersih yang siap diekstrak.  

### 3.2 Tahap 2 — Implementasi API Gateway (Go)

**Status: Selesai.** Model dibangun menggunakan framework Scikit-Learn. Teks diubah menjadi vektor numerik melalui pembobotan TF-IDF. Sistem dipecah menggunakan train_test_split (80% data latih, 20% data uji). Model K-NN dieksekusi dengan parameter ketetanggaan K=3 untuk menghindari bias pada sampel kecil.

### 3.3 Tahap 3 — Pengujian Beban k6

**Status: Selesai.** Model LDA diprogram untuk hanya menerima DataFrame ulasan yang telah diprediksi "Negatif" oleh K-NN. Parameter ditetapkan pada pencarian 2 topik utama (n_components=2). Ekstraksi difokuskan pada observasi kualitatif Top-N Words.

### 3.4 Tahap 4 — Ekstraksi Data & Visualisasi

**Status: Selesai.** Dibangun *pipeline* analisis Python (`05-kode/analysis/`, dijalankan via `python run_all.py`) terdiri dari:

| Modul | Fungsi |
|---|---|
| `scraper_seabank.py` | Menarik (scraping) data ulasan mentah secara otomatis dari antarmuka Google Play Store. |
| `preprocessing_seabank.py` | Membersihkan teks melalui tahap case folding, cleansing (Regex), stopword removal, dan stemming menggunakan pustaka Sastrawi. |
| `eksekusi_model.py` | Menjalankan ekstraksi fitur (TF-IDF), membelah data latih/uji (80:20), mengeksekusi algoritma K-NN (K=3), dan melatih pemodelan topik LDA (n_components=2). |



### 3.5 Tahap 5 — Draf Naskah Jurnal

**Status: Selesai.** Draf konten per bab (Pendahuluan, Metodologi, Hasil, Kesimpulan) dan Naskah Jurnal telah dikonsolidasi menjadi dokumen skripsi akhir.

---

## 4. Hasil Penelitian

### 4.1 Performa Klasifikasi Sentimen (K-Nearest Neighbors)

| Parameter Pengujian | Metrik Evaluasi | Hasil | Keterangan |
|---|---|---|---|
| Pembagian Data | Rasio Train-Test | 80:20 | Dari total 44 data ulasan bersih. | 
| Ketetanggaan (Neighbors) | K | 3 | Parameter optimal untuk klasifikasi. | 
| Waktu Komputasi | Execution Time | 0,09 detik | Sangat ringan dan efisien. |
| Kinerja Model | Akurasi | 88,89% | Layak digunakan sebagai filter awal. | 


### 4.2 Hasil Ekstraksi Topik Keluhan (Latent Dirichlet Allocation)

| Klaster Topik LDA | Representasi Keluhan | Probabilitas Kata Kunci Tertinggi (Top Words) |
|---|---|---|
| Topik 1 |Layanan Customer Service |nomor, nelfon, nya, gua, udah |
| Topik 2 | Kendala Fitur Pinjaman | pinjam, tahun, dapat, yg, baru |


### 4.3 Temuan Analisis Kegagalan (Failure Analysis)

| Komponen Prapemrosesan | Jenis Kendala (Boundary Condition) | Noise yang Lolos ke Model LDA |
|---|---|---|
| Pustaka Sastrawi | Gagal mendeteksi dan menghapus bahasa slang/informal. | nya, gua, udah, yg |


---

## 5. Kendala dan Catatan Lingkungan

- **Limitasi Library Sastrawi:** Hanya mendukung bahasa Indonesia baku (Kamus Besar Bahasa Indonesia). Hal ini memerlukan penanganan manual atau kustomisasi pustaka di masa depan.  
- **Kompatibilitas Dependensi:** Penggunaan pustaka Gensim untuk LDA sempat dihindari karena kendala kompilasi komponen C++ di beberapa lingkungan lokal. Solusinya, algoritma LDA sepenuhnya diganti dan dieksekusi menggunakan modul bawaan Scikit-Learn yang jauh lebih stabil di berbagai OS.  
- **Ukuran Dataset Eksperimen:** Dijalankan pada 44 ulasan sebagai purwarupa pembuktian konsep (proof of concept). Untuk penggunaan pada level produksi, jumlah dataset perlu diperbesar ke ribuan baris. 

---

## 6. Kesimpulan dan Saran

Skema K-NN + LDA Hybrid terbukti sangat efektif memitigasi pencampuran sentimen pada analisis topik — K-NN menyaring sentimen dengan akurasi 88,89%, memastikan LDA memetakan akar keluhan antarmuka secara spesifik (CS & Pinjaman). Satu trade-off teridentifikasi: penggunaan pustaka standar menyebabkan lolosnya noise bahasa slang. Disarankan untuk merancang Custom Stopword Dictionary pada penelitian lanjutan.

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder | Isi | Status |
|---|---|---|
| [01-proposal/](../01-proposal/) | Proposal penelitian Analisis Sentimen dan Ekstraksi Topik K-NN & LDA (Bab 1-3) | Selesai |
| [02-literatur/](../02-literatur/) | Matriks literatur terkait K-NN, LDA, dan pencarian research gap (usability perbankan digital) | Selesai |
| [05-kode/](../05-kode/) | Arsitektur sistem Machine Learning, pemetaan variabel eksperimen, dan evaluasi Confusion Matrix. | Selesai |
| [04-data/](../04-data/) | Data ulasan mentah Play Store (seabank_reviews_raw.csv) dan data bersih (seabank_reviews_clean.csv) | Selesai |
| [05-kode/](../05-kode/) | Skrip Python lengkap (scraper_seabank.py, preprocessing_seabank.py, eksekusi_model.py) | Selesai |
| [06-output/](../06-output/) | Matriks Akurasi (88,89%), visualisasi Word Cloud, bar chart probabilitas LDA, dan hasil Failure Analysis | Selesai |
| [07-manuskrip/](../07-manuskrip/) | Draf naskah artikel jurnal ilmiah dan kompilasi utuh dokumen skripsi (Abstrak s.d. Daftar Pustaka) | Selesai |
| [08-laporan/](../08-laporan/) | Dokumen laporan resmi hasil penelitian institusi (Berkas Ini) | Selesai |

**Cara reproduksi penuh:**

```bash
# Tahap 1: Jalankan skrip scraping untuk menarik ulasan mentah dari Google Play Store
python scraper_seabank.py

# Tahap 2: Jalankan prapemrosesan teks (cleansing, Sastrawi, stopword removal, stemming)
python preprocessing_seabank.py

# Tahap 3: Jalankan pipeline Machine Learning (Klasifikasi K-NN, metrik akurasi, dan ekstraksi topik LDA)
python eksekusi_model.py
```
