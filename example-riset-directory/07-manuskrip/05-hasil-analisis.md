## 4. HASIL DAN PEMBAHASAN

### 4.1 Performa Klasifikasi K-Nearest Neighbors (K-NN)
Berdasarkan hasil eksekusi komputasi menggunakan pustaka Scikit-Learn pada skrip Python, algoritma K-Nearest Neighbors (K-NN) bertindak sebagai gerbang penyaring (filter) sentimen ulasan. Pengujian dilakukan dengan skema pembagian dataset 80:20 (80% data latih dan 20% data uji) pada 44 ulasan bersih yang sebelumnya telah diubah menjadi matriks numerik melalui pembobotan TF-IDF.

Hasil evaluasi metrik performa (Confusion Matrix) dengan parameter ketetanggaan K=3 menunjukkan tingkat akurasi klasifikasi sentimen mencapai 88,89%. Selain akurasi yang tergolong sangat tinggi, model klasifikasi ini terbukti sangat ringan secara komputasional. Waktu eksekusi yang dibutuhkan untuk memproses dan mengklasifikasikan teks hanya memakan waktu 0,09 detik. Fakta ini secara empiris menegaskan kelayakan K-NN sebagai pra-kondisi (pre-condition) yang efisien sebelum teks diteruskan ke tahap ekstraksi topik.

### 4.2 Ekstraksi Topik Keluhan Menggunakan Latent Dirichlet Allocation (LDA)
Setelah K-NN berhasil memisahkan sentimen, sistem secara eksklusif hanya mengambil ulasan yang diprediksi "Negatif" untuk diteruskan ke dalam algoritma probabilistik Latent Dirichlet Allocation (LDA). Tujuannya adalah untuk menggali akar masalah usability secara spesifik tanpa tercampur oleh ulasan berupa pujian.

Dengan parameter jumlah topik ditetapkan sebanyak dua (n_components=2), LDA berhasil mengidentifikasi dua klaster keluhan utama pengguna SeaBank:
- Topik 1 (Layanan Customer Service): Didominasi oleh sebaran probabilitas kata kunci seperti nomor, nelfon, nya, gua, udah. Klaster ini secara kualitatif merepresentasikan keluhan dan frustrasi pengguna saat mencoba menghubungi pusat bantuan terkait kendala operasional aplikasi.
- Topik 2 (Kendala Fitur Pinjaman): Didominasi oleh sebaran probabilitas kata kunci seperti pinjam, tahun, dapat, yg, baru. Klaster ini mengindikasikan adanya kebingungan atau masalah teknis pada antarmuka layanan pengajuan pinjaman digital.

### 4.3 Analisis Kegagalan (Failure Analysis) Prapemrosesan Bahasa Informal
Meskipun LDA berhasil mengelompokkan topik keluhan secara koheren, observasi mendalam terhadap deretan kata kunci menemukan adanya anomali linguistik. Kemunculan kata-kata tidak baku seperti gua, udah, yg, dan nya di jajaran probabilitas kata tertinggi membuktikan adanya batasan sistem (boundary condition) pada fase prapemrosesan.

Analisis kegagalan (failure analysis) ini bermuara pada kelemahan pustaka stemmer Sastrawi yang digunakan di awal eksperimen. Sastrawi secara eksklusif hanya dirancang untuk mendeteksi dan memotong kata berbahasa Indonesia baku sesuai tata bahasa resmi. Karena ulasan di Google Play Store sangat didominasi oleh dialek media sosial dan bahasa slang, sistem gagal mengidentifikasi kata-kata tersebut sebagai noise pada tahap stopword removal. Temuan kegagalan instrumental ini justru menjadi kontribusi empiris yang berharga, membuktikan urgensi perancangan Custom Stopword Dictionary (kamus kata henti khusus bahasa informal) pada penelitian NLP perbankan digital di masa mendatang.