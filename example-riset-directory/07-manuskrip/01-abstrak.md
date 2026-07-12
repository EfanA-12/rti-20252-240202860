# 01-abstrak

Draf abstrak naskah ilmiah dua bahasa (Bahasa Indonesia dan English).

---

## Abstrak (Bahasa Indonesia)

**Abstrak** Ulasan pengguna pada aplikasi perbankan digital seperti SeaBank memuat wawasan penting terkait keluhan usability, namun volume data yang masif menyulitkan tim pengembang untuk melakukan analisis secara manual. Pemodelan topik konvensional sering kali menghasilkan klaster kata yang bias akibat tercampurnya sentimen positif dan negatif. Penelitian ini mengusulkan pendekatan komputasional hibrida dengan menggunakan algoritma K-Nearest Neighbors (K-NN) sebagai penyaring sentimen awal sebelum mengekstraksi topik keluhan menggunakan Latent Dirichlet Allocation (LDA). Eksperimen dilakukan menggunakan ulasan dari Google Play Store yang diproses melalui tahapan pembersihan reguler, stopword removal (Sastrawi), pembobotan TF-IDF, dan pembagian data uji latih 80:20. Hasil pengujian menunjukkan bahwa K-NN (K=3) berhasil membedakan sentimen dengan tingkat akurasi mencapai 88,89% dan waktu komputasi yang sangat ringan, yakni 0,09 detik. Algoritma LDA kemudian berhasil mengekstrak dua topik keluhan utama secara spesifik: masalah layanan pelanggan (Customer Service) dan keluhan fitur pengajuan pinjaman. Melalui proses failure analysis, ditemukan pula batasan sistem (boundary condition) berupa ketidakmampuan pustaka Sastrawi dalam mendeteksi dan menghapus bahasa informal (seperti "gua", "udah", "yg"). Penelitian ini menyimpulkan bahwa kombinasi K-NN dan LDA sangat efisien sebagai gerbang penyaring sebelum pemodelan topik, serta merekomendasikan perancangan Custom Stopword Dictionary khusus bahasa slang untuk optimalisasi pemrosesan teks media sosial di masa mendatang.  

**Kata Kunci:** Analisis Sentimen, K-Nearest Neighbors, Latent Dirichlet Allocation, SeaBank, Usability, Failure Analysis.

---

## Abstract (English)

**Abstract** User reviews on digital banking applications such as SeaBank contain crucial insights regarding usability complaints, yet the massive volume of data complicates manual analysis for developers. Conventional topic modeling often produces biased word clusters due to the mixing of positive and negative sentiments. This study proposes a hybrid computational approach utilizing the K-Nearest Neighbors (K-NN) algorithm as an initial sentiment filter before extracting complaint topics using Latent Dirichlet Allocation (LDA). The experiment was conducted using Google Play Store reviews processed through regular cleansing, stopword removal (Sastrawi), TF-IDF weighting, and an 80:20 train-test data split. Test results demonstrated that K-NN (K=3) successfully distinguished sentiments with an accuracy rate of 88.89% and a highly efficient computational time of 0.09 seconds. Subsequently, the LDA algorithm successfully extracted two specific main complaint topics: Customer Service issues and loan application features. Through failure analysis, a system boundary condition was also discovered regarding the inability of the Sastrawi library to detect and remove informal language (such as "gua", "udah", "yg"). This study concludes that the combination of K-NN and LDA is highly efficient as a filtering gateway before topic modeling and recommends the design of a Custom Stopword Dictionary specifically for slang to optimize social media text processing in the future.

**Keywords:** Sentiment Analysis, K-Nearest Neighbors, Latent Dirichlet Allocation, SeaBank, Usability, Failure Analysis.