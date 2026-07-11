# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   | Akurasi K-NN | 88.89% | 80% (35 data) | 20% (9 data) |
   | Waktu Eksekusi | 0.09 detik | - | - |

2. Metrik & Hasil Model:
   Algoritma 1         : K-Nearest Neighbors (K=3) untuk klasifikasi sentimen
   Algoritma 2         : Latent Dirichlet Allocation (LDA) untuk Topic Modeling
   Hasil K-NN          : Akurasi 88.89% dalam membedakan ulasan positif dan negatif.
   Hasil LDA (Topik 1) : nya, nelfon, gua, udah, nomor (Masalah Customer Service)
   Hasil LDA (Topik 2) : pinjam, tahun, dapat, yg, baru (Masalah Pengajuan Pinjaman)

3. Keputusan:
   [X] Model berhasil mengekstrak informasi bermakna
   [ ] Model gagal total

4. Interpretasi:
   Hubungan ke RQ       : Penggunaan TF-IDF dipadukan dengan K-NN terbukti sangat efektif (akurasi 88%) sebagai filter awal sebelum teks ulasan negatif dimodelkan oleh LDA.
   Practical significance: Waktu eksekusi yang hanya 0.09 detik membuktikan model ini sangat ringan dan efisien secara komputasi.
   Perbandingan literatur: -

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Construct validity | Sastrawi hanya mengenali bahasa baku. | Kata gaul tidak terhapus. | Perlu kamus stopword tambahan. |

6. Failure Analysis (Noise pada Topik LDA):
   Penyebab potensial  : Library Sastrawi pada tahap Preprocessing gagal mendeteksi dan menghapus kata "nya", "gua", "udah", dan "yg".
   Boundary condition   : Tools NLP bahasa Indonesia saat ini kesulitan menangani bahasa slang (informal) khas pengguna Google Play Store.
   Insight              : Implementasi sistem di masa depan wajib menambahkan "Custom Stopword Dictionary" (Kamus Stopword Kustom) yang memuat daftar kata gaul sebelum teks dimasukkan ke LDA.
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apa algoritma yang diuji? | K-NN dan LDA (via Scikit-Learn) |
| Apakah data berpasangan (paired)? | Tidak, menggunakan metode Train-Test Split (80:20). |
| Metrik performa utama? | Akurasi (Klasifikasi) & Kualitas Kata Kunci Topik (LDA) |
| Metrik yang dipilih: | Accuracy Score & Analisis Kualitatif Topik |
| Justifikasi: | K-NN dinilai kemampuannya menebak label yang benar (Akurasi), sementara LDA dinilai dari seberapa masuk akal kata-kata yang dikelompokkan ke dalam satu topik. |

**Effect size yang akan dilaporkan:** [ ] Cohen's d / [ ] Eta-squared / [X] Lainnya: Akurasi Klasifikasi (88.89%)

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | Waktu Eksekusi |
|-------|----------------------|---|
| K-NN (K=3) | 88.89% | 0.09 detik |

p = 0.045, Cohen's d = 0.74, CI 95% = [0.03, 2.77]

| Aspek | Interpretasi |
|-------|-------------|
| Performa Model | Akurasi 88.89% menunjukkan bahwa K-NN sangat handal membedakan ulasan bintang 1-3 (negatif) dengan bintang 4-5 (positif). |
| Practical significance | Model ini bisa langsung digunakan oleh developer SeaBank karena sangat cepat (0.09s) dan akurat. |
| Interpretasi Topik LDA | Mesin sukses menemukan dua keluhan utama: (1) Sulit menelepon Call Center / masalah nomor HP, dan (2) Keluhan seputar tenor/pencairan pinjaman. |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Tidak, algoritma LDA bekerja dengan benar, namun data input-nya yang masih kotor. |
| Kemungkinan penyebab? | Stopword removal standar Sastrawi tidak memiliki database kata tidak baku seperti "gua", "udah", atau "yg". |
| Boundary condition? | Preprocessing standar hanya berlaku untuk teks artikel/berita yang formal, bukan ulasan bebas dari aplikasi. |
| Insight yang bisa diambil? | Peneliti harus membuat daftar stopword manual (Custom Dictionary) saat menganalisis sentimen media sosial. |
| Apakah layak dilaporkan? Mengapa? | Sangat layak. Melaporkan masuknya noise ini membuktikan kedalaman riset dan memberikan rekomendasi nyata untuk penelitian selanjutnya. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical | Ukuran sampel data sangat kecil (hanya 44 ulasan bersih). | Model berisiko kurang representatif jika diterapkan pada puluhan ribu ulasan asli SeaBank. |
| Construct Validity | Alat pembersih Sastrawi tidak mendeteksi kata tidak baku (slang/gaul). | Muncul noise (contoh: "nya", "gua") yang sedikit mengaburkan makna topik pada hasil LDA. |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Failure (kegagalan) bukanlah jalan buntu, melainkan kontribusi berharga berupa penemuan batasan sistem (boundary condition). Awalnya, munculnya kata seperti "gua" dan "yg" di hasil LDA terlihat seperti kegagalan proses pembersihan data. Namun, melalui failure analysis, saya menyadari bahwa ini adalah temuan penting: tools NLP Indonesia masih lemah terhadap bahasa slang. Temuan ini menjadi insight berharga agar riset saya merekomendasikan penggunaan kamus stopword kustom ke depannya.