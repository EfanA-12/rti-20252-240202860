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

Research Question: ____________________

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|          | IV   |        |        |       |        |               |             |
|          | DV   |        |        |       |        |               |             |
|          | CV   |        |        |       |        |               |             |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [ ] Setiap langkah terdokumentasi
  [ ] Tidak ada "lompatan logis"
  [ ] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah aplikasi BCA Mobile memiliki tingkat usability yang dapat diterima oleh nasabah di Singaraja?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Kelompok Pengguna | IV | Tingkat pengalaman partisipan | Kategorikal: Non-pengguna vs Pengguna Aktif | Nominal | — |
| Efisiensi Sistem | DV | Kecepatan kerja (Efficiency) | Time-based efficiency (goals/sec) | Ratio | goals/sec |
| Skenario Tugas | CV | Standarisasi beban pengujian | 4 Tugas (Cek saldo, transfer, mutasi, top up) | Nominal | — |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [X] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Mewakili kepuasan subjektif secara menyeluruh melalui 10 pernyataan standar industri. |
| Sensitive | 4 | Skala Likert 1-5 cukup peka untuk menangkap variasi pendapat responden yang beragam. |
| Feasible | 5 | Sangat mudah dikumpulkan karena hanya membutuhkan pengisian kuesioner singkat. |

**Apakah perlu secondary metric?** [X] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Penambahan metrik Success Rate bertujuan untuk memverifikasi apakah persepsi kepuasan nasabah selaras dengan kemampuan nyata mereka dalam menyelesaikan skenario tugas yang diberikan.
Tanpa dukungan data objektif, hasil evaluasi berisiko mengalami bias karena hanya mengandalkan opini subjektif tanpa bukti eksekusi yang terukur.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika tugas yang diberikan terlalu sederhana (contohnya ya itu: hanya menekan tombol login), semua partisipan akan merasa sangat puas dan sukses 100%, sehingga metrik tidak bisa membedakan kualitas desain yang sebenarnya.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | Ya, meskipun ada tugas yang gagal (Fail), data tersebut tetap dicatat untuk perhitungan. | Memastikan seluruh 4 task dicatat hasilnya baik berhasil maupun gagal. |
| Consistency | *Apakah ada kontradiksi internal?* | Mungkin ada pengguna yang memberi skor kepuasan tinggi tapi gagal di banyak tugas. | Melakukan wawancara untuk memahami mengapa mereka tetap merasa puas meski mengalami kesulitan. |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | Ya, penggunaan metrik Nielsen sudah baku untuk pengujian perangkat lunak. | Mengikuti panduan perhitungan rumus SUS dan Success Rate dari literatur tepercaya. |
| Representativeness | *Apakah sampel mewakili populasi target?* | Sampel 6 orang untuk tes dan 20 untuk kuesioner dianggap cukup untuk skala studi kasus lokal. | Memilih partisipan dengan rentang usia yang luas (18-56 tahun) agar mewakili nasabah umum. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Penetapan metrik setelah observasi data dikategorikan sebagai p-hacking karena memungkinkan peneliti melakukan seleksi metrik secara selektif demi menunjukkan hasil yang signifikan, sehingga validitas riset berkurang. Perbedaan mendasarnya dengan eksplorasi data yang sah terletak pada tujuan: eksplorasi berfokus pada identifikasi anomali atau pola untuk merumuskan hipotesis baru, sementara penelitian konfirmatori mewajibkan metrik ditentukan sebelum eksperimen dimulai guna menjamin objektivitas.