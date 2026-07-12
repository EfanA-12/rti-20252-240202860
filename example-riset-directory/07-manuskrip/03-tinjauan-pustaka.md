# 03-tinjauan-pustaka

Draf bab tinjauan pustaka naskah ilmiah.

---

## 2.1 Analisis Sentimen, Pembobotan TF-IDF, dan K-Nearest Neighbors (K-NN)

Analisis sentimen adalah jenis penelitian komputasi yang bertujuan untuk mengevaluasi pendapat, penilaian, dan perasaan pengguna berdasarkan data ulasan. Teknik ini umumnya mengkategorikan ulasan menjadi sentimen positif, negatif, atau netral. Dalam pemrosesan teks, algoritma K-Nearest Neighbors (K-NN) menjadi metode yang populer karena keunggulannya dalam kesederhanaan implementasi. K-NN merupakan algoritma klasifikasi berbasis jarak yang bekerja dengan menentukan sejumlah tetangga terdekat (K) dari data uji berdasarkan data latih yang ada.  Sebelum diklasifikasikan oleh K-NN, teks harus diubah menjadi angka menggunakan teknik Term Frequency-Inverse Document Frequency (TF-IDF). TF-IDF adalah teknik text mining yang digunakan untuk mengetahui relevansi kata dengan menghitung frekuensi relatif kata tersebut dalam sebuah dokumen dan di seluruh kumpulan dokumen. Proses ini mentransformasi data tekstual ke dalam data numerik sehingga pembobotan pada tiap fitur dapat dilakukan.  

## 2.2 Pemodelan Topik dan Latent Dirichlet Allocation (LDA)

Topic modeling merupakan salah satu teknik unsupervised machine learning yang digunakan untuk menemukan tema tersembunyi dari kumpulan dokumen teks besar. Tujuan utamanya adalah untuk mengelompokkan tema-tema tersebut menjadi satu topik yang koheren.  Di dalam bidang pemodelan topik, Latent Dirichlet Allocation (LDA) adalah salah satu metode yang paling banyak digunakan karena dianggap lebih unggul dalam menghasilkan topik bermakna logis. LDA bekerja dengan menampilkan sebuah topik menggunakan probabilitas dari setiap kata, yang pada akhirnya membantu menggambarkan dokumen-dokumen teks menjadi struktur yang jauh lebih rapi dan dapat diinterpretasikan.  

## 2.3 Usability pada Aplikasi Mobile Banking

Usability merujuk pada sejauh mana sebuah produk dapat digunakan oleh pengguna tertentu untuk mencapai tujuan dengan efektivitas, efisiensi, dan kepuasan pada konteks penggunaannya. Pada aplikasi mobile banking seperti SeaBank, ulasan di Google Play Store menjadi tolok ukur utama. Ulasan positif umumnya menyoroti kemudahan penggunaan aplikasi. Sebaliknya, ulasan negatif sering kali memuat keluhan terkait usability, seperti waktu pemuatan aplikasi yang lama dan informasi transaksi yang tidak akurat. Keluhan-keluhan inilah yang menjadi target ekstraksi informasi pada penelitian ini.  

## 2.4 Penelitian Terdahulu (Related Work) dan Celah Penelitian
Riset di bidang klasifikasi teks dan pemodelan topik telah banyak dilakukan, namun sering kali berjalan pada ruang lingkup yang terpisah. Pada domain klasifikasi sentimen, Vinne dkk. mengimplementasikan K-NN pada ulasan aplikasi SeaBank dan mencapai tingkat akurasi 62,5%. Namun, model tersebut memiliki kinerja yang rendah dalam memprediksi kelas negatif (hanya 42%). Penelitian lain oleh Nurian & Sari menggunakan Naive Bayes untuk aplikasi dompet digital DANA dan mencapai akurasi tinggi sebesar 85%. Septian dkk. juga membuktikan ketangguhan K-NN dalam menganalisis sentimen Twitter dengan akurasi 79,99% pada nilai K=23. Ketiga studi ini konsisten menempatkan fokus pada pemilahan sentimen, tanpa mengekstrak akar permasalahan secara lebih mendalam.  
Di sisi lain, penelitian mengenai pemodelan topik dilakukan secara independen. Puspita dkk. mengaplikasikan LDA pada berita online merek Somethinc dan berhasil mengekstrak 6 topik utama yang dievaluasi dengan nilai coherence. Akan tetapi, algoritma LDA dalam penelitian tersebut langsung "menelan" data mentah tanpa adanya tahapan filter polaritas sentimen terlebih dahulu.  
Pola yang konsisten muncul dari studi-studi di atas adalah: riset sentimen berhenti pada sekadar mengetahui pengguna "suka atau tidak suka", sementara riset LDA rentan bias karena mencampuradukkan teks positif dan negatif dalam satu model ruang vektor. Belum ada satu pun studi yang menyatukan kedua sisi ini secara sekuensial, yakni menguji langsung integrasi K-NN sebagai pra-penyaring sentimen negatif sebelum diekstrak oleh LDA pada konteks keluhan usability aplikasi perbankan digital.

### Tabel 1. Ringkasan Peta Literatur

| Peneliti (Tahun) | Metode & Konteks | Hasil Utama | Celah yang Ditemukan |
|---|---|---|---|
| Vinne, dkk. (2025) [1] | K-NN, TF-IDF, Ulasan Google Play Store SeaBank | Akurasi mencapai 62,5% | Akurasi kelas negatif rendah dan belum ada tindak lanjut ekstraksi topik keluhan   |
|Nurian & Sari (2023) [2] |Naive Bayes Classifier, TF-IDF, Ulasan DANA | Akurasi klasifikasi mencapai 85% | Terbatas pada pelabelan opini, tidak mengidentifikasi subjek spesifik keluhan |
| Septian, dkk. (2019) [3] | K-NN, TF-IDF, Data tweet Twitter terkait sepak bola | Akurasi 79,99% pada parameter K=23 | Hanya berfungsi sebagai alat pengklasifikasi sentimen tunggal tanpa integrasi algoritma pemodelan lanjutan |
| Puspita, dkk. (2024) [4] | LDA, Evaluasi Nilai Coherence, Data berita online | Menghasilkan 6 topik dengan nilai coherence 0.404 | LDA berisiko mencampur kata positif dan negatif karena tidak didahului tahapan filter sentimen |


**Gap utama yang diangkat:** Belum ada penelitian yang menguji efektivitas penggabungan K-NN sebagai gerbang pemfilter (gatekeeper) khusus sentimen negatif sebelum teks diteruskan ke algoritma LDA untuk ekstraksi topik usability pada aplikasi perbankan digital.

## 2.5 Landasan Teori Statistik: Paired Samples T-Test

*Karena penelitian ini merupakan pemrosesan Machine Learning, evaluasi tidak menggunakan uji statistik probabilitas klasik, melainkan menggunakan metrik evaluasi klasifikasi dan observasi pemodelan.
- Confusion Matrix: Evaluasi kinerja algoritma klasifikasi (K-NN) diukur menggunakan matriks konfusi yang membandingkan prediksi model dengan label sebenarnya. Tolok ukur utama yang dinilai meliputi akurasi, presisi, recall, dan f-measure. Akurasi adalah rasio jumlah prediksi yang benar terhadap total keseluruhan data.
- Evaluasi LDA (Human Judgement & Coherence): Untuk algoritma LDA, evaluasi mengandalkan pendekatan penilaian manusia (human judgement) dan nilai coherence. Evaluasi ini berfungsi untuk melihat sejauh mana topik yang dihasilkan (berdasarkan distribusi kata-kata dengan probabilitas tertinggi) dapat direpresentasikan secara logis dan saling berkaitan satu sama lain menurut pemahaman komprehensif manusia.  