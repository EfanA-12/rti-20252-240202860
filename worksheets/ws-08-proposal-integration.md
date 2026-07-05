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
| Problem Statement | WS-02 | Pengembang SeaBank kesulitan memetakan keluhan antarmuka secara spesifik karena tingginya volume ulasan tak terstruktur yang masuk di Play Store setiap hari. |
| Gap | WS-03 | BBelum ada studi yang merangkai pipeline di mana K-NN digunakan sebagai filter sentimen negatif sebelum diekstrak menjadi topik keluhan usability oleh LDA. |
| RQ | WS-04 | Apakah penggunaan K-NN sebagai filter sentimen negatif mampu menghasilkan topik keluhan usability yang koheren (Cv > 0.4) menggunakan model LDA pada ulasan SeaBank? |
| Hipotesis | WS-04 | H₁: Penggunaan K-NN sebagai filter sentimen negatif menghasilkan pemodelan topik keluhan yang koheren (Cv > 0.4) pada model LDA aplikasi SeaBank. |
| Variabel & Metrik | WS-05 | IV = K-NN Filter (ON/OFF); DV = Kualitas Topik; Metrik = Coherence Score (Cv) dan F1-Score. |
| Sistem | WS-06 | Pipeline script Python modular yang terdiri dari fungsi scraper, pra-pemrosesan teks, klasifikasi K-NN, dan pemodelan LDA berbasis Gensim. |
| Desain Eksperimen | WS-07 | Ablation Study yang membandingkan performa Coherence Score LDA saat memproses seluruh data (Baseline) melawan LDA yang hanya memproses data tersaring K-NN (Treatment). |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Keluhan tertimbun volume data besar $\rightarrow$ literatur menunjukkan belum ada ekstraksi topik spesifik (K-NN + LDA) untuk membedah tumpukan tersebut. |
| Gap → RQ | ✅ | Celah ketiadaan pipeline integrasi dijawab dengan pertanyaan yang menguji performa integrasi tersebut. |
| RQ → Hypothesis | ✅ | Pertanyaan koherensi diwujudkan dalam prediksi H₁ yang menetapkan angka Coherence Score spesifik (Cv > 0.4). |
| Hypothesis → Metric | ✅ | Koherensi diukur menggunakan standar baku Gensim Coherence Score (Cv). |
| Metric → System | ✅ |Nilai Cv dan F1-Score dikalkulasi dan di-log secara otomatis oleh fungsi Python. |
| System → Experiment | ✅ | Script Python digunakan untuk mengeksekusi iterasi Ablation Study (mematikan/menghidupkan filter K-NN lewat config file). |

**Koneksi mana yang paling lemah?** Hypothesis → Metric.
**Bagaimana cara memperkuatnya?**
> Metrik Coherence Score bersifat matematis dan terkadang tidak mencerminkan koherensi semantik yang sesungguhnya di mata manusia. Untuk memperkuat metrik ini, saya perlu menambahkan langkah validasi manual (Human-in-the-Loop) di akhir eksperimen untuk memastikan klaster kata (misal: "susah", "login", "otp") benar-benar masuk akal sebagai satu kalimat keluhan.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [X] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Alur logis dari masalah penumpukan keluhan, gap di NLP, hingga eksperimen Ablation Study mengalir sempurna. |
| Specificity | 3 | Memiliki batasan metrik komputasional yang tegas (Coherence Score > 0.4). |
| Feasibility | 3 | Riset 100% menggunakan data sekunder publik dan library Python open-source, sangat realistis selesai dalam 1-2 bulan. |
| Rigor | 3 | Menggunakan metode validasi Machine Learning yang standar (multiple runs, parameter configuration). |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [X] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Mengidentifikasi masalah pada WS-02, karena fenomena keluhan aplikasi di Google Play Store sangat mudah diobservasi dan tersedia secara publik (tidak perlu perizinan khusus untuk mengakses datanya).
**Bagian tersulit:** Merumuskan desain eksperimen komparatif di WS-07, karena saya harus mengubah mindset dari sekadar "membuat program K-NN yang jalan" menjadi "merancang skenario pengujian untuk membuktikan seberapa besar pengaruh K-NN tersebut terhadap kinerja LDA".
**Yang akan dilakukan berbeda:**
> Saya akan jauh lebih teliti dan strict (ketat) saat melakukan tahap pencarian literatur di WS-03. Awalnya saya sempat keliru merancang riset korelasi dengan manusia yang justru menyulitkan diri sendiri. Ke depannya, saya akan memastikan Boolean Query yang saya cari benar-benar berfokus pada metode komputasional (seperti "K-NN" AND "Topic Modeling") agar metodologinya tetap berada dalam kendali Data Science yang terukur murni lewat kode program.