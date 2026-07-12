# Tahap 1 — Perancangan Arsitektur Sistem & Skema Pemrosesan Data

**Status:** Selesai

---

## 1. Komponen Sistem

1. Modul Scraping (google-play-scraper) — bertugas mengekstrak ulasan mentah (teks dan rating) dari pengguna aplikasi SeaBank secara otomatis dari antarmuka Google Play Store.
2. Modul Pra-pemrosesan Teks (Sastrawi & Regex)
- Regex: Membersihkan teks dari karakter khusus, angka, dan emoji.
- Sastrawi: Melakukan case folding, stemming (pemotongan imbuhan), dan stopword removal (penghapusan kata hubung baku).
3. Modul Klasifikasi Sentimen (Scikit-Learn K-NN) — bertindak sebagai gerbang penyaring (gatekeeper). Mengklasifikasikan teks berdimensi tinggi menggunakan pembobotan TF-IDF untuk memisahkan sentimen positif (pujian) dan negatif (keluhan).
4. Modul Pemodelan Topik (Scikit-Learn LDA) — sistem utama yang menerima teks berlabel negatif untuk mengekstrak klaster topik keluhan secara probabilistik.

## 2. Alur Resolusi Kunci (Mitigasi)

| Kolom | Tipe Data | Deskripsi | 
|---|---|---|
| username | String | Identitas/nama akun pembuat ulasan. |
| score | Integer (1-5) | Rating bintang mentah dari Google Play Store. |
| content | String | Teks ulasan asli sebelum dibersihkan. |
| teks_bersih | String | Teks hasil proses Regex dan Sastrawi. |
| label | String/Kategori | Label awal (Positif/Negatif) berdasarkan parameter rating. |
| tfidf_weight | Float | Nilai bobot vektor TF-IDF per fitur kata. |
| knn_prediction | String/Kategori | Hasil prediksi klasifikasi dari algoritma K-NN. |

Data ini diekspor ke dalam format CSV (seabank_reviews_clean.csv) sebagai bentuk penyimpanan permanen untuk tahap visualisasi.

## 4. Skema Redis (Murni L1 Cache JWKS)
Sebagai pengganti arsitektur cache, sistem menggunakan pembobotan Term Frequency-Inverse Document Frequency (TF-IDF) untuk mengevaluasi seberapa penting sebuah kata di dalam kumpulan ulasan.

| Key Pattern | Tipe  | Tujuan |
|---|---|---|---|
| Term Frequency (TF) | Mengukur frekuensi kemunculan kata dalam satu ulasan tunggal. | Mengetahui fokus utama dari satu pengguna tertentu. |
| Inverse Document Frequency (IDF) | Mengukur kelangkaan kata di seluruh dataset ulasan. | Menekan bobot kata yang terlalu umum dan mengangkat bobot kata spesifik (seperti "nelfon", "pinjam"). |

## 5. Keputusan Teknis (Final)

1. Framework Machine Learning: Eksperimen murni menggunakan Scikit-Learn pada bahasa pemrograman Python. Pustaka Gensim tidak digunakan untuk menghindari isu kompatibilitas dependensi C++ pada beberapa lingkungan eksekusi.
2. Pra-pemrosesan (Sastrawi): Sengaja tidak menggunakan Custom Stopword Dictionary khusus bahasa slang. Hal ini diputuskan untuk menguji batas kemampuan pustaka standar (boundary condition) yang nantinya akan dibahas pada bagian Failure Analysis.
3. Pembagian Data (Split Ratio): Menggunakan rasio 80:20 (80% data latih dan 20% data uji) untuk mendapatkan matriks pengujian yang optimal pada sampel 44 data ulasan bersih.
4. Parameter K-NN: Menggunakan nilai k-neighbors = 3 (K=3) untuk menghindari hasil seri dalam pemungutan suara mayoritas kelas tetangga, sekaligus mencegah overfitting pada dataset kecil.
5. Parameter LDA: Membatasi pencarian probabilitas hanya pada 2 klaster utama (n_components=2).
