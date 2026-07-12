Analisis Sentimen dan Ekstraksi Topik Keluhan Usability pada Aplikasi SeaBank Menggunakan Algoritma K-NN dan Latent Dirichlet Allocation (LDA)

## ABSTRAK (ID)
Ulasan pengguna pada aplikasi perbankan digital seperti SeaBank memuat wawasan penting terkait keluhan usability, namun volume data yang masif menyulitkan analisis manual. Pemodelan topik konvensional sering kali menghasilkan klaster kata yang bias akibat tercampurnya sentimen positif dan negatif. Penelitian ini mengusulkan pendekatan komputasional hibrida dengan menggunakan algoritma K-Nearest Neighbors (K-NN) sebagai penyaring sentimen awal sebelum mengekstraksi topik keluhan menggunakan Latent Dirichlet Allocation (LDA). Eksperimen dilakukan menggunakan ulasan dari Google Play Store yang diproses melalui stopword removal (Sastrawi), pembobotan TF-IDF, dan pembagian data uji latih 80:20. Hasil pengujian menunjukkan bahwa K-NN (K=3) berhasil membedakan sentimen dengan akurasi 88,89% dalam waktu 0,09 detik. Algoritma LDA kemudian berhasil mengekstrak dua topik keluhan spesifik: masalah layanan Customer Service dan keluhan fitur Pinjaman. Melalui proses failure analysis, ditemukan pula ketidakmampuan pustaka Sastrawi dalam mendeteksi bahasa informal ("gua", "udah", "yg"). Kombinasi K-NN dan LDA terbukti efisien sebagai gerbang penyaring sebelum pemodelan topik.

Kata Kunci: Analisis Sentimen, K-Nearest Neighbors, Latent Dirichlet Allocation, SeaBank, Usability.

---

## ABSTRACT (EN)
User reviews on digital banking applications such as SeaBank contain crucial insights regarding usability complaints, yet the massive volume of data complicates manual analysis. Conventional topic modeling often produces biased word clusters due to the mixing of positive and negative sentiments. This study proposes a hybrid computational approach utilizing the K-Nearest Neighbors (K-NN) algorithm as an initial sentiment filter before extracting complaint topics using Latent Dirichlet Allocation (LDA). The experiment was conducted using Google Play Store reviews processed through stopword removal (Sastrawi), TF-IDF weighting, and an 80:20 train-test split. Test results demonstrated that K-NN (K=3) successfully distinguished sentiments with an accuracy of 88.89% in 0.09 seconds. The LDA algorithm subsequently extracted two specific complaint topics: Customer Service issues and Loan feature complaints. Through failure analysis, the inability of the Sastrawi library to detect informal language ("gua", "udah", "yg") was discovered. The combination of K-NN and LDA proves efficient as a filtering gateway before topic modeling.

Keywords: Sentiment Analysis, K-Nearest Neighbors, Latent Dirichlet Allocation, SeaBank, Usability.

## 1. PENDAHULUAN

### 1.1 Latar Belakang
Digitalisasi perbankan telah mengubah cara masyarakat melakukan transaksi keuangan, ditandai dengan hadirnya aplikasi bank digital seperti SeaBank. Sebagai platform yang didistribusikan melalui Google Play Store, SeaBank menerima ribuan ulasan dari pengguna setiap harinya. Ulasan ini memuat berbagai tanggapan esensial terkait usability (kemudahan penggunaan), seperti masalah login, kegagalan pemuatan halaman, hingga kendala layanan pelanggan.

Meskipun menyimpan wawasan berharga bagi tim pengembang untuk perbaikan sistem, volume data tekstual yang masif menyulitkan proses ekstraksi manual. Pendekatan Natural Language Processing (NLP) seperti Latent Dirichlet Allocation (LDA) sering digunakan. Namun, algoritma LDA yang memproses ulasan mentah sering mencampuradukkan sentimen positif dan negatif dalam satu klaster topik, menyebabkan ambiguitas. Berdasarkan celah tersebut, penelitian ini mengusulkan arsitektur hibrida: menyaring ulasan menggunakan K-Nearest Neighbors (K-NN) berbasis pembobotan TF-IDF sebelum dimodelkan oleh LDA, sehingga memastikan LDA hanya menerima asupan data murni bernada keluhan.

### 1.2 Rumusan Masalah
1. Seberapa besar tingkat akurasi algoritma K-NN dalam mengklasifikasikan sentimen ulasan pengguna aplikasi SeaBank?
2. Apa saja topik utama keluhan usability yang diekstrak oleh algoritma LDA setelah difilter menggunakan K-NN?
3. Bagaimana kelemahan pustaka pra-pemrosesan teks (Sastrawi) dalam menangani bahasa slang memengaruhi hasil pemodelan?

### 1.3 Tujuan Penelitian
Penelitian ini bertujuan mengimplementasikan K-NN sebagai filter pemisah sentimen, mengekstraksi klaster topik keluhan usability menggunakan LDA, dan merumuskan analisis kegagalan (failure analysis) terkait kelemahan pustaka stopword standar dalam menangani bahasa informal.

### 1.4 Kontribusi Penelitian
Secara teoretis, penelitian ini membuktikan efektivitas penggabungan K-NN dan LDA secara sekuensial serta memberikan pijakan empiris mengenai urgensi Custom Stopword Dictionary. Secara praktis, model komputasi ini dapat diadopsi oleh pengembang aplikasi perbankan sebagai alat penyaring topik keluhan otomatis yang cepat dan efisien.

## 2. TINJAUAN PUSTAKA

### 2.1 Analisis Sentimen dan K-Nearest Neighbors (K-NN)
Analisis sentimen mengevaluasi pendapat dan sentimen pengguna berdasarkan data teks. Algoritma K-NN menjadi metode populer karena kesederhanaan implementasinya berbasis jarak antar data latih dan data uji. Agar dapat diproses, teks diubah menjadi angka menggunakan Term Frequency-Inverse Document Frequency (TF-IDF), yang menghitung relevansi kata secara relatif dalam kumpulan dokumen.

### 2.2 Latent Dirichlet Allocation (LDA)
LDA adalah metode unsupervised machine learning berbasis probabilistik yang menampilkan topik menggunakan probabilitas dari setiap kata. Metode ini membantu menggambarkan dokumen teks menjadi struktur tersembunyi (latent) yang jauh lebih rapi dan dapat diinterpretasikan secara leksikal.

### 2.3 Related Work (Penelitian Terdahulu)
Penelitian terdahulu sering memisahkan klasifikasi dan ekstraksi topik. Vinne dkk. (2025) menerapkan K-NN pada SeaBank namun hanya mencapai akurasi kelas negatif 42%. Nurian & Sari (2023) menggunakan Naive Bayes pada aplikasi DANA dengan akurasi 85%, namun terbatas pada pelabelan opini tanpa ekstraksi subjek. Puspita dkk. (2024) menggunakan LDA untuk mengekstrak topik kosmetik, namun tanpa filter sentimen, model tersebut rentan bias. Penelitian ini menjembatani celah tersebut dengan menjadikan K-NN sebagai gerbang filter sentimen sebelum LDA.

## 3. METODOLOGI PENELITIAN

### 3.1 Arsitektur Sistem Pengujian
Penelitian ini menggunakan desain eksperimental komputasional. Arsitektur dibangun secara sekuensial:

1. Scraping: Menarik ulasan mentah SeaBank dari Google Play Store.
2. Preprocessing: Case folding, cleansing (Regex), stopword removal, dan stemming (Sastrawi).
3. Ekstraksi Fitur: Pembobotan matriks TF-IDF.
4. Klasifikasi K-NN: Melatih model dengan Scikit-Learn untuk membedakan sentimen positif dan negatif.
5. Pemodelan LDA: Mengelompokkan teks yang dilabeli "Negatif" oleh K-NN menjadi klaster topik keluhan.

### 3.2 Variabel dan Prosedur Eksperimen
Eksperimen menggunakan 44 ulasan bersih yang dibagi dengan rasio 80% data latih dan 20% data uji. Parameter dikunci pada K=3 untuk K-NN dan n_components=2 untuk pencarian LDA.

### 3.3 Metode Evaluasi
Kinerja K-NN dievaluasi menggunakan Confusion Matrix untuk mendapatkan persentase akurasi. Kualitas LDA dievaluasi melalui human judgement atas probabilitas distribusi kata penyusun klaster. Anomali bahasa informal diidentifikasi melalui Failure Analysis.

## 4. HASIL DAN PEMBAHASAN

### 4.1 Performa Klasifikasi K-Nearest Neighbors (K-NN)
Hasil evaluasi matriks konfusi dengan parameter K=3 menunjukkan tingkat akurasi klasifikasi sentimen mencapai 88,89%. Model ini terbukti sangat ringan secara komputasional, menyelesaikan proses teks hanya dalam waktu 0,09 detik. Hal ini menegaskan kelayakan K-NN sebagai prapengondisi (pre-condition) yang tangguh.

### 4.2 Ekstraksi Topik Menggunakan LDA
LDA secara eksklusif memproses ulasan "Negatif" dan mengidentifikasi dua klaster keluhan utama:

- Topik 1 (Layanan Customer Service): Didominasi kata kunci nomor, nelfon, nya, gua, udah. Klaster ini merepresentasikan kendala operasional saat menghubungi pusat bantuan.
- Topik 2 (Kendala Pinjaman): Didominasi kata kunci pinjam, tahun, dapat, yg, baru. Mengindikasikan masalah teknis pada antarmuka layanan pengajuan pinjaman digital.

### 4.3 Analisis Kegagalan (Failure Analysis)
Kemunculan kata-kata tidak baku (gua, udah, yg) di puncak probabilitas kata membuktikan batasan pustaka stemmer Sastrawi. Karena ulasan didominasi bahasa slang, sistem gagal mengidentifikasi kata tersebut sebagai noise. Ini mengindikasikan urgensi penggunaan Custom Stopword Dictionary pada penelitian NLP masa depan.

## 5. KESIMPULAN DAN SARAN

### 5.1 Kesimpulan
Pendekatan hibrida ini terbukti efektif. K-NN sangat andal sebagai gerbang penyaring dengan akurasi 88,89% (0,09 detik). LDA sukses memetakan akar masalah usability menjadi keluhan Customer Service dan fitur Pinjaman tanpa terdistraksi sentimen pujian. Di sisi lain, teridentifikasi batasan pustaka standar Sastrawi yang gagal mengeliminasi noise bahasa informal.

### 5.2 Saran
Direkomendasikan bagi praktisi Data Science untuk menyusun Custom Stopword Dictionary khusus bahasa slang Indonesia. Bagi pengembang SeaBank, temuan ini dapat dijadikan rujukan evaluasi pada alur UX fitur pinjaman dan respons layanan pelanggan.

DAFTAR PUSTAKA

[1] Septian, Jeremy Andre, Tresna Maulana Fachrudin, and Aryo Nugroho. "Analisis sentimen pengguna Twitter terhadap polemik persepakbolaan Indonesia menggunakan pembobotan TF-IDF dan K-Nearest Neighbor." Insyst 1.1 (2019): 43-49.

[2] Nurian, Andriani. "Analisis sentimen ulasan pengguna aplikasi google play menggunakan naïve bayes." Jurnal Informatika dan Teknik Elektro Terapan 11.3s1 (2023).

[3] Vinne, Vinne, Dina Ulitia Sinurat, and Yunika Prasetianti. "Penerapan algoritma k-nearest neighbors (knn) dalam menganalisis sentimen ulasan aplikasi seabank pada google play store." Journal of Information Systems Management and Digital Business 2.2 (2025): 103-113.

[4] Puspita, Evi, Diqy Fakhrun Shiddieq, and Fikri Fahru Roji. "Pemodelan Topik pada Media Berita Online Menggunakan Latent Dirichlet Allocation (Studi Kasus Merek Somethinc): Topic Modeling on Online News Media Using Latent Diriclet Allocation (Case Study Somethinc Brand)." MALCOM: Indonesian Journal of Machine Learning and Computer Science 4.2 (2024): 481-489.