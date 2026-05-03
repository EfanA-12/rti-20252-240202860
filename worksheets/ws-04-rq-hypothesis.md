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

Gap Statement  : Belum ada integrasi yang kuat antara pengujian berbasis sentimen pengguna (seperti SUS) dengan inspeksi pakar antarmuka (Heuristic Evaluation) untuk mendiagnosis masalah UX secara akurat.

Research Question:
  Tipe         : [X] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : Apakah integrasi metode SUS (System Usability Scale) dan Heuristic Evaluation menghasilkan identifikasi masalah usability yang lebih banyak dan presisi dibandingkan metode kuesioner tunggal pada evaluasi komparatif aplikasi Mobile Banking X dan Y?
  Variabel IV  : Strategi Evaluasi (Metode Tunggal vs. Metode Integrasi).
  Variabel DV  : Kuantitas dan kualitas temuan masalah usability.
  Metrik       : Jumlah temuan masalah (issue count), skor kepuasan (SUS), dan peringkat keparahan (severity rating).
  Dataset      : Antarmuka fitur utama (transfer, cek saldo, mutasi) pada dua aplikasi mobile banking berbeda.
  Baseline     : Metode kuesioner tunggal (seperti dalam studi Dewi, dkk., 2022).

Quality Check RQ:
  [X] Variabel spesifik
  [X] Metrik jelas
  [X] Baseline ada
  [X] Konteks disebutkan
  [X] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Efektivitas integrasi metrik kuantitatif dan kualitatif dalam mendiagnosis masalah antarmuka secara presisi pada domain aplikasi finansial.
  Jenis kontribusi        : [ ] Improvement  [X] Comparison  [ ] Novel approach
  Gap yang diisi          : Method Gap (integrasi instrumen) dan Context Gap (perbandingan kompetitor).

Hypothesis Pair:
  H₀ : Tidak ada perbedaan signifikan dalam jumlah temuan masalah usability antara metode integrasi dan metode kuesioner tunggal.
  H₁ : Metode integrasi menghasilkan identifikasi masalah usability yang lebih banyak secara signifikan dibandingkan metode kuesioner tunggal.
  Threshold              : p < 0,05 (Signifikansi statistik).
  Justifikasi threshold  : Ambang batas ini adalah standar akademik untuk menolak hipotesis nol dan memastikan hasil bukan karena kebetulan.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Belum ada integrasi instrumen pelacak kepuasan dengan instrumen pelacak error antarmuka secara simultan.

**RQ versi pertama (tulis bebas):**
> Bagaimana cara menggabungkan metode SUS dan Heuristic Evaluation untuk mengevaluasi aplikasi Mobile Banking agar hasilnya lebih akurat dibandingkan aplikasi lain?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya | Integrasi metode SUS dan Heuristic Evaluation. |
| Metrik terukur | Ya | Jumlah temuan masalah (usability issues) dan skor kepuasan. |
| Baseline | Ya | Metode kuesioner tunggal (seperti pada penelitian Dewi et al., 2022). |
| Dataset/konteks | Ya | Antarmuka aplikasi Mobile Banking. |

**Tipe RQ:** [X] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah integrasi metode System Usability Scale (SUS) dan Heuristic Evaluation mampu menghasilkan identifikasi masalah usability yang lebih komprehensif dibandingkan metode kuesioner tunggal pada aplikasi Mobile Banking?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | H_0Tidak ada perbedaan signifikan dalam jumlah temuan masalah usability antara metode integrasi (SUS + Heuristic) dan metode kuesioner tunggal pada aplikasi Mobile Banking. |
| H₁ | Metode integrasi (SUS + Heuristic) menghasilkan jumlah temuan masalah usability yang lebih banyak dan lebih presisi secara signifikan dibandingkan metode kuesioner tunggal. |
| Metrik | Jumlah usability issues yang tervalidasi dan rata-rata severity rating. |
| Threshold | Nilai signifikansi p < 0,05 (Alpha 5%) atau peningkatan jumlah temuan minimal sebesar 30%. |
| Justifikasi threshold | Ambang batas p < 0,05 adalah standar umum dalam penelitian perangkat lunak untuk menolak klaim kebetulan, sedangkan target 30% didasarkan pada ekspektasi keunggulan metode campuran terhadap metode tunggal. |

**Apakah hipotesis ini falsifiable?** [X] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Terbukti salah jika hasil eksperimen menunjukkan bahwa jumlah masalah usability yang ditemukan melalui integrasi metode tidak lebih banyak (atau justru lebih sedikit) dibandingkan hanya menggunakan satu metode saja.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah integrasi metode SUS dan Heuristic Evaluation lebih efektif mendeteksi masalah usability dibanding metode tunggal? |
| Variable (IV) | Strategi Evaluasi (Metode Integrasi vs. Metode Tunggal). |
| Variable (DV) | Efektivitas deteksi masalah usability. |
| Metric | Issue count (jumlah temuan) dan tingkat keparahan (severity score). |
| Data source | Log pengujian tugas (task scenario), skor kuesioner dari nasabah, dan catatan observasi pakar. |
| Analysis method | Uji komparatif statistik (misalnya Wilcoxon Signed-Rank Test) untuk membandingkan performa kedua kelompok metode. |

**Apakah rantai lengkap?** [X] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Evaluasi Usability Aplikasi Mobile Banking BCA dengan menggunakan Usability Testing dan System Usability Scale (Studi Kasus: BCA Kota Singaraja)
**RQ yang diekstrak:** Bagaimana tingkat usability aplikasi mobile banking berdasarkan persepsi pengguna menggunakan kuesioner SUS?
**Komponen yang hilang:** Baseline: Penelitian tersebut hanya berfokus pada satu aplikasi tanpa membandingkan hasilnya dengan aplikasi kompetitor sejenis atau standar industri yang lebih luas dalam formulasi pertanyaannya.
Diagnosis Kesalahan Spesifik: RQ tersebut tidak mencakup metode inspeksi (seperti Heuristic Evaluation) yang bisa menunjukkan koordinat atau titik presisi di mana kesalahan desain terjadi, sehingga hanya menghasilkan skor kepuasan umum.
