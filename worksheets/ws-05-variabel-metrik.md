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

Research Question: Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang koheren (Coherence Score c_v >= 0.4) menggunakan model LDA pada ulasan aplikasi SeaBank?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Filter Sentimen | IV | Pra-pemrosesan Data | Status Penggunaan Filter | Nominal | Ya/Tidak | Dijalankan via script Python | Menjadi kondisi perlakuan utama (Treatment vs Baseline). |
| Performa Klasifikasi | DV | Keandalan K-NN | F1-Score & Accuracy | Ratio | % | Kalkulasi otomatis via library Scikit-Learn | Menyeimbangkan ukuran presisi dan recall pada dataset ulasan yang rentan imbalanced. |
| Kualitas Topik | DV | Koherensi Semantik LDA | Coherence Score (c_v) | Ratio | Nilai (0-1) | Dihitung otomatis via library Gensim | Metrik SOTA (State-of-the-Art) untuk mengukur apakah topik yang dihasilkan masuk akal bagi manusia. |
| Dataset Ulasan | CV | Batasan Lingkungan | Rentang Waktu Ulasan | Interval | Bulan/Tahun | Dikunci pada parameter script scraper | Memastikan perbandingan K-NN dan LDA dilakukan pada kondisi data yang identik. |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [X] Setiap langkah terdokumentasi
  [X] Tidak ada "lompatan logis"
  [X] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang koheren (Coherence Score c_v >= 0.4) menggunakan model LDA pada ulasan aplikasi SeaBank?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Sentimen Ulasan | IV | Intervensi Pemrosesan | Penggunaan Filter K-NN | Nominal | Ya / Tidak |
| Skor Usability | DV | Keakuratan Prediksi | F1-Score | Ratio | % |
| Task Success | DV | Koherensi Semantik | Coherence Score (c_v) | Ratio | Nilai (0 - 1) |
| Demografi | CV | Konfigurasi Model | Nilai K (K-NN) & Jumlah Topik (LDA) | Ratio | Integer (Angka Mutlak) |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [X] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | F1-Score dan Coherence Score adalah metrik baku dalam paper jurnal NLP untuk mengukur klasifikasi dan pemodelan topik. |
| Sensitive | 4 | Coherence Score sangat sensitif terhadap perubahan nilai K (jumlah topik) pada model LDA. |
| Feasible | 5 | Semua metrik dapat dihitung secara instan menggunakan fungsi bawaan (built-in functions) pada library Python. |

**Apakah perlu secondary metric?** [X] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Ya, perlu metrik Waktu Komputasi / Execution Time (satuan detik). Tujuannya untuk melihat seberapa besar beban komputasi tambahan jika K-NN dan LDA digabungkan, karena efisiensi sumber daya juga penting dalam pipeline Machine Learning.

**Contoh kasus ceiling effect untuk metrik ini:**
> Model K-NN mencapai metrik Accuracy hingga 99% bukan karena modelnya pintar, melainkan karena terkena efek Data Imbalance (misalnya 99% isi dataset adalah ulasan positif). Model akhirnya hanya "menebak" kelas mayoritas, sehingga metrik Accuracy menjadi tidak sensitif (mengalami ceiling effect). Inilah alasan F1-Score digunakan sebagai metrik utama yang lebih tangguh.
---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Sangat mungkin terdapat baris ulasan (scraping) yang hanya berisi rating bintang tanpa teks keluhan sama sekali. | Melakukan dropping (penghapusan) pada baris data yang bernilai NaN/Null pada kolom teks. |
| Consistency | Apakah ada kontradiksi internal? | Adanya duplikasi data akibat serangan bot/buzzer yang menulis ulasan dengan teks persis sama berulang kali. | Menambahkan fungsi .drop_duplicates() pada Pandas DataFrame di tahap awal pra-pemrosesan. |
| Validity | Apakah benar-benar mengukur yang dimaksud? | Teks ulasan yang penuh dengan typo, singkatan, dan slang khas Indonesia akan merusak hasil ekstraksi topik LDA. | Melakukan normalisasi teks menggunakan kamus slang (slang word dictionary) dan library Sastrawi untuk stemming. |
| Representativeness | Apakah sampel mewakili populasi target? | Algoritma scraper mungkin hanya menarik ulasan dari versi update aplikasi minggu terakhir. | Mengatur rentang tanggal scraping (parameter timeframe) agar mencakup ulasan minimal 6 bulan terakhir. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Dalam konteks Machine Learning, mengubah-ubah parameter (seperti nilai random_state atau metrik evaluasi) secara membabi buta hanya agar hasil akurasinya terlihat tinggi (>90%) adalah bentuk manipulasi p-hacking. Hal ini merusak objektivitas karena model tidak benar-benar belajar, melainkan kita hanya mencari celah agar terlihat bagus. Eksplorasi data yang sah berarti kita sudah mengunci rencana pengukuran (pre-registration)—misalnya mengunci penggunaan F1-Score sebagai metrik—sebelum script dijalankan. Jika di tengah evaluasi ternyata hasilnya rendah, temuan tersebut dilaporkan secara jujur untuk kemudian dianalisis penyebabnya secara logis, bukan sekadar mengganti metrik agar angkanya membaik secara artifisial.
