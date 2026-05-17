# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah tingkat kepuasan (berdasarkan skor SUS) dan tingkat keberhasilan tugas (success rate) pada antarmuka aplikasi SeaBank melampaui standar kelayakan rata-rata industri?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Aplikasi SeaBank | IV | Sistem yang dievaluasi | Identitas Sistem (SeaBank versi terbaru) | Nominal | - | Observasi versi aplikasi yang digunakan partisipan | Merupakan objek (treatment) konstan yang menjadi fokus riset. |
| Kepuasan Pengguna | DV | Persepsi kenyamanan UI/UX | Skor System Usability Scale (SUS) | Interval | Poin (0-100) | Pengisian 10 item kuesioner SUS setelah selesai simulasi | Kuesioner SUS adalah instrumen standar global yang tervalidasi. |
| Efektivitas | DV | Kemampuan menyelesaikan tugas | Task Success Rate | Ratio | Persentase (%) | (Jumlah task berhasil diselesaikan / Total task) * 100% | Sesuai pedoman ISO 9241-11 untuk mengukur efektivitas. |
| Efisiensi | DV | Kecepatan bertransaksi | Time-based Efficiency | Ratio | Detik (sec) | Menggunakan stopwatch saat task scenario berlangsung | Metrik waktu adalah ukuran paling objektif untuk efisiensi beban kognitif. |
| Profil Partisipan | CV | Pengalaman pengguna (Mental Model) | Durasi menjadi nasabah SeaBank | Ordinal | Bulan/Tahun | Kuesioner screening di awal (pre-test) | Mengontrol bias; pengguna lama pasti lebih cepat dari pengguna baru. |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [X] Setiap langkah terdokumentasi
  [X] Tidak ada "lompatan logis"
  [X] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah tingkat kepuasan (SUS) dan tingkat keberhasilan tugas (success rate) pada antarmuka aplikasi SeaBank melampaui standar kelayakan rata-rata industri?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Antarmuka SeaBank | IV | Antarmuka Perbankan Digital | Aplikasi mobile spesifik | Nominal | — |
| Kepuasan Pengguna | DV | Persepsi Subjektif Kenyamanan | Skor Akhir Kuesioner SUS | Interval | 0-100 Poin |
| Tingkat Keberhasilan | DV | Efektivitas Navigasi | Task Success Rate | Ratio | Persentase (%) |
| Kecepatan Transaksi | DV |Efisiensi Navigasi UI | Time-based Efficiency | Ratio | Detik |
| Pengalaman Partisipan | CV | Literasi Digital Nasabah | Filter kriteria pengguna aktif | Nominal | Kategori |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [X] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Sangat mewakili. Skor SUS, Success Rate, dan Time (Waktu) adalah 3 metrik mutlak yang merepresentasikan definisi Usability berdasarkan standar internasional (ISO 9241-11). |
| Sensitive | 4 | Cukup peka. Skor SUS (0-100) dan hitungan waktu (detik) sangat detail sehingga dapat membedakan sedikit saja kebingungan yang dialami pengguna. |
| Feasible | 5 | Sangat memungkinkan. Evaluasi Task Scenario bisa dilakukan secara langsung maupun jarak jauh (via Zoom screen share), dan SUS bisa dihitung otomatis pakai Google Forms. |

**Apakah perlu secondary metric?** [X] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? metrik sekunder berupa Error Rate (Jumlah klik salah / defect). Alasannya: Karena seorang pengguna aplikas bisa saja berhasil mencapai 100% Success Rate, tapi jika ia salah pencet menu sebanyak 5 kali sebelum berhasil, itu membuktikan UI tersebut membingungkan. Error rate menambal celah dari Success Rate.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika skenario tugas (task) yang dirancang peneliti terlalu mudah (misalnya: "Coba login ke aplikasi"), maka semua partisipan akan mendapat Success Rate 100% dan waktu pengerjaan 2 detik. Akibatnya, metrik gagal mendeteksi masalah kelancaran navigasi yang sebenarnya terjadi di fitur yang lebih kompleks (seperti fitur deposito).

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Ada risiko responden lupa mengisi beberapa pertanyaan di kuesioner SUS. | Menggunakan Google Forms dan mengaktifkan fitur "Wajib Diisi" (Required) pada seluruh 10 item kuesioner SUS. |
| Consistency | *Apakah ada kontradiksi internal?* | Responden yang malas baca mungkin memilih angka "5" (Sangat Setuju) untuk semua pertanyaan SUS. | Pertanyaan ganjil & genap di SUS saling bertolak belakang. Jawaban bernilai 5 semua akan terdeteksi sebagai kontradiksi dan datanya akan dieliminasi (data cleaning). |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | Ya, kuesioner SUS sudah diakui validitasnya oleh peneliti global untuk mengukur usability. | Menggunakan instrumen SUS versi terjemahan Bahasa Indonesia yang sudah divalidasi keandalannya di riset-riset sebelumnya (misal: oleh Sharfina & Santoso). |
| Representativeness | *Apakah sampel mewakili populasi target?* | Bisa tidak mewakili jika partisipan yang diuji hanyalah teman kampus IT peneliti. | Menerapkan kriteria inklusi sampel: Partisipan harus dari berbagai latar belakang jurusan/pekerjaan yang merupakan pengguna murni aplikasi SeaBank (bukan desainer UI/UX). |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data (p-hacking) ibarat memanah dinding kosong, lalu menggambar target pas di tengah anak panah yang menancap agar seolah-olah kita tepat sasaran. Ini adalah manipulasi (distorsi) karena peneliti menyeleksi metrik yang hanya menguntungkan dan membuang hasil buruk.
Eksplorasi data yang sah, di sisi lain, berarti kita menetapkan metrik utama sejak awal eksperimen (Pre-registration). Jika hasilnya ternyata gagal atau tidak sesuai hipotesis, kita jujur melaporkannya. Kemudian, jika saat melihat data kita menemukan pola atau wawasan baru (misalnya pengguna ternyata lebih lambat di jam malam), temuan tersebut dilaporkan secara transparan sebagai "metrik eksploratif" atau temuan tambahan, bukan diklaim sebagai tujuan utama dari awal.