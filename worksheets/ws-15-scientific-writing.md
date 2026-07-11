# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Analisis Sentimen dan Pemodelan Topik Ulasan Pengguna Aplikasi SeaBank Menggunakan K-Nearest Neighbors dan Latent Dirichlet Allocation
Target  : [X] Jurnal  [ ] Konferensi  [X] Skripsi / Laporan

Section Check:
  [X] Abstract — Kombinasi K-NN dan LDA; Akurasi K-NN 88.89%; LDA menemukan 2 topik utama; Perlunya custom stopword.
  [X] Introduction — Konteks ribuan ulasan Play Store → Gap: perlunya memisahkan ulasan positif/negatif sebelum dicari topiknya → RQ performa & topik.
  [X] Related Work — Tinjauan algoritma K-NN pada teks dan penerapan LDA di sektor perbankan digital.
  [X] Method — Scraping (google-play-scraper), Preprocessing (Sastrawi), TF-IDF, K-NN (K=3, 80:20 split), dan LDA (Scikit-learn, 2 components).
  [X] Results — Tabel akurasi (88.89%), waktu komputasi (0.09s), dan daftar kata kunci untuk Topik 1 & Topik 2.
  [X] Discussion — Makna Topik 1 (Customer Service) & Topik 2 (Pinjaman), evaluasi efisiensi waktu, serta failure analysis terkait kata gaul ("gua", "udah").
  [X] Conclusion — Menjawab RQ, menyoroti keberhasilan klasifikasi, dan rekomendasi future work (Custom Stopword).

Consistency Matrix:
  [X] RQ di Introduction = RQ di Method = RQ di Conclusion
  [X] Variabel di Method = variabel di Results
  [X] Klaim di Discussion didukung data di Results
  [X] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [ ] Clarity — (Akan dievaluasi saat penyusunan draf final)
  [ ] Precision — (Akan dievaluasi saat penyusunan draf final)
  [ ] Conciseness — (Akan dievaluasi saat penyusunan draf final)
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Penelitian ini menggabungkan K-NN dan LDA untuk menganalisis ulasan aplikasi SeaBank. K-NN (akurasi 88.89%) digunakan untuk memfilter sentimen, disusul LDA yang menemukan dua keluhan utama (Customer Service & Pinjaman). Ditemukan batasan pada deteksi bahasa slang. | 200-250 |
| Introduction | Jutaan ulasan pengguna di Google Play Store sulit dianalisis secara manual. Belum banyak studi yang menggunakan K-NN sebagai filter awal sebelum LDA pada data perbankan digital. Penelitian ini bertujuan mengukur akurasi filtering K-NN dan mengidentifikasi topik keluhan dominan. | 500-700 |
| Related Work | Membahas keunggulan K-NN dalam klasifikasi teks berbasis TF-IDF. Membandingkan dengan penelitian sebelumnya yang murni menggunakan LDA tanpa memisahkan sentimen terlebih dahulu. | 700-1000 |
| Method | Menggunakan pendekatan kuantitatif. Data diambil scraping sebanyak 44 sampel (untuk uji coba), dibersihkan dengan Sastrawi, dibobotkan dengan TF-IDF, dilatih dengan K-NN (K=3, split 80:20), dan dimodelkan dengan LDA (2 komponen) via Scikit-Learn. | 800-1200 |
| Results | Model K-NN memisahkan sentimen dengan akurasi 88.89% dalam 0.09 detik. LDA mengekstrak Topik 1 (nomor, nelfon) dan Topik 2 (pinjam, tahun), namun dengan noise kata gaul (nya, gua, udah). | 500-800 |
| Discussion | Performa tinggi menunjukkan efisiensi perpaduan kedua algoritma. Namun, munculnya kata slang membuktikan bahwa library standar (Sastrawi) kurang relevan untuk teks media sosial, sehingga menurunkan koherensi topik secara kualitatif. | 600-900 |
| Conclusion | K-NN dan LDA terbukti efisien menganalisis ulasan SeaBank. Penelitian selanjutnya sangat disarankan membangun Custom Stopword Dictionary khusus bahasa Indonesia informal. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ1 (Seberapa akurat K-NN?) |✓|✓|✓|✓|✓|
| RQ2 (Apa topik keluhan LDA?) |✓|✓|✓|✓|✓|
| Metrik (Accuracy) |✓|✓|✓|✓|✓|
| Variabel (Teks Ulasan) |✓|✓|✓|✓|✓|
| Temuan: Sastrawi gagal deteksi bahasa slang |✗|✗|✓|✓|✓|

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Ditemukan inkonsistensi pada temuan "noise bahasa slang". Temuan ini muncul di Result, Discussion, dan Conclusion, tetapi di bagian Introduction dan Method sama sekali tidak disinggung tentang potensi masalah stopword atau tantangan bahasa slang.

**Tindakan perbaikan:**
> Menambahkan satu atau dua kalimat di bagian Introduction yang menyinggung bahwa "ulasan di Play Store didominasi oleh bahasa Indonesia informal/slang, yang menjadi tantangan tersendiri dalam pemrosesan teks."

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Hasil dari algoritma ini lumayan bagus. Performa programnya naik dan waktunya cepet banget saat dijalankan di laptop. Tapi, ada kata-kata aneh yang keluar di topik yang bikin hasilnya agak kurang pas dilihat.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | "lumayan bagus" dan "cepet banget" sangat ambigu dan tidak ilmiah. | Ubah menjadi deskripsi spesifik tentang akurasi dan waktu. |
| Precision | "Performa programnya naik" tidak jelas mengacu pada matriks apa. "Kata-kata aneh" bukan istilah teknis. | Ganti dengan "akurasi klasifikasi" dan "noise linguistik/kata slang". |
| Conciseness | "saat dijalankan di laptop" adalah informasi yang tidak perlu (redundant). | Dihapus. |

**Paragraf setelah perbaikan:**
> Model gabungan ini menunjukkan performa yang sangat baik, di mana K-NN mencapai akurasi klasifikasi sebesar 88.89% dengan waktu komputasi hanya 0.09 detik. Kendati demikian, hasil pemodelan topik pada LDA masih memunculkan noise linguistik (seperti kata "nya", "gua", dan "udah") akibat ketidakmampuan library stopword baku dalam mendeteksi bahasa informal.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset ibarat membuat laporan kegiatan (hanya menceritakan apa yang dilakukan dari A sampai Z). Sebaliknya, menulis sebagai "argumen" berarti mengikat setiap bab dengan benang merah yang kuat—dimulai dari masalah, dibuktikan lewat hasil (data 88.89%), lalu dijawab di kesimpulan.
> Mengubah urutan penulisan dengan memulai dari Method & Results sangat membantu memecahkan writer's block. Karena hasil asli eksperimen (akurasi tinggi, masalah kata slang) sudah terlihat secara objektif terlebih dahulu, penulisan Discussion menjadi lebih tajam. Pada akhirnya, Introduction bisa ditulis paling akhir untuk membingkai narasi awal agar benar-benar cocok dengan temuan di garis akhir.
