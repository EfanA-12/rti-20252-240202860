# Tahap 3 — Pemodelan Topik (LDA)

**Status:** Selesai 

---

## Tujuan

Mengimplementasikan algoritma probabilistik Latent Dirichlet Allocation (LDA) untuk mengelompokkan teks ulasan SeaBank ke dalam topik yang spesifik dan koheren. Algoritma ini dirancang untuk secara eksklusif hanya memproses data teks yang telah disaring dan dilabeli sebagai sentimen "Negatif" oleh model K-NN pada tahap sebelumnya.

## Deliverable

- [x] Fungsi pengambilan DataFrame yang telah difilter (hanya sentimen negatif).
- [x] Implementasi CountVectorizer dari Scikit-Learn untuk membangun dokumen-matriks istilah (Delaunay/Bag-of-Words) khusus untuk distribusi LDA.
- [x] Pelatihan model LatentDirichletAllocation dengan parameter n_components=2 (mencari dua klaster topik utama) dan random_state=42 agar hasil reproduksi tetap stabil.
- [x] Modul ekstraksi probabilitas (Top-N Words) untuk mencetak 5 hingga 10 kata kunci dengan beban distribusi probabilitas tertinggi per klaster topik.
- [x] Visualisasi kualitatif Output berupa distribusi kata dan Word Cloud pada tahap akhir.

## Hasil Verifikasi End-to-End
Diverifikasi secara kualitatif (Human Judgement) melalui pengamatan terhadap deretan kata penyusun topik:
- Isolasi Sentimen: LDA terbukti tidak mengalami ambiguitas (percampuran kata pujian dan keluhan). Tidak ditemukan kata seperti "bagus", "keren", atau "mantap" di dalam klaster, membuktikan bahwa gerbang K-NN pada Tahap 2 sukses besar memblokir masuknya teks berlabel positif.
- Topik 1 (Customer Service): Model berhasil menyatukan dan mengerucutkan keluhan dengan mendistribusikan probabilitas tertinggi pada kelompok kata: nomor, nelfon, nya, gua, udah. Deretan ini merepresentasikan keluhan pengguna saat kesulitan menghubungi layanan pelanggan SeaBank.
- Topik 2 (Fitur Pinjaman): Model mengelompokkan keluhan lain pada fitur pinjaman, ditandai dengan bobot probabilitas tinggi pada deretan kata: pinjam, tahun, dapat, yg, baru.

## Catatan Lingkungan
- Berbeda dengan pendekatan konvensional yang kerap menggunakan pustaka Gensim, implementasi LDA pada eksperimen ini sengaja diprogram sepenuhnya menggunakan modul bawaan Scikit-Learn (sklearn.decomposition.LatentDirichletAllocation). Keputusan ini diambil untuk menghindari isu dependensi kompilator C++ di Windows yang sering kali menyebabkan kegagalan instalasi pada lingkungan lokal.
- Analisis kualitatif lebih lanjut terkait kemunculan kata tidak baku (noise leksikal) akan dibahas secara terpisah pada dokumen Tahap 4 (Failure Analysis).
