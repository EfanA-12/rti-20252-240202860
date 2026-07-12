# Tahap 4 — Evaluasi Metrik K-NN & Failure Analysis

**Status:** Selesai 

---

## Tujuan

Melakukan rekapitulasi data hasil eksekusi komputasi pada skrip Python untuk mendapatkan angka metrik performa K-NN secara definitif, serta merumuskan analisis kegagalan (Failure Analysis) linguistik terhadap parameter prapemrosesan teks Sastrawi.
## Deliverable

- [x] Ekstraksi metrik Confusion Matrix (True Positive, True Negative) untuk menghitung Akurasi (Accuracy) model K-NN.
- [x] Pencatatan nilai akhir waktu eksekusi komputasi (dalam hitungan detik).
- [x] Rekapitulasi daftar 5 kata kunci teratas pada distribusi Topik 1 dan Topik 2 hasil model LDA.
- [x] Perumusan Failure Analysis berdasarkan temuan kata tidak baku (noise) yang mendistorsi pemodelan topik.
- [x] Pembuatan grafik sebaran Word Cloud per topik dan ekspor visualisasinya ke format PNG (06-output/figures/).

## Desain yang Diimplementasikan

### Modul Pengolahan (Pada eksekusi_model.py)

Skrip diatur untuk tidak hanya melatih model, namun juga mengotomatisasi cetakan laporan hasil menggunakan pustaka sklearn.metrics. Evaluasi didorong secara langsung menggunakan modul accuracy_score dan confusion_matrix.
Visualisasi kata untuk LDA di-kustomisasi menggunakan pustaka pihak ketiga wordcloud pada Python untuk membentuk diagram awan kata di mana ukuran font sebuah kata diatur berbanding lurus dengan nilai probabilitas (weight)-nya.

## Hasil

### Metrik Akurasi Filter K-NN (K=3)

Hasil perhitungan algoritma (K-NN dengan parameter k-neighbors=3) diukur dengan parameter pembagian data uji sebesar 20%.

| Metrik Evaluasi | Hasil Komputasi |Interpretasi Praktis |
|---|---|---|
| Akurasi (Accuracy Score) | 88,89% | Sangat mumpuni. Model berhasil mereplikasi kemampuan analisis manusia untuk membedakan ulasan SeaBank bernada keluhan dan bernada pujian. |
| Waktu Eksekusi (Computation Time) | 0,09 Detik | Sangat ringan. Model ini sangat layak diterapkan sebagai filter awal (gerbang) tanpa takut menjadi bottleneck performa sistem. |


### Failure Analysis (Analisis Kegagalan Prapemrosesan)

Terdapat temuan berupa batasan sistem (boundary condition) pada fase persiapan data. Meskipun model LDA sangat efektif menemukan topik "Pinjaman" dan "Customer Service", terdapat anomali pada jajaran kata kuncinya.
Kata-kata seperti nya, gua, udah, dan yg berhasil menduduki puncak bobot probabilitas. Padahal, kata-kata tersebut adalah kata hubung tak bermakna (noise) yang seharusnya tidak muncul di dalam klaster pembentuk topik.

Kesimpulan Failure Analysis:
Pustaka stemming Sastrawi terbukti memiliki kemampuan yang sangat terbatas saat dihadapkan pada teks bergenre media sosial. Sastrawi secara baku dikembangkan dan dikunci berdasarkan Kamus Besar Bahasa Indonesia (KBBI) sehingga ia gagal mengenali, memotong, dan menghapus dialek slang (bahasa gaul) atau singkatan (text speak) khas warganet. Temuan cacat performa ini digunakan sebagai argumen utama yang merekomendasikan perlunya integrasi Custom Stopword Dictionary (Kamus Kata Henti Kustom) pada penelitian klasifikasi teks di masa mendatang.