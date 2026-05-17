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

Gap Statement  : Belum adanya pengujian empiris yang memadukan Task Scenario (untuk mengukur performa objektif) dan kuesioner SUS (untuk kepuasan subjektif) pada aplikasi bank digital murni (branchless banking) seperti SeaBank.

Research Question:
  Tipe         : [ ] Comparison  [ ] Improvement  [X] Exploratory / Evaluative
  Formulasi    : Apakah skor kepuasan rata-rata pengguna aplikasi SeaBank saat mengeksekusi skenario transaksi utama melampaui ambang batas standar kelayakan (SUS score > 68)?
  Variabel IV  : Antarmuka Aplikasi SeaBank (Sistem yang dievaluasi)
  Variabel DV  : Tingkat Kegunaan / Usability (Efektivitas, Efisiensi, Kepuasan)
  Metrik       : Success Rate (%), Time-based Efficiency (goals/sec), dan Skor SUS (skala 0-100)
  Dataset      : Data observasi 6 pengguna (Task Scenario) dan kuesioner dari 20+ responden nasabah SeaBank.
  Baseline     : Standar rata-rata industri untuk SUS (skor 68) dan rata-rata completion rate global (78%).

Quality Check RQ:
  [X] Variabel spesifik
  [X] Metrik jelas
  [X] Baseline ada
  [X] Konteks disebutkan
  [X] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Baseline metrik empiris (tingkat efektivitas, efisiensi, dan kepuasan) dari UI/UX aplikasi bank digital murni yang tidak memiliki dukungan kantor cabang.
  Jenis kontribusi        : [ ] Improvement  [ ] Comparison  [X] Novel approach / Baseline Establishment
  Gap yang diisi          : Mengisi Method Gap & Context Gap dengan menerapkan pengujian gabungan (Task Scenario + SUS) pada konteks branchless banking.

Hypothesis Pair:
  H₀ : Rata-rata skor kepuasan (SUS) pengguna aplikasi SeaBank ≤ 68 (Berada pada level rata-rata atau di bawah standar kelayakan).
  H₁ : Rata-rata skor kepuasan (SUS) pengguna aplikasi SeaBank > 68 (Berada di atas standar kelayakan/acceptable).
  Threshold              : Skor SUS = 68.
  Justifikasi threshold  : Skor 68 adalah acuan global dari literatur (Sauro & Lewis) yang diakui secara akademis untuk menentukan apakah antarmuka suatu sistem dikategorikan layak digunakan (acceptable) atau butuh perbaikan.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Kurangnya evaluasi empiris pada bank digital murni yang memadukan pengukuran performa objektif (Task Scenario) dengan pengukuran kepuasan subjektif (SUS) untuk menguji kelayakan UI/UX-nya.

**RQ versi pertama (tulis bebas):**
> Bagaimana tingkat usability aplikasi SeaBank dan apakah penggunanya merasa puas?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Tidak | Belum menyebutkan instrumen/metodenya. |
| Metrik terukur | Tidak | "Tingkat usability" masih terlalu abstrak, belum ada angka terukurnya. |
| Baseline | Tidak | Tidak ada standar perbandingan |
| Dataset/konteks | Ya | Aplikasi SeaBank. |

**Tipe RQ:** [ ] Comparison / [ ] Improvement / [X] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah tingkat kepuasan (berdasarkan metrik System Usability Scale) dan tingkat keberhasilan tugas (success rate) pada antarmuka aplikasi SeaBank melampaui standar kelayakan rata-rata industri (SUS > 68 dan Success Rate > 78%)?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Rata-rata skor SUS aplikasi SeaBank ≤ 68 dan success rate ≤ 78% (Tidak melampaui standar kelayakan industri). |
| H₁ | Rata-rata skor SUS aplikasi SeaBank > 68 dan success rate > 78% (Secara signifikan melampaui standar kelayakan industri). |
| Metrik | Skor gabungan instrumen kuesioner SUS (rentang 0-100) dan Task Success Rate (%). |
| Threshold | Skor 68 (Untuk SUS) dan 78% (Untuk Completion Rate). |
| Justifikasi threshold | Standar acuan akademik global (Sauro, 2011) yang membagi kategori usability menjadi Not Acceptable, Marginal, dan Acceptable (Skor > 68). |

**Apakah hipotesis ini falsifiable?** [X] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Jika setelah pengumpulan data dari responden dilakukan perhitungan statistik (One-Sample T-Test) dan hasilnya menunjukkan nilai rata-rata (mean) SUS berada di angka 60 (kurang dari 68), maka secara otomatis hipotesis awal (H₁) gagal dibuktikan, dan H₀ diterima.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah skor kepuasan SUS dan keberhasilan tugas pada aplikasi SeaBank melampaui standar acceptable industri? |
| Variable (IV) | Antarmuka pengguna (UI/UX) aplikasi SeaBank.|
| Variable (DV) | Kepuasan pengguna (Satisfaction) dan Tingkat Keberhasilan (Learnability). |
| Metric | Skor skala likert yang dikonversi ke sistem SUS (0-100) dan Persentase (%). |
| Data source | Data log durasi task scenario dari 6 pengguna dan kuesioner dari minimal 20 responden nasabah SeaBank. |
| Analysis method | Analisis statistik deskriptif dan pengujian rata-rata satu populasi (One-Sample T-Test terhadap nilai acuan 68). |

**Apakah rantai lengkap?** [X] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Evaluasi Usability Pada Aplikasi BNI Mobile Banking Dengan Menggunakan Metode Usability Testing dan System Usability Scale
**RQ yang diekstrak:** Bagaimana tingkat kegunaan (usability) pada aplikasi BNI Mobile Banking?
**Komponen yang hilang:** RQ di paper tersebut kurang tajam karena Metrik Terukur dan Baseline dihilangkan dari rumusan masalah utamanya. Pertanyaan tersebut tidak menyebutkan akan diuji dengan threshold apa dan angka kesuksesannya akan diukur berdasarkan parameter pembanding apa, sehingga terkesan sangat normatif.