# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (artefak dibuat sebagai instrumen pengujian hipotesis, bukan tujuan akhir).

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Efan Aryanto Adli
Tanggal          : 12 April 2026

1. Ketika membaca klaim "metode X 95% akurat" (atau dalam konteks UI/UX: "Aplikasi X memiliki Usability 95%"):
   - Pertanyaan pertama saya: Siapa populasi responden yang diuji, dan apakah metrik pengukuran yang digunakan sudah memenuhi standar industri yang valid?
   - Data yang dibutuhkan untuk verifikasi: Profil demografi responden, jumlah sampel (N), dan validitas/reliabilitas instrumen kuesioner yang digunakan.

2. Posisi paradigma:
   - Pendekatan: [X] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Kualitas dan kelayakan sebuah perangkat lunak dapat diukur secara objektif dan empiris menggunakan kerangka kerja baku (seperti ISO/IEC 25010 atau System Usability Scale) melalui pendekatan kuantitatif.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Bahwa skor rata-rata (mean) yang tinggi otomatis berarti seluruh fitur di dalam sistem berjalan sempurna tanpa ada celah kritis (misalnya pada aspek keamanan).
   - Sumber bias potensial: Sampling bias; kuesioner hanya diisi oleh pengguna yang sudah terbiasa dengan teknologi cerdas (tech-savvy), sehingga mengabaikan keluhan pengguna awam.
   - Langkah mitigasi: Melakukan uji validitas dan reliabilitas pada instrumen, serta memastikan sebaran responden mencakup berbagai rentang usia dan tingkat literasi digital.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Skor mentah dari kuesioner pengguna atau log eror sistem.
   - Batasan yang diakui sejak awal: Evaluasi hanya mencakup modul tertentu dari sistem dan tidak merepresentasikan kualitas pemeliharaan (maintainability) jangka panjang di level kode sumber (source code).
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

**Paper yang dipilih:**
> Judul: Evaluasi Kualitas Aplikasi Keuangan UMKM Menggunakan ISO/IEC 25010
> Penulis (Tahun): Nurqamarani, dkk. (Jurnal REMIK - Riset dan E-Jurnal Manajemen Informatika Komputer, 2023)
> Link : https://www.jurnal.polgan.ac.id/index.php/remik/article/view/15072/3427

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Menyebarkan instrumen kuesioner dengan 17 butir pernyataan (Skala Likert 1-5) kepada para pengguna aplikasi keuangan UMKM. | Sampling bias: Kuesioner mungkin didistribusikan secara online, sehingga UMKM tradisional yang tidak memiliki akses internet memadai tidak terwakili dalam sampel. |
| Data → Processing | Mengonversi jawaban kuesioner kualitatif (Sangat Setuju - Sangat Tidak Setuju) menjadi skor persentase kuantitatif. | Translation Error: Asumsi bahwa jarak emosional antara "Setuju" (4) dan "Sangat Setuju" (5) memiliki rentang interval matematis yang persis sama. |
| Processing → Analysis | Mengkategorikan skor rata-rata Functional Suitability sebesar 82,00% ke dalam kategori "Sangat Baik". | Aggregation Bias: Menggabungkan semua fitur menjadi satu skor rata-rata dapat menyembunyikan fakta jika ada satu fitur krusial yang sebenarnya sering gagal saat digunakan. |
| Analysis → Inference | Menyimpulkan bahwa aplikasi tersebut telah memenuhi kelayakan fungsional untuk pencatatan transaksi UMKM karena tidak ada skor subkarakteristik di bawah 78%. | Construct Validity threat: Kelayakan aplikasi di dunia nyata seringkali juga dipengaruhi oleh faktor eksternal (seperti dukungan layanan pelanggan), yang tidak selalu tercakup penuh dalam kuesioner standar. |
| Inference → Knowledge | Menetapkan aplikasi tersebut sebagai standar aplikasi pencatatan keuangan yang ideal untuk UMKM secara umum. | Overgeneralization: Kebutuhan UMKM di sektor manufaktur sangat berbeda dengan UMKM retail/jasa; aplikasi ini mungkin hanya ideal untuk model bisnis retail sederhana. |

**Distorsi paling besar di tahap:** Reality → Data

**Dua distorsi spesifik yang teridentifikasi:**
1. Bias Populasi Responden: Pengguna yang bersedia meluangkan waktu mengisi kuesioner evaluasi biasanya adalah power-user atau mereka yang sudah memiliki opini kuat terhadap aplikasi, sehingga data yang terkumpul kurang merepresentasikan pengguna pasif.
2. Ilusi Skor Rata-rata: Skor akhir di atas 80% pada evaluasi ISO 25010 bisa menciptakan ilusi kesempurnaan sistem, padahal di dalam operasional nyata, bug kecil pada sistem laporan keuangan bisa berdampak fatal pada arus kas UMKM.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Dalam riset evaluasi sistem TI, responden yang memberikan nilai ekstrem (sangat rendah) adalah bentuk feedback yang valid. Menghapus data mereka agar sistem terlihat "sudah baik" adalah tindakan manipulasi data. |
| Transparansi | Outlier justru bisa menjadi indikator adanya edge-case (kasus khusus) pada sistem—misalnya antarmuka (UI) yang tidak kompatibel di perangkat lama. Peneliti harus menganalisis penyebab anomali tersebut, bukan membuangnya. |
| Peer review | Reviewer akan mempertanyakan metodologi pembersihan data jika rentang nilai yang disajikan terlihat tidak alamiah atau terlalu seragam untuk sebuah evaluasi usability. |

**Keputusan akhir dan justifikasi:**
> Data outlier tersebut harus tetap disertakan dalam pengolahan akhir. Alih-alih menghapusnya demi mengejar skor kelayakan yang tinggi, peneliti wajib melakukan penyelidikan kualitatif tambahan terhadap 3 data point tersebut. Jika nilai rendah itu disebabkan oleh error pada sistem (system failure) atau desain antarmuka yang membingungkan bagi segmen pengguna tertentu, maka hal itu adalah temuan riset yang sangat berharga (kontribusi negatif/perbaikan), bukan pengganggu yang harus disembunyikan.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Evaluasi Kualitas Perangkat Lunak pada Sistem Informasi Point of Sale (POS) untuk UMKM Menggunakan Standar ISO/IEC 25010.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 2 | 3 |
| Jenis data yang dikumpulkan | Metrik performa (waktu respon), tingkat error rate, dan skor kuesioner skala Likert untuk fungsionalitas dan keamanan. | Wawancara mendalam tentang "perasaan" kasir saat menggunakan mesin POS. | Kode program, rancangan database relasional, diagram UML. |
| Limitasi paradigma | Sulit menangkap alasan sosiologis mengapa pengguna enggan bermigrasi dari pencatatan manual ke POS digital meskipun skor efisiensi sistemnya tinggi. | Hasil tidak dapat digeneralisasi untuk mengevaluasi kelayakan teknis software di tempat lain. | Fokus pada "bagaimana membangun POS", bukan pada "apakah POS ini secara objektif berkualitas tinggi berdasarkan standar yang ada". |

**Paradigma yang dipilih:** Positivis.
**Alasan:** Riset ini bertujuan mengukur kualitas kelayakan sebuah artefak teknologi (Sistem POS) dengan menggunakan instrumen pengujian baku yang diakui secara internasional (ISO/IEC 25010). Data yang ditarik bersifat empiris, terukur, dan diolah menggunakan perhitungan statistik untuk menguji kesesuaian antara fungsi sistem dengan kebutuhan operasional UMKM, sehingga pendekatan Positivis adalah pilihan yang paling valid.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Dulu saya menganggap angka kepuasan tinggi pada rilis perangkat lunak sebagai indikator pasti keberhasilan pengembang. Setelah memahami rantai distorsi, saya kini lebih skeptis terhadap klaim tersebut dan akan menggali lebih dalam:
1. Apakah instrumen penilaiannya valid?
2. Pakah nilai rata-rata yang tinggi itu menyembunyikan tingkat eror yang sebenarnya besar?
3. Apakah pengujiannya dilakukan pada lingkungan produksi atau sebatas localhost?"