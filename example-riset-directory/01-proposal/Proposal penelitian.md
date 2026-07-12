# PROPOSAL PENELITIAN

## A. JUDUL
Analisis Sentimen dan Ekstraksi Topik Keluhan Usability pada Aplikasi SeaBank Menggunakan Algoritma K-NN dan Latent Dirichlet Allocation (LDA)

## B. RINGKASAN
Ulasan pengguna pada aplikasi perbankan digital memuat wawasan penting bagi pengembang, namun jumlahnya yang masif menyulitkan analisis secara manual. Pemodelan topik murni menggunakan algoritma seperti Latent Dirichlet Allocation (LDA) sering kali menghasilkan topik yang ambigu karena tercampurnya sentimen positif dan negatif di dalam satu ruang data. Penelitian ini bertujuan untuk meningkatkan kualitas pemodelan topik keluhan dengan menerapkan algoritma K-Nearest Neighbors (K-NN) sebagai filter sentimen prakondisi sebelum teks diproses oleh LDA. Metode yang diusulkan mencakup pengumpulan data ulasan dari platform distribusi aplikasi, pra-pemrosesan menggunakan pembersihan reguler dan Sastrawi, pembobotan matriks TF-IDF, klasifikasi sentimen menggunakan K-NN, dan ekstraksi topik spesifik melalui LDA. Luaran yang ditargetkan berupa model hibrida yang efisien secara komputasi serta mampu mengidentifikasi topik keluhan yang koheren. Selain itu, penelitian ini juga akan menghasilkan analisis batasan sistem terkait penanganan bahasa informal untuk merumuskan daftar kata henti kustom (custom stopword dictionary).

## C. KATA KUNCI
Analisis Sentimen; Latent Dirichlet Allocation; K-Nearest Neighbors; Ulasan Aplikasi; SeaBank

## D. PENDAHULUAN

### D.1. LATAR BELAKANG DAN RUMUSAN MASALAH
Aplikasi perbankan digital SeaBank melayani jutaan pengguna yang secara aktif memberikan ulasan di Google Play Store. Ulasan ini memuat masukan krusial terkait performa sistem, antarmuka, fitur pinjaman, hingga layanan pelanggan. Namun, volume data tekstual yang sangat besar menyulitkan tim pengembang untuk mengekstrak inti permasalahan secara manual. Gejala yang muncul di industri adalah penumpukan keluhan tak terbaca yang memperlambat respons perbaikan sistem (bug fixing). Akar masalahnya terletak pada ketiadaan sistem klasifikasi otomatis yang mampu memilah keluhan secara spesifik dan akurat. Jika dibiarkan, pengembang akan kehilangan wawasan berharga yang berdampak langsung pada stagnasi layanan dan penurunan tingkat kepuasan pengguna.

### D.2. PENDEKATAN PEMECAHAN MASALAH
Penelitian ini bertujuan untuk mengekstrak topik keluhan utama pengguna SeaBank secara otomatis. Hipotesis awal penelitian ini adalah: memfilter teks ulasan berdasarkan sentimen negatif menggunakan K-Nearest Neighbors (K-NN) sebelum proses pemodelan topik akan menghasilkan klaster keluhan yang lebih spesifik dibandingkan jika seluruh teks diproses sekaligus. Intervensi yang diusulkan adalah arsitektur sistem hibrida (K-NN dilanjutkan dengan LDA), yang akan dievaluasi dan dibandingkan dengan baseline berupa algoritma LDA murni tanpa filter sentimen.

### D.3. STATE OF THE ART DAN KEBARUAN
Studi terdahulu di bidang pemrosesan bahasa alami umumnya menerapkan analisis sentimen atau pemodelan topik sebagai dua entitas yang terpisah. Benchmark praktik saat ini menunjukkan bahwa algoritma LDA yang memproses ulasan mentah secara langsung sering kali menggabungkan kata pujian dan keluhan dalam satu topik yang sama, sehingga menurunkan nilai koherensinya secara kualitatif. Terdapat gap yang valid pada literatur saat ini: masih kurangnya implementasi filter sentimen penyaring noise (berbasis K-NN) yang terintegrasi langsung sebelum pemodelan LDA pada domain perbankan digital di Indonesia. Kebaruan penelitian ini terletak pada penggabungan kedua algoritma tersebut yang dieksekusi secara berurutan, serta penyediaan analisis kegagalan (failure analysis) terhadap ketidakmampuan pustaka standar dalam menangani bahasa slang.

### D.4. PETA JALAN PENELITIAN
Penelitian ini diawali dengan tahap pengumpulan data (scraping) dan pra-pemrosesan teks yang telah berhasil direalisasikan pada skala uji coba. Tahapan yang dikerjakan pada usulan ini adalah implementasi penuh pembobotan TF-IDF, pelatihan model klasifikasi K-NN, dan pencarian distribusi topik melalui LDA menggunakan pustaka Scikit-Learn. Tahap lanjutan yang direncanakan mencakup perancangan kamus kata henti kustom (custom dictionary) untuk menangani noise bahasa informal sebelum sistem direkomendasikan untuk tahap produksi berskala besar.

## E. METODE

### E.1. Desain Penelitian dan Unit Analisis
Penelitian ini menggunakan desain eksperimental komputasional. Unit analisisnya adalah teks ulasan pengguna aplikasi SeaBank yang merepresentasikan opini publik. Kondisi baseline yang dikaji adalah performa ekstraksi kata kunci dari LDA murni, sedangkan intervensinya adalah LDA yang difilter terlebih dahulu oleh K-NN. Outcome yang dituju adalah tingginya akurasi klasifikasi sentimen dan terbentuknya klaster keluhan yang masuk akal secara leksikal.

### E.2. Variabel, Metric, Instrumen, dan Data
Variabel independen utama dalam penelitian ini adalah penerapan algoritma K-NN sebagai filter prasyarat pemodelan. Variabel dependennya adalah kualitas topik keluhan yang dihasilkan. Metrik utama yang digunakan adalah skor akurasi (untuk evaluasi K-NN) dan observasi kualitatif terhadap kata kunci penyusun topik (untuk LDA). Instrumen penelitian berupa skrip kode Python. Sumber data bersifat sekunder, ditarik langsung dari ulasan Google Play Store.

### E.3. Skenario dan Prosedur Pengujian
Pengujian dimulai dengan mengekstraksi matriks TF-IDF dari teks bersih. Dataset dibagi menjadi data latih dan data uji dengan rasio 80:20 untuk melatih algoritma K-NN dalam membedakan ulasan positif (bintang 4-5) dan negatif (bintang 1-3). Setelah model klasifikasi terbentuk, sistem hanya akan meneruskan ulasan yang diprediksi 'negatif' ke dalam algoritma LDA. Keluaran intervensi ini (berupa deretan kata kunci topik) diamati kemasukakalannya dan dicatat waktu eksekusinya untuk mengevaluasi efisiensi beban komputasi.

### E.4. Artifact, Setup, atau Kesiapan Implementasi
Lingkungan uji (setup) berjalan pada perangkat keras komputasi lokal menggunakan bahasa pemrograman Python. Pustaka utama yang menopang arsitektur ini adalah Scikit-Learn untuk algoritma pembelajaran mesin, Sastrawi untuk pemotongan imbuhan kata (stemming), dan Pandas untuk manipulasi kerangka data. Sistem diposisikan sebagai alat uji (proof of concept) untuk memvalidasi kelayakan alur kerja penyaringan sentimen sebelum pemodelan topik keluhan.

### E.5. Teknik Analisis, Asumsi, dan Validitas
Data dianalisis dengan meninjau matriks evaluasi dari K-NN dan membedah koherensi leksikal dari kata kunci luaran LDA. Asumsi fundamental penelitian ini adalah pengguna dengan rating bintang 1 hingga 3 secara konsisten menuliskan teks bernada negatif. Ancaman validitas utama (construct validity) berasal dari kelemahan instrumen pembersih teks (Sastrawi) yang hanya mengenali Bahasa Indonesia baku. Hal ini dimitigasi dengan melaporkannya secara transparan sebagai boundary condition bahwa sistem rentan terhadap noise bahasa slang (seperti "gua", "yg", "udah") pada lingkungan media sosial.

## F. HASIL YANG DIHARAPKAN
Penelitian ini diharapkan menghasilkan arsitektur perangkat lunak hibrida (K-NN dan LDA) yang terbukti cepat dan akurat dalam menyaring sekaligus memetakan topik keluhan spesifik dari pelanggan SeaBank. Luaran utama mencakup skrip algoritma yang dapat direplikasi, publikasi laporan analisis data, serta rekomendasi teknis pembuatan Custom Stopword Dictionary untuk meningkatkan performa pemrosesan bahasa alami (NLP) pada penelitian perbankan digital di masa mendatang.

## G. JADWAL PENELITIAN
| No | Nama kegiatan | Bulan 1 | Bulan 2 | Bulan 3 | Bulan 4 | Bulan 5 | Bulan 6 | Bulan 7 | Bulan 8 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Identifikasi *gap* permasalahan (observasi awal)      |X|X| | | | | | |
| 2 | Desain eksperimen dan persiapan kuesioner SUS         | |X|X| | | | | |
| 3 | Pengumpulan data dari responden eksperimental         | | |X|X| | | | |
| 4 | Koding dan otomatisasi pra-pemrosesan data (*Python*) | | | |X|X| | | |
| 5 | Analisis skor dan eksekusi komputasi *Paired T-Test*  | | | | |X|X| | |
| 6 | Interpretasi data, validasi, dan penulisan luaran     | | | | | |X|X| |
| 7 | Penyusunan laporan penelitian dan manuskrip akhir     | | | | | | |X|X| 

## H. DAFTAR PUSTAKA
[1] Septian, Jeremy Andre, Tresna Maulana Fachrudin, and Aryo Nugroho. "Analisis sentimen pengguna Twitter terhadap polemik persepakbolaan Indonesia menggunakan pembobotan TF-IDF dan K-Nearest Neighbor." Insyst 1.1 (2019): 43-49.

[2] Nurian, Andriani. "Analisis sentimen ulasan pengguna aplikasi google play menggunakan naïve bayes." Jurnal Informatika dan Teknik Elektro Terapan 11.3s1 (2023).

[3] Vinne, Vinne, Dina Ulitia Sinurat, and Yunika Prasetianti. "Penerapan algoritma k-nearest neighbors (knn) dalam menganalisis sentimen ulasan aplikasi seabank pada google play store." Journal of Information Systems Management and Digital Business 2.2 (2025): 103-113.

[4] Puspita, Evi, Diqy Fakhrun Shiddieq, and Fikri Fahru Roji. "Pemodelan Topik pada Media Berita Online Menggunakan Latent Dirichlet Allocation (Studi Kasus Merek Somethinc): Topic Modeling on Online News Media Using Latent Diriclet Allocation (Case Study Somethinc Brand)." MALCOM: Indonesian Journal of Machine Learning and Computer Science 4.2 (2024): 481-489.

