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

Research Question : Apakah tingkat kepuasan (SUS) dan keberhasilan tugas (success rate) pada antarmuka aplikasi SeaBank melampaui standar kelayakan rata-rata industri?
Hypothesis        : H1 = Rata-rata skor SUS aplikasi SeaBank > 68 (Signifikan melampaui standar kelayakan).
Tipe Eksperimen   : [X] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Standar kelayakan industri (Baseline) | Skor referensi (SUS 68) | - (Nilai referensi statis / baku) |
| Treatment | Pengujian langsung aplikasi SeaBank | UI/UX SeaBank | Smartphone seragam, koneksi stabil, skenario task identik |

Fairness Checklist:
  [X] Dataset identik untuk semua kondisi (Semua partisipan diuji dengan task yang sama)
  [X] Preprocessing setara (Instruksi dan ice breaking disamakan untuk semua partisipan)
  [X] Tuning effort setara (Tidak ada manipulasi bantuan teknis saat partisipan kesulitan)
  [X] Environment identik (Pengujian di lab/ruangan tenang yang sama)
  [X] Metrik evaluasi sama (Menggunakan kuesioner SUS yang baku)

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Partisipan kelelahan (fatigue effect) karena task terlalu banyak. | Membatasi durasi total pengujian maksimal 15-20 menit per orang. |
| External    | Sampel hanya terdiri dari mahasiswa IT, tidak merepresentasikan nasabah asli. | Menerapkan kriteria inklusi (purposive sampling) yang mencakup berbagai usia dan profesi. |
| Construct   | Partisipan menjawab kuesioner SUS asal-asalan karena merasa sungkan dengan peneliti (Hawthorne Effect). | Menegaskan di awal bahwa yang diuji adalah *aplikasi*, bukan *kecerdasan partisipan*, dan kuesioner bersifat anonim. |
| Conclusion  | Ukuran sampel terlalu kecil sehingga tidak memiliki statistical power yang cukup. | Menggunakan minimal 20-30 partisipan aktif agar distribusi data mendekati normal untuk uji parametrik. |

Statistical Plan:
  Uji statistik   : One-Sample T-Test (Uji-T Satu Sampel)
  Justifikasi     : Karena kita membandingkan nilai rata-rata dari satu kelompok perlakuan (SeaBank) terhadap satu nilai acuan pasti/konstan (Baseline SUS 68).
  Alpha           : 0.05 (Tingkat kepercayaan 95%)
  Effect size min : Cohen's d > 0.5 (Medium effect size)
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** __________________________________________________
**Tipe eksperimen:** [ ] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Nilai acuan standar usability dari Sauro & Lewis (2011) sebagai baseline. | Threshold SUS = 68 | Nilai baku. |
| Treatment | Observasi task scenario dan pengisian kuesioner pada aplikasi SeaBank. | Antarmuka SeaBank | Skenario tugas, smartphone Android/iOS yang dikondisikan, timer maks 3 menit per task. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ Fair | Semua pengguna menyelesaikan urutan skenario tugas (Task A, B, C) yang persis sama tanpa ada yang dibedakan. |
| Preprocessing setara | ✅ Fair | Semua partisipan diberikan briefing awal yang sama persis (menggunakan teks script) sebelum eksperimen dimulai. |
| Tuning effort setara | ✅ Fair | Fasilitator (peneliti) dilarang memberikan hint atau bantuan apa pun saat partisipan kebingungan memencet menu. |
| Environment identik | ✅ Fair | Seluruh pengujian dilakukan di lingkungan fisik yang tenang, dengan tingkat kecerahan layar HP yang disamakan. |
| Metrik evaluasi sama | ✅ Fair | Semua menggunakan kuesioner baku System Usability Scale berisi 10 pertanyaan standar yang tidak dimodifikasi isinya. |

**Ada yang tidak fair?** [ ] Ya / [X] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Learning Effect: Partisipan menjadi lebih cepat di task kedua hanya karena sudah terbiasa memegang device tes. | Memberikan waktu 2 menit di awal bagi partisipan untuk sekadar melakukan scroll bebas agar terbiasa dengan layar HP yang digunakan. |
| External | Demografi sampel yang terlalu sempit (misalnya hanya mengambil sampel usia 18-22 tahun). | Melakukan rekrutmen partisipan secara purposive untuk mencakup rentang usia produktif yang lebih luas (18-40 tahun). |
| Construct | Hawthorne Effect / Social Desirability Bias: Partisipan merasa sedang diawasi dan ingin menyenangkan peneliti dengan memberi skor tinggi. | Memberi tahu responden bahwa tidak ada jawaban benar/salah, dan evaluasi ini adalah murni untuk mengkritik aplikasi bank. |
| Conclusion | Data berdistribusi tidak normal (outlier), membuat uji One-Sample T-Test menjadi tidak valid. | Melakukan uji normalitas (Shapiro-Wilk) terlebih dahulu. Jika tidak normal, gunakan uji non-parametrik Wilcoxon Signed-Rank Test. |

**Ancaman mana yang paling sulit dimitigasi?** Construct Validity (Social Desirability Bias / Hawthorne Effect)
**Mengapa?**
> Karena dalam pengujian usability tatap muka, kehadiran peneliti di sebelah partisipan secara psikologis sering kali membuat partisipan merasa "sedang diuji kecerdasannya". Rasa tidak enak hati ini sering membuat pengguna secara otomatis mengisi kuesioner dengan nilai bagus, meskipun mereka tadi kesulitan (berbohong demi kesopanan). Hal ini paling sulit dikontrol karena murni masalah emosi manusia.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah perbandingannya jujur (fair)? Apakah baseline yang digunakan adalah baseline usang/lemah yang sengaja dipilih agar metode mereka terlihat bagus, alias Straw Man Comparison?
2. Apakah lingkungan dan kondisinya setara? Apakah metode mereka diuji menggunakan dataset, parameter, dan batasan hardware yang persis sama dengan baseline-nya?
3. Apakah metrik yang digunakan benar? Apakah mereka hanya menonjolkan satu metrik yang kebetulan unggul (cherry-picking), sementara mengabaikan metrik lain yang mungkin lebih relevan namun hasilnya buruk?