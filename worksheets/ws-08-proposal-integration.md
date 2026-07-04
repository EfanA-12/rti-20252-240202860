# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [X] Problem → Gap: masalah terdokumentasi di literatur
  [X] Gap → RQ: pertanyaan menjawab gap spesifik
  [X] RQ → Hypothesis: hipotesis memprediksi jawaban
  [X] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [X] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [X] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [X] Istilah sama di semua bagian
  [X] Variabel di RQ = variabel di hipotesis = metrik di desain
  [X] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [X] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [X] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [X] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [X] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [X] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor |
|----------|-----------|-----------|----------|------|
| Koherensi |          |           |     X     |      |
| Specificity |        |           |     X     |      |
| Feasibility |        |           |     X     |      |
| Rigor     |          |           |     X     |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Terdapat banyak keluhan UI/UX mengenai aplikasi SeaBank di ulasan Play Store, namun keluhan tersebut belum pernah divalidasi kebenarannya melalui pengujian usability yang objektif. |
| Gap | WS-03 | Belum ada studi yang melakukan triangulasi metode antara analisis sentimen publik secara real-time dengan pengujian performa usability secara eksperimental pada aplikasi branchless banking. |
| RQ | WS-04 | Apakah terdapat korelasi yang signifikan antara rasio sentimen negatif (K-NN) di Play Store dengan metrik objektif (Skor SUS & Task Success Rate) pada aplikasi SeaBank? |
| Hipotesis | WS-04 | H₁: Terdapat korelasi yang signifikan (p-value < 0.05) antara rasio sentimen ulasan publik dengan performa usability objektif pada SeaBank. |
| Variabel & Metrik | WS-05 | IV = Sentimen Publik (Rasio %); DV = Performa Objektif (Skor SUS & Persentase Success Rate). |
| Sistem | WS-06 | Skrip Python pemroses NLP (K-NN) untuk membedah data ulasan, dan platform kuesioner otomatis untuk merekam skor SUS dari partisipan eksperimen. |
| Desain Eksperimen | WS-07 | Studi komparatif/korelasional antara data 1000+ ulasan (periode X) dengan hasil uji 30 partisipan (versi aplikasi yang sama) menggunakan uji korelasi Spearman. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Keluhan pengguna tidak tervalidasi → Dibuktikan di literatur bahwa triangulasi belum pernah dilakukan. |
| Gap → RQ | ✅ | Celah triangulasi langsung dijawab oleh rumusan masalah yang membandingkan/mengkorelasi metode subjektif (Sentimen) vs objektif (SUS). |
| RQ → Hypothesis | ✅ | Pertanyaan korelasi diwujudkan dalam prediksi H₁ yang terukur dengan threshold p-value < 0.05. |
| Hypothesis → Metric | ✅ | Metrik dikunci: p-value didapat dari uji korelasi antara skor Sentimen K-NN (Ratio) dan Skor SUS (Interval). |
| Metric → System | ✅ | Skor K-NN (rasio sentimen) dihasilkan oleh skrip Python, skor SUS dikalkulasi otomatis oleh form kuesioner. |
| System → Experiment | ✅ | Eksperimen dilakukan dengan mengambil output algoritma (skrip) dan membenturkannya dengan output usability testing di lingkungan yang terkontrol (versi aplikasi yang sama). |

**Koneksi mana yang paling lemah?** System → Experiment.
**Bagaimana cara memperkuatnya?**
> Memastikan bahwa data ulasan Play Store yang disedot algoritma K-NN benar-benar direntang waktu yang identik dengan versi UI aplikasi yang digunakan partisipan saat eksperimen usability, agar perbandingannya benar-benar apple-to-apple.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [X] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Seluruh koneksi dari perumusan masalah (SeaBank) hingga metode korelasi sudah mengalir menjadi satu argumen utuh. |
| Specificity | 3 | Metrik sudah memiliki angka yang konkret: rasio sentimen (%), Skor SUS (0-100), dan threshold p-value (0.05). |
| Feasibility | 3 | Desain eksperimen menggunakan 30 partisipan dan analisis data sekunder sangat relevan diselesaikan dalam kurun waktu 1-3 bulan (timeline realistis). |
| Rigor | 3 | Menggunakan baseline instrumen baku (System Usability Scale) dan metode yang direplikasi dari kondisi State-of-the-Art. |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [X] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Mengidentifikasi masalah (Problem Statement) pada WS-02, karena fenomena terkait keluhan aplikasi perbankan digital sangat nyata dan mudah ditemukan symptom-nya secara empiris.
**Bagian tersulit:** Merumuskan desain sistem ke dalam eksperimen (System-Experiment Mapping di WS-06 dan WS-07), karena saya harus mengubah pola pikir engineering (membuat produk) menjadi pola pikir research (membuat instrumen pembuktian/artefak).
**Yang akan dilakukan berbeda:**
> Saya akan menghabiskan lebih banyak waktu di tahap Literature Mapping (WS-03) untuk benar-benar mencari State-of-the-Art yang paling presisi. Awalnya saya sempat kesulitan merumuskan baseline sebelum mengadopsi System Usability Scale, karena sering terjebak membandingkan dengan metode yang lemah (straw man comparison). Ke depannya, saya akan lebih ketat dalam menyusun Boolean query untuk mencari literatur yang benar-benar relevan sebelum melangkah ke penentuan variabel.