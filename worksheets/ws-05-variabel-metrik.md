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

Research Question: Apakah terdapat korelasi yang signifikan antara rasio sentimen negatif publik (berbasis K-NN pada ulasan Play Store) dengan metrik performa objektif (Skor SUS dan Task Success Rate) pada aplikasi SeaBank?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|     Kategori Ulasan     | IV   |    Sentimen Publik    |    Rasio Klasifikasi Sentimen    |   Ratio    |    %    |       Ekstraksi API Play Store & Analisis K-NN        |      Representasi persepsi publik skala besar.       |
|     Tingkat Kebergunaan     | DV   |    Performa Usability (Subjektif)    |    Skor System Usability Scale (SUS)    |   Interval    |   Poin (0-100)     |       Kuesioner SUS pasca-task        |      Standar pengukuran usability berbasis persepsi.       |
|     Pengalaman Pengguna     | CV   |    Demografi    |    Lama penggunaan aplikasi    |   Ordinal    |    Bulan    |       Kuesioner pra-task        |      Mengontrol bias learning curve pengguna lama.       |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [X] Setiap langkah terdokumentasi
  [X] Tidak ada "lompatan logis"
  [X] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah terdapat korelasi yang signifikan antara rasio sentimen negatif publik (berbasis K-NN pada ulasan Play Store) dengan metrik performa objektif (Skor SUS dan Task Success Rate) pada aplikasi SeaBank?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Sentimen Ulasan | IV | Opini Publik | Rasio Sentimen K-NN | Ratio | % |
| Skor Usability | DV | Persepsi Pengguna | Skor SUS | Interval | Poin (0-100) |
| Task Success | DV | Efektivitas Sistem | Success Rate | Ratio | % |
| Demografi | CV | Pengalaman Pengguna | Lama Pemakaian | Ordinal | Bulan/Tahun |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [X] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Skor SUS dan Success Rate secara langsung mewakili construct validity dari konsep usability. |
| Sensitive | 4 | Success Rate mungkin kurang peka jika task terlalu mudah, namun Skor SUS memiliki rentang 0-100 yang cukup sensitif. |
| Feasible | 5 | Pengambilan data melalui observasi task dan kuesioner sangat mungkin dilakukan dalam batasan waktu riset. |

**Apakah perlu secondary metric?** [X] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Perlu menambahkan Time on Task (Waktu Eksekusi) dalam satuan milisecond (Ratio) sebagai secondary metric. Tujuannya untuk menangkap inefisiensi pada partisipan yang berhasil menyelesaikan tugas namun membutuhkan waktu yang sangat lama.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika skenario tugas (task scenario) dirancang terlalu mudah atau terlalu mendasar (misalnya: sekadar login), maka hampir 100% responden akan berhasil, sehingga metrik Success Rate kehilangan kemampuannya untuk mendeteksi friction points pada antarmuka.
---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Bisa terjadi nilai kosong jika responden tidak menyelesaikan kuesioner. | Menggunakan validasi mandatory fields (required) pada form kuesioner digital. |
| Consistency | Apakah ada kontradiksi internal? | Responden mungkin menjawab secara acak atau pola lurus. | Menggunakan sistem reverse phrasing pada kuesioner SUS (pertanyaan ganjil positif, genap negatif) untuk memverifikasi konsistensi. |
| Validity | Apakah benar-benar mengukur yang dimaksud? | Risiko metrik mengukur estetika visual, bukan fungsi usability. | Mengunci skenario tugas pada alur transaksi inti (deposito/mutasi) sehingga pengujian murni pada efektivitas sistem. |
| Representativeness | Apakah sampel mewakili populasi target? | Mayoritas responden mungkin mahasiswa TI yang terbiasa dengan teknologi. | Merekrut responden dengan berbagai tingkat keahlian (tech-savvy dan awam) yang merupakan nasabah aktif SeaBank. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat data (p-hacking) merusak objektivitas riset karena peneliti dengan sengaja memanipulasi parameter hingga menemukan hasil yang signifikan secara statistik, sehingga H₀ seolah-olah berhasil ditolak. Ini membuat kesimpulan menjadi bias dan tidak valid. Eksplorasi data yang sah (data exploration) berbeda; dalam eksperimen yang benar, metrik utama (termasuk pre-registration) sudah dikunci sebelum eksperimen dimulai[cite: 4]. Jika di tengah evaluasi ditemukan anomali atau pola metrik baru, temuan tersebut tetap dilaporkan secara transparan sebagai secondary metric atau temuan eksploratori, bukan diklaim sebagai jawaban utama (confirmatory) dari hipotesis awal.
