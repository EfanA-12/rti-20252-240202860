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

Gap Statement  : Belum ada studi yang memvalidasi tingkat usability aplikasi perbankan digital (SeaBank) melalui triangulasi antara metrik performa objektif (eksperimen) dan sentimen subjektif (ulasan publik).

Research Question:
  Tipe         : [ ] Comparison  [ ] Improvement  [X] Exploratory
  Formulasi    : Apakah terdapat korelasi yang signifikan antara rasio sentimen negatif publik (berbasis K-NN pada ulasan Play Store) dengan metrik performa objektif (Skor SUS dan Task Success Rate) pada aplikasi SeaBank?
  Variabel IV  : Sentimen Ulasan Publik (Positif/Negatif).
  Variabel DV  : Performa Usability Objektif (Skor SUS dan Task Success Rate).
  Metrik       : Persentase klasifikasi sentimen (%), Skor SUS (0-100), dan Success Rate (%).
  Dataset      : Data sekunder (Ulasan Google Play Store) dan Data primer (Hasil tes skenario 30 responden).
  Baseline     : Skor SUS standar (68) dan rasio sentimen riset terdahulu.

Quality Check RQ:
  [X] Variabel spesifik
  [X] Metrik jelas
  [X] Baseline ada
  [X] Konteks disebutkan
  [X] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui :Pemetaan akurat mengenai friction points pada UI SeaBank yang tervalidasi secara hibrida (objektif & subjektif).
  Jenis kontribusi        : [ ] Improvement  [X] Comparison  [ ] Novel approach
  Gap yang diisi          : Methodological Triangulation Gap pada evaluasi mobile banking.

Hypothesis Pair:
  H₀ : Tidak terdapat korelasi yang signifikan antara rasio sentimen ulasan publik dengan hasil performa usability objektif pada aplikasi SeaBank.
  H₁ : Terdapat korelasi yang signifikan antara rasio sentimen ulasan publik dengan hasil performa usability objektif pada aplikasi SeaBank.
  Threshold              : p-value < 0.05 (Tingkat signifikansi 5%).
  Justifikasi threshold  : Standar umum dalam pengujian statistik pada riset Human-Computer Interaction (HCI) untuk menolak hipotesis nol.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Belum ada triangulasi metode antara performa objektif (Task Scenario) dan sentimen subjektif (ulasan publik).
**RQ versi pertama (tulis bebas):**
> Bagaimana perbandingan hasil tes usability SeaBank dengan ulasan di Play Store?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Tidak | Belum menyebutkan metodenya. |
| Metrik terukur | Tidak | Belum ada metrik. |
| Baseline | Tidak | Belum ada acuan. |
| Dataset/konteks | Ya | SeaBank dan Play Store. |

**Tipe RQ:** [ ] Comparison / [ ] Improvement / [X] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah terdapat korelasi yang signifikan antara rasio sentimen negatif (berbasis klasifikasi K-NN) pada ulasan Google Play Store dengan rendahnya performa metrik objektif (Skor SUS < 68 dan Task Success Rate < 70%) pada evaluasi usability aplikasi SeaBank?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak terdapat korelasi yang signifikan (p-value ≥ 0.05) antara sentimen ulasan Play Store dengan hasil performa usability objektif (SUS & Success Rate) SeaBank. |
| H₁ | Terdapat korelasi yang signifikan (p-value < 0.05) antara sentimen ulasan Play Store dengan hasil performa usability objektif (SUS & Success Rate) SeaBank. |
| Metrik | Koefisien korelasi (r) dan p-value. |
| Threshold | p-value < 0.05 |
| Justifikasi threshold | Standar empiris yang diakui dalam riset kuantitatif ilmu komputer dan HCI untuk memastikan bahwa temuan tidak terjadi secara kebetulan. |

**Apakah hipotesis ini falsifiable?** [X] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? ika setelah dilakukan uji korelasi statistik antara data sentimen dan data performa ternyata menghasilkan p-value lebih dari atau sama dengan 0.05, maka hipotesis alternatif (H₁) gugur dan H₀ diterima.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah terdapat korelasi antara rasio sentimen K-NN di Play Store dengan metrik objektif (SUS & Success Rate) pada SeaBank? |
| Variable (IV) | Kategori Sentimen Publik (Positif / Negatif) |
| Variable (DV) | Performa Usability Pengguna |
| Metric | Persentase Sentimen (%), Skor SUS (0-100), Task Success Rate (%) |
| Data source | API Google Play Store (Data sekunder) dan Observasi 30 Nasabah SeaBank (Data primer) |
| Analysis method | Klasifikasi K-NN (Sentimen) & Uji Korelasi Statistik (Spearman/Pearson) |

**Apakah rantai lengkap?** [X] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Evaluasi Usability Aplikasi Tokopedia Menggunakan Metode System Usability Scale (SUS)
**RQ yang diekstrak:** Bagaimana tingkat kelayakan usability dari aplikasi Tokopedia berdasarkan perhitungan skor kuesioner SUS?
**Komponen yang hilang:** RQ tersebut memiliki kualitas yang lemah karena tidak memenuhi kriteria rumusan masalah riset yang baik. Beberapa komponen yang hilang antara lain:
1. Tidak ada Baseline: RQ ini hanya mencari nilai rata-rata (skor) tanpa membandingkannya dengan kondisi lain, algoritma lain, atau kompetitor.
2. Tidak menguji Hipotesis (H₀ / H₁): Karena tidak ada variabel yang dibandingkan atau dikorelasikan, RQ ini tidak bersifat falsifiable (tidak bisa dibuktikan salah melalui eksperimen).