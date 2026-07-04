# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Belum ada studi yang mengintegrasikan pipeline K-NN sebagai filter sentimen negatif sebelum melakukan ekstraksi topik keluhan usability menggunakan Latent Dirichlet Allocation (LDA) pada aplikasi perbankan digital.

Research Question:
  Tipe         : [ ] Comparison  [X] Improvement  [ ] Exploratory
  Formulasi    : Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang koheren (Coherence Score cv >= 0.4) menggunakan model LDA pada ulasan aplikasi SeaBank?
  Variabel IV  : Penerapan Filter K-NN (Sentimen Negatif) dan Jumlah Topik LDA (K-topics).
  Variabel DV  : Kualitas Pemodelan Topik (Topic Quality) dan Performa Klasifikasi.
  Metrik       : Coherence Score (cv) untuk LDA dan F1-Score/Accuracy (%) untuk K-NN.
  Dataset      : Data sekunder (Ulasan Google Play Store SeaBank).
  Baseline     : Model LDA standar (mengekstrak topik dari seluruh ulasan tanpa disaring K-NN terlebih dahulu).

Quality Check RQ:
  [X] Variabel spesifik
  [X] Metrik jelas
  [X] Baseline ada
  [X] Konteks disebutkan
  [X] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Pipeline otomatis berbasis NLP yang terbukti mampu memetakan titik masalah (friction points) antarmuka SeaBank secara akurat dan koheren tanpa intervensi manual.
  Jenis kontribusi        : [X] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : Method Gap (Integrasi K-NN dan LDA untuk meminimalkan noise pada Topic Modeling).

Hypothesis Pair:
  H₀ : Penggunaan K-NN sebagai filter sentimen negatif tidak memberikan hasil topik keluhan yang koheren (Coherence Score cv < 0.4) pada model LDA aplikasi SeaBank.
  H₁ : Penggunaan K-NN sebagai filter sentimen negatif menghasilkan pemodelan topik keluhan yang koheren (Coherence Score cv >= 0.4) pada model LDA aplikasi SeaBank.
  Threshold              : Coherence Score (cv) >= 0.4.
  Justifikasi threshold  : Dalam ranah Topic Modeling (NLP), nilai cv di atas 0.4 hingga 0.5 diakui secara empiris sebagai batas di mana topik yang dihasilkan oleh mesin sudah dapat diinterpretasikan dengan baik oleh manusia.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Belum ada studi yang merangkai pipeline di mana K-NN digunakan sebagai filter (penyaring ulasan bernada negatif) sebelum data tersebut diekstrak menjadi topik keluhan antarmuka secara spesifik menggunakan LDA.
**RQ versi pertama (tulis bebas):**
> Bagaimana hasil topik keluhan SeaBank jika ulasannya dipilah pakai K-NN lalu diproses LDA?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | K-NN dan LDA. |
| Metrik terukur | Tidak | Belum menyebutkan metrik ukur performanya. |
| Baseline | Tidak | Belum ada pembanding (baseline). |
| Dataset/konteks | Ya | Ulasan SeaBank. |

**Tipe RQ:** [ ] Comparison / [X] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang lebih koheren (Coherence Score cv >= 0.4) menggunakan model LDA dibandingkan baseline LDA tanpa filter pada ulasan aplikasi SeaBank?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Pipeline K-NN dan LDA gagal menghasilkan klaster topik keluhan yang dapat diinterpretasikan (Coherence Score cv < 0.4). |
| H₁ | Pipeline K-NN dan LDA berhasil menghasilkan klaster topik keluhan usability yang terstruktur dan dapat diinterpretasikan (Coherence Score c_v >= 0.4). |
| Metrik | Coherence Score (Cv) dan Akurasi (Accuracy). |
| Threshold | Coherence Score (Cv) >= 0.4 |
| Justifikasi tStandar evaluasi pemodelan topik dalam jurnal NLP menetapkan bahwa skor koherensi Cv di atas 0.4 menunjukkan bahwa kata-kata yang berkumpul dalam satu topik memiliki relasi semantik yang kuat (bukan kata acak). |

**Apakah hipotesis ini falsifiable?** [X] Ya / [ ] Tidak
> Jika setelah program Python dijalankan dan model LDA selesai melakukan iterasi pembentukan topik, ternyata nilai perhitungan Coherence Score mentok di angka 0.2 atau 0.3, maka H₁ otomatis gugur dan H₀ diterima (artinya pipeline ini gagal menghasilkan topik yang berbunyi).

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah K-NN dan LDA mampu mengekstrak topik keluhan usability SeaBank dengan skor koherensi >= 0.4? |
| Variable (IV) | Parameter Model: Nilai K pada K-NN dan Jumlah Topik (K-topics) pada LDA. |
| Variable (DV) | Kinerja / Performa Model (Model Performance). |
| Metric | Accuracy (%), Precision, Recall, F1-Score, dan Coherence Score (Cv). |
| Data source | Data sekunder berupa teks ulasan dari API Google Play Store. |
| Analysis method | Confusion Matrix (untuk evaluasi K-NN) dan Topic Modeling Evaluation (untuk evaluasi LDA). |

**Apakah rantai lengkap?** [X] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Analisis Sentimen Ulasan Pengguna Aplikasi E-Commerce X Menggunakan Algoritma K-Nearest Neighbor (K-NN).
**RQ yang diekstrak:** Bagaimana sentimen pengguna terhadap aplikasi e-commerce X berdasarkan algoritma K-NN?
**Komponen yang hilang:** RQ tersebut sangat lemah untuk standar Data Science karena:
1. Tidak ada Metrik Terukur: Hanya bertanya "bagaimana sentimennya", bukan "seberapa akurat K-NN dalam memilah sentimen tersebut".
2. Tidak ada Baseline: Tidak membandingkan K-NN dengan algoritma lain (misal Naive Bayes) atau parameter default.
3. Tidak Falsifiable: RQ ini hanya bersifat deskriptif (mendeskripsikan hasil) sehingga tidak ada hipotesis yang bisa dibuktikan gagal (H₀) dalam eksperimen.