# 00-outline

Outline, peta sumber data, dan daftar klaim kunci untuk draf manuskrip ilmiah **Tahap 5**.

---

## 1. Peta Sumber Data & Keselarasan Berkas

Dokumen ini berfungsi sebagai peta kendali untuk memastikan seluruh data statistik yang ditulis pada naskah bersumber dari data empiris yang valid (bukan dari folder contoh/template):

* **Sumber Data Mentah:** Sumber Data Mentah: Skrip `scraper_seabank.py` (menghasilkan 50 ulasan mentah dari Google Play Store) dan `preprocessing_seabank.py` (menyisakan 44 data bersih).
* **Sumber Output Metrik:** Skrip `eksekusi_model.py` (Scikit-Learn).
* **Dokumen Evaluasi Analisis:** File `WS-14` (mengenai Failure Analysis bahasa gaul).
* **Arsitektur & Skema Sistem:** Flowchart alur kerja Machine Learning K-NN dan LDA.
* **Tinjauan Pustaka & Gap:** Matriks Literatur.

---

## 2. Struktur Outline Manuskrip (Template IMRAD)

### Judul Penelitian
*Analisis Sentimen dan Ekstraksi Topik Keluhan Usability pada Aplikasi SeaBank Menggunakan Algoritma K-NN dan Latent Dirichlet Allocation (LDA)*

### Abstrak (Abstract)
Ringkasan latar belakang penumpukan ulasan, metode eksperimen (pembagian data 80:20, filter K-NN dengan K=3, pemodelan 2 topik LDA), hasil akurasi (88,89%), dan kesimpulan kegagalan Sastrawi pada bahasa slang.

### 1. Pendahuluan
* **Latar Belakang:** Kebutuhan pengembang SeaBank membaca ribuan feedback keluhan usability secara otomatis.
* **Rumusan Masalah:** LDA murni rentan mencampuradukkan kata sentimen positif dan negatif.
* **Tujuan & Kontribusi:** Mengukur akurasi pra-pemfilteran K-NN dan mengekstraksi topik spesifik keluhan via LDA pada dataset ulasan aplikasi keuangan.

### 2. Tinjauan Pustaka
* Landasan teori: Pra-pemrosesan teks (Sastrawi), TF-IDF, K-Nearest Neighbors (K-NN), dan Latent Dirichlet Allocation (LDA).
* *Related work*: 4 studi terdahulu (terkait K-NN analisis sentimen dan LDA pada perbankan) dan pemetaan research gap.

### 3. Metodologi
* **Desain Penelitian:** Eksperimental komputasional.
* **Arsitektur Sistem:** Scraping Play Store → Preprocessing → Feature Extraction (TF-IDF & CountVectorizer) → Klasifikasi K-NN → Ekstraksi Topik LDA.
* **Variabel:** IV = Filter sentimen K-NN; DV = Kualitas topik LDA; CV = Parameter K=3 dan LDA n_components=2.

### 4. Hasil dan Analisis
* **Statistik K-NN:** Akurasi K-NN membedakan sentimen mencapai 88,89% dengan waktu komputasi 0,09 detik.
* **Ekstraksi LDA:** Menemukan dua klaster masalah. Topik 1 (Customer Service) dan Topik 2 (Pinjaman).
* **Failure Analysis (Temuan Batasan):** Sastrawi gagal memotong kata gaul (noise), memunculkan kata "nya", "gua", "udah", dan "yg" ke dalam urutan kata kunci LDA.

### 5. Kesimpulan dan Saran
*Metode hybrid (K-NN dilanjutkan LDA) terbukti cepat dan akurat sebagai gerbang penyaring sebelum pemodelan topik.
* Saran: Wajib menyusun Custom Stopword Dictionary (Kamus Bahasa Slang/Informal) untuk penelitian media sosial di masa depan.
---

## 3. Daftar Klaim Kunci (Key Claims) yang Harus Konsisten

1. **Jumlah Sampel Uji Coba:** n = 44 ulasan bersih (setelah dibersihkan dari 50 ulasan mentah).
2. **Skenario Pembagian Data:** MySQL = Train-Test Split dengan rasio 80% data latih dan 20% data uji.
3. **Parameter Model:** Algoritma K-NN menggunakan nilai Ketetanggaan Terdekat K=3; Algoritma LDA mencari 2 Topik (n_components=2).
4. **Rata-rata Waktu Eksekusi:** 0.09 detik (sangat ringan secara komputasional).
5. **Akurasi Klasifikasi (K-NN):** MySQL = **88.89%.** 
6. **Hasil Kata Kunci Topik 1 (Layanan CS):** nya, nelfon, gua, udah, nomor.
7. **Hasil Kata Kunci Topik 2 (Layanan Pinjaman):** pinjam, tahun, dapat, yg, baru.
8. **Data Noise (Analisis Kegagalan):** Kata slang/informal (nya, gua, udah, yg) terbukti lolos dari library Sastrawi, membuktikan batasan (boundary condition) dari alat pra-pemrosesan berbahasa Indonesia baku.
9. **Library Pendukung:** Eksperimen tidak menggunakan Gensim karena isu kompabilitas C++, melainkan murni menggunakan Scikit-Learn untuk efisiensi.
