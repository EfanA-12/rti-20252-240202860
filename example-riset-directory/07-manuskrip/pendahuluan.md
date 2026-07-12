# 02-pendahuluan

Draf bab pendahuluan naskah ilmiah.

---

## 1.1 Latar Belakang

Digitalisasi perbankan telah mengubah cara masyarakat melakukan transaksi keuangan, salah satunya ditandai dengan hadirnya aplikasi bank digital seperti SeaBank. Kemudahan akses melalui telepon pintar membuat aplikasi ini memiliki jutaan pengguna aktif. Sebagai platform yang didistribusikan melalui Google Play Store, SeaBank menerima ribuan ulasan (reviews) dari pengguna setiap harinya. Ulasan ini memuat berbagai tanggapan esensial, mulai dari apresiasi fitur hingga keluhan terkait usability (kemudahan dan kenyamanan penggunaan antarmuka), seperti masalah saat login, kegagalan pemuatan halaman (loading), ketidakakuratan menu transaksi, hingga kendala layanan pelanggan.

Meskipun ulasan pengguna menyimpan wawasan (insight) yang sangat berharga bagi tim pengembang untuk melakukan perbaikan sistem (bug fixing), volume data tekstual yang masif menyulitkan proses ekstraksi informasi jika dilakukan secara manual. Di industri rekayasa perangkat lunak, penumpukan keluhan tak terbaca sering kali menjadi akar masalah lambatnya respons pengembang, yang pada akhirnya berdampak pada penurunan tingkat kepuasan dan retensi pengguna.

Untuk mengatasi masalah tersebut, pendekatan Natural Language Processing (NLP) seperti Topic Modeling sering digunakan. Salah satu algoritma pemodelan topik yang paling populer adalah Latent Dirichlet Allocation (LDA). Namun, penerapan benchmark praktik saat ini menunjukkan adanya celah (gap) penelitian: algoritma LDA yang secara langsung memproses ulasan mentah sering kali mencampuradukkan kata-kata pujian (sentimen positif) dengan kata-kata keluhan (sentimen negatif) di dalam satu klaster topik yang sama. Hal ini menyebabkan topik yang dihasilkan menjadi ambigu dan menurunkan nilai koherensinya secara kualitatif. Mengetahui bahwa pengguna marah tidaklah cukup; pengembang perlu mengetahui secara pasti "topik usability apa" yang membuat pengguna mengeluh.

Berdasarkan celah tersebut, penelitian ini mengusulkan sebuah pendekatan arsitektur hibrida. Sebelum teks ulasan dimodelkan ke dalam LDA, sistem akan difilter terlebih dahulu menggunakan algoritma K-Nearest Neighbors (K-NN) yang dioptimasi dengan pembobotan Term Frequency-Inverse Document Frequency (TF-IDF). K-NN dipilih karena ketangguhannya dalam mengklasifikasikan teks berdimensi tinggi secara efisien. Dengan menyaring dan membuang ulasan bersentimen positif terlebih dahulu, algoritma LDA dipastikan hanya akan menerima asupan data murni bernada keluhan (negatif). Selain itu, ulasan pada media sosial sangat identik dengan bahasa tidak baku (slang), sehingga penelitian ini juga akan menyoroti batasan (boundary condition) dari alat pra-pemrosesan teks dalam menangani noise bahasa informal.

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian ini adalah sebagai berikut:

1. Seberapa besar tingkat akurasi algoritma K-Nearest Neighbors (K-NN) dalam mengklasifikasikan dan memfilter sentimen ulasan pengguna aplikasi SeaBank?
2. Apa saja topik utama keluhan usability yang berhasil diekstrak oleh algoritma Latent Dirichlet Allocation (LDA) setelah data ulasan difilter menggunakan K-NN?
3. Bagaimana dampak keberadaan bahasa informal (slang) pada ulasan Google Play Store terhadap hasil koherensi topik yang diekstrak, dan bagaimana analisis kegagalannya (failure analysis) terhadap pustaka prapemrosesan teks standar?

## 1.3 Tujuan Penelitian

1. Mengimplementasikan dan mengukur tingkat akurasi algoritma K-Nearest Neighbors (K-NN) berbasis pembobotan TF-IDF sebagai filter awal pemisah sentimen ulasan aplikasi SeaBank.
2. Mengekstraksi dan mengidentifikasi klaster topik keluhan usability pengguna aplikasi SeaBank secara spesifik menggunakan pemodelan Latent Dirichlet Allocation (LDA).
3. Menemukan batasan sistem (boundary condition) dan merumuskan analisis kegagalan (failure analysis) terkait kelemahan pustaka stopword standar (Sastrawi) dalam menangani bahasa slang khas media sosial Indonesia.

## 1.4 Kontribusi Penelitian
1. Kontribusi Teoretis (Keilmuan)
Penelitian ini memperkaya literatur di bidang pemrosesan bahasa alami (NLP) dengan membuktikan efektivitas penggabungan algoritma klasifikasi (K-NN) dan pemodelan probabilistik (LDA) yang dijalankan secara sekuensial (berurutan). Selain itu, laporan temuan terkait noise leksikal pada tahap Failure Analysis memberikan pijakan empiris bagi penelitian selanjutnya mengenai urgensi pengembangan Custom Stopword Dictionary untuk penanganan bahasa informal di Indonesia.

2. Kontribusi Praktis
Secara praktis, model komputasi yang dihasilkan dari penelitian ini dapat diadopsi oleh tim pengembang aplikasi SeaBank (dan perbankan digital lainnya) sebagai alat penyaring (filtering tool) yang sangat ringan (waktu komputasi di bawah 1 detik). Alat ini memungkinkan developer untuk secara instan melihat topik keluhan usability yang mendesak (seperti masalah layanan Customer Service atau fitur antarmuka Pinjaman), sehingga mempercepat proses bug fixing dan evaluasi pengalaman pengguna (UI/UX).

## 1.5 Batasan Masalah

1. Sumber Data: Data yang digunakan sebagai unit analisis adalah ulasan tekstual dan rating bintang dari pengguna aplikasi perbankan digital SeaBank, yang dikumpulkan (scraping) secara spesifik dari platform distribusi Google Play Store.
2. Fokus Sentimen: Penelitian ini memfokuskan pemodelan topik hanya pada ulasan yang terindikasi bersentimen negatif (diasumsikan berasal dari rating 1 hingga 3 bintang) guna secara spesifik menggali keluhan terkait usability aplikasi dan kendala layanan.
3. Algoritma dan Parameter Eksperimen:
- Proses klasifikasi sentimen menggunakan algoritma K-Nearest Neighbors (K-NN) yang didukung oleh ekstraksi fitur dan pembobotan matriks TF-IDF. Skema pengujian dibatasi pada pembagian data latih dan data uji sebesar 80:20, dengan nilai parameter ketetanggaan terdekat K=3.
- Proses pemodelan topik menggunakan algoritma Latent Dirichlet Allocation (LDA) berbasis pustaka Scikit-Learn, dengan target pencarian klaster dibatasi pada 2 topik utama (n_components = 2).
4. Alat Prapemrosesan dan Hambatan Bahasa: Teks yang diolah berfokus pada ulasan berbahasa Indonesia. Proses pemotongan imbuhan (stemming) dan penghapusan kata hubung (stopword removal) murni mengandalkan pustaka baku Sastrawi. Ketiadaan kamus kustom (custom dictionary) menyebabkan lolosnya bahasa tidak baku/gaul (seperti "yg", "gua", "udah") ke dalam sistem, yang mana diasumsikan sebagai noise bawaan dan akan dibahas pada porsi Failure Analysis.
5. Skala Pengujian: Implementasi eksperimen komputasi pada penelitian ini bersifat purwarupa (proof of concept) yang dijalankan pada sampel data uji coba terbatas (44 data ulasan bersih). Pengujian ini dirancang untuk memvalidasi efisiensi waktu komputasi dan kelayakan arsitektur sistem hibrida sebelum direkomendasikan untuk produksi berskala masif.