# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang koheren (Coherence Score c_v >= 0.4) menggunakan model LDA pada ulasan aplikasi SeaBank?
Hypothesis        : H₁: Penggunaan K-NN sebagai filter sentimen negatif menghasilkan pemodelan topik keluhan yang koheren (Coherence Score c_v >= 0.4) pada model LDA aplikasi SeaBank.
Tipe Eksperimen   : [ ] Comparison  [X] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | LDA memproses seluruh dataset ulasan tanpa filter (Baseline) | K-NN Filter = OFF | Dataset ulasan SeaBank sama, K-Topics LDA = 5, Seed = 42 |
| Treatment | LDA memproses hanya ulasan negatif hasil penyaringan | K-NN Filter = ON | Dataset ulasan SeaBank sama, K-Topics LDA = 5, Seed = 42 |

Fairness Checklist:
  [X] Dataset identik untuk semua kondisi
  [X] Preprocessing setara
  [X] Tuning effort setara
  [X] Environment identik
  [X] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Variasi hasil acak karena inisialisasi random seed pada algoritma LDA. | Mengeksekusi pipeline minimal 5 kali (multiple runs) dengan seed berbeda dan merata-ratakan hasilnya. |
| External    | Topik keluhan hanya berlaku untuk update UI SeaBank bulan ini, tidak bisa digeneralisasi untuk bulan depan. | Menarik dataset (scraping) dengan rentang waktu minimal 6 bulan terakhir. |
| Construct   | Coherence Score (metrik matematis) tinggi, tetapi kata-katanya tidak bisa dipahami oleh manusia (developer). | Melakukan inspeksi kualitatif (sanity check) secara manual pada klaster kata yang dihasilkan. |
| Conclusion  | Mengandalkan single run (1 kali eksekusi) yang kebetulan beruntung mendapatkan skor bagus. | Uji statistik pada distribusi skor dari 10 run eksperimen. |

Statistical Plan:
  Uji statistik   : Independent Sample T-Test (atau Mann-Whitney U Test jika distribusi tidak normal).
  Justifikasi     : Bertujuan untuk membandingkan rata-rata (mean) Coherence Score antara kelompok Control (tanpa K-NN) dan kelompok Treatment (dengan K-NN) dari hasil multiple runs.
  Alpha           : 0.05 (Tingkat signifikansi 5%)
  Effect size min : Cohen's d > 0.5 (Medium effect size)
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah terdapat korelasi yang signifikan antara rasio sentimen negatif publik (berbasis K-NN) dengan metrik performa objektif (Skor SUS & Task Success Rate) pada aplikasi SeaBank?
**Tipe eksperimen:** [X] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Evaluasi Objektif via Eksperimen (Standar Baseline)   | Skor SUS & Task Success Rate | Lingkungan tertutup, 30 responden, skenario terstruktur |
| Treatment | Evaluasi Subjektif via Social Listening (Metode Usulan) | Rasio Sentimen Positif/Negatif (K-NN) | Lingkungan natural, ekstraksi 1000 ulasan Play Store pada periode yang sama |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Menggunakan periode waktu yang sama. Partisipan menguji SeaBank versi 2.4, dan ulasan yang ditarik khusus untuk versi 2.4 saja. |
| Preprocessing setara | ✅ | Ulasan spam/bot dibuang (K-NN); partisipan yang tidak menyelesaikan kuesioner dibuang (SUS). |
| Tuning effort setara | ✅ | Optimasi hyperparameter K pada K-NN diimbangi dengan pilot testing (uji coba awal) skenario tugas SUS agar setara kualitasnya. |
| Environment identik | ✅ | Keduanya mengevaluasi antarmuka pada platform Android. |
| Metrik evaluasi sama | ✅ | Keduanya dinormalisasi ke rentang rasio (0-100%) untuk memudahkan perbandingan korelasi. |

**Ada yang tidak fair?** [ ] Ya / [X] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Bias seleksi responden SUS (misal: hanya merekrut teman kampus). | Menggunakan purposive sampling berbasis kriteria nasabah riil SeaBank. |
| External | Hasil korelasi hanya berlaku untuk SeaBank, tidak bisa digeneralisasi ke bank digital lain. | Mengakui batasan ini di laporan riset, atau menambah aplikasi pembanding jika waktu memungkinkan. |
| Construct | Ulasan bintang 5 di Play Store terkadang berisi teks keluhan, mengecoh sentimen K-NN. | Menggunakan isi teks sebagai fitur latih K-NN, bukan rating bintangnya. |
| Conclusion | Kesalahan asumsi distribusi data saat uji statistik. | Uji normalitas (Shapiro-Wilk) sebelum memilih antara Pearson atau Spearman. |

**Ancaman mana yang paling sulit dimitigasi?** Construct Validity pada pemrosesan sentimen ulasan.
**Mengapa?**
> Bahasa ulasan di Play Store sering kali tidak baku, penuh singkatan, typo, dan sarkasme. Sekalipun K-NN sudah dilatih dengan baik, selalu ada margin error klasifikasi yang bisa mendistorsi rasio sentimen dan melemahkan tingkat korelasi dengan skor SUS yang murni objektif.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah dataset, parameter environment, dan metrik evaluasi yang digunakan benar-benar identik antara metode usulan dengan baseline?
2. Apakah tuning effort (hyperparameter optimization) yang diberikan pada metode baseline setara dengan metode yang diusulkan, atau baseline dibiarkan menggunakan pengaturan bawaan (default)?
3. Apakah baseline yang dikalahkan merupakan State-of-the-Art (SOTA) yang relevan dan terkini, atau sekadar straw man (metode usang yang sengaja dipilih agar mudah dikalahkan)?