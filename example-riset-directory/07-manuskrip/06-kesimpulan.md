## 5. KESIMPULAN DAN SARAN

### 5.1 Kesimpulan
Penelitian ini membuktikan secara empiris bahwa arsitektur komputasional hibrida yang menggabungkan algoritma klasifikasi sentimen dan pemodelan probabilistik sangat efektif untuk mengekstrak informasi keluhan pengguna pada aplikasi perbankan digital. Berdasarkan hasil pengujian sistem, ditarik tiga kesimpulan utama:
1. Ketangguhan Filter Sentimen: Algoritma K-Nearest Neighbors (K-NN) berbasis pembobotan TF-IDF pada parameter K=3 terbukti sangat andal sebagai gerbang penyaring (gatekeeper). Model ini mencatatkan tingkat akurasi klasifikasi sebesar 88,89% dengan waktu eksekusi 0,09 detik, memastikan algoritma selanjutnya hanya menerima asupan data ulasan yang benar-benar bernada negatif.
2. Spesifisitas Ekstraksi Topik: Algoritma Latent Dirichlet Allocation (LDA) berhasil menembus batasan sentimen murni dengan memetakan akar masalah usability ke dalam dua klaster spesifik. Topik pertama berkaitan dengan keluhan operasional Layanan Pelanggan (Customer Service), sedangkan topik kedua mengindikasikan adanya kendala pada antarmuka fitur Pinjaman.
3. Analisis Kegagalan (Failure Analysis): Penelitian ini memvalidasi adanya batasan sistem (boundary condition) pada fase prapemrosesan teks. Pustaka stemming dan stopword removal standar (Sastrawi) terbukti gagal mengeleminasi bahasa informal atau slang (seperti gua, udah, nya, yg). Kegagalan ini menyumbangkan noise linguistik pada jajaran probabilitas kata kunci tertinggi di hasil akhir LDA.

### 5.2 Saran dan Rekomendasi
Berdasarkan konklusi pengujian, terdapat beberapa rekomendasi taktis baik untuk pengembang aplikasi maupun praktisi Data Science:

1. Pengembangan Kamus Kustom (Secara Teknis): Bagi praktisi NLP di Indonesia, sangat direkomendasikan untuk tidak hanya bergantung pada pustaka Sastrawi saat memproses ulasan Google Play Store atau media sosial. Implementasi wajib didampingi dengan Custom Stopword Dictionary khusus bahasa gaul/slang untuk memastikan kata-kata noise tidak merusak koherensi topik model LDA.

2. Mitigasi Layanan (Secara Praktis): Bagi tim pengembang SeaBank, hasil ekstraksi topik mengindikasikan urgensi untuk segera mengevaluasi Service Level Agreement (SLA) pada pusat bantuan (Customer Service) serta merombak alur pengalaman pengguna (UX) pada halaman pengajuan pinjaman agar lebih intuitif.

### 5.3 Limitasi dan Penelitian Lanjutan
Penelitian ini berstatus proof of concept dengan batasan sampel uji coba berskala kecil (44 ulasan bersih). Meskipun cukup untuk memvalidasi arsitektur algoritma, pemodelan topik dengan jumlah data yang minim rentan terhadap pergeseran distribusi probabilitas jika dihadapkan pada jutaan baris data sekaligus.

Oleh karena itu, penelitian lanjutan sangat didorong untuk mengekspansi volume dataset di atas 1.000 ulasan ulasan guna melihat stabilitas klaster topik. Selain itu, direkomendasikan agar studi berikutnya mencoba mengkomparasi arsitektur K-NN dan LDA ini dengan model bahasa berbasis jaringan saraf tiruan (Deep Learning)—seperti arsitektur Transformer (IndoBERT)—untuk melihat apakah model mutakhir tersebut mampu memahami konteks kalimat keluhan yang penuh dengan bahasa informal secara lebih cerdas.