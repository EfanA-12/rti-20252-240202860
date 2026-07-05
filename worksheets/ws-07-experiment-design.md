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

**RQ:**Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang koheren (Coherence Score c_v >= 0.4) menggunakan model LDA pada ulasan aplikasi SeaBank?
**Tipe eksperimen:** [ ] Comparison / [X] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Ekstraksi topik pada seluruh data mentah (Baseline)   | K-NN Filter = OFF | TF-IDF diaktifkan, jumlah topik (K)=5, Random State = 42 |
| Treatment | Ekstraksi topik khusus pada data tersaring | K-NN Filter = ON | TF-IDF diaktifkan, jumlah topik (K)=5, Random State = 42 |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Keduanya menggunakan file ulasan SeaBank (.csv) dari periode scraping yang sama persis. |
| Preprocessing setara | ✅ | Kedua kondisi sama-sama melalui tahap case folding, stopword removal, dan stemming. |
| Tuning effort setara | ✅ | Jumlah target topik pada LDA (K-topics) dikunci pada angka yang sama untuk memastikan perbandingannya apple-to-apple. |
| Environment identik | ✅ | Berjalan di dalam satu script Python yang sama, di atas sistem operasi (Windows 11) dan spesifikasi laptop yang sama (Advan Workplus). |
| Metrik evaluasi sama | ✅ | Kinerja ekstraksi topik diukur murni berdasarkan Coherence Score (Cv) bawaan dari library Gensim. |

**Ada yang tidak fair?** [ ] Ya / [X] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Kebocoran data (Data Leakage) saat memisahkan train-test split pada pengujian algoritma K-NN. | Menggunakan Stratified K-Fold Cross Validation agar rasio kelas positif/negatif seimbang. |
| External | Teks ulasan sangat bergantung pada event SeaBank (misal: promo mengundang teman), sehingga topik keluhan UI/UX tertutup keluhan promo. | Menambahkan daftar filter stopword kustom (contoh: hapus kata "kode", "referral", "cuan"). |
| Construct | Metrik Coherence Score secara matematis bagus, tapi maknanya bias. | Melibatkan inspeksi pakar (diri sendiri sebagai peneliti) untuk menamai klaster topik secara logis. |
| Conclusion | Menyimpulkan LDA sukses atau gagal hanya dari 1 kali run (eksekusi program). | Menerapkan multiple runs (minimal 5 kali iterasi program) dengan seed berbeda. |

**Ancaman mana yang paling sulit dimitigasi?** Construct Validity pada penilaian Coherence Score.
**Mengapa?**
> Karena dalam algoritma Unsupervised Learning seperti LDA, tidak ada label kebenaran mutlak (tidak ada "kunci jawaban"). Mesin hanya mengelompokkan kata yang sering muncul bersama. Meskipun metrik $C_v$ tinggi, selalu ada subjektivitas manusia saat berusaha menamai (menginterpretasi) kumpulan kata tersebut menjadi sebuah kalimat masalah UI/UX yang masuk akal.
---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah dataset, parameter environment, dan metrik evaluasi yang digunakan benar-benar identik (seimbang) antara metode usulan dengan baseline?
2. Apakah tuning effort (hyperparameter optimization) yang diberikan pada metode baseline setara dengan metode yang diusulkan, atau baseline justru dibiarkan lemah menggunakan pengaturan bawaan (default)?
3. Apakah baseline yang dikalahkan merupakan State-of-the-Art (SOTA) yang relevan dan terkini di ranah Machine Learning, atau sekadar straw man (algoritma usang yang sengaja dipilih agar mudah dikalahkan)?