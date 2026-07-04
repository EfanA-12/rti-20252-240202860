# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Data Science / Natural Language Processing (NLP)
  Konteks  : Otomatisasi ekstraksi topik keluhan usability pada aplikasi SeaBank melalui penambangan data teks (text mining) berbasis Machine Learning.

System Context
  Input       : Data sekunder tidak terstruktur (unstructured data) berupa ribuan ulasan pengguna dari Google Play Store.
  Process     : Pra-pemrosesan teks (NLP), klasifikasi sentimen menggunakan K-Nearest Neighbor (K-NN), dan pemodelan topik menggunakan Latent Dirichlet Allocation (LDA).
  Output      : Metrik performa klasifikasi (Accuracy, F1-Score), skor koherensi (Coherence Score), dan klaster topik keluhan pengguna.
  Outcome     : Pipeline otomatis yang mampu memetakan titik masalah (friction points) UI/UX secara instan tanpa perlu membaca ulasan secara manual.
  Constraints : Tingginya noise pada data ulasan publik (typo, slang, singkatan, bot) dan sifat kelas data yang sering kali tidak seimbang (imbalanced data).
  Stakeholders: Tim Pengembang (Developer) SeaBank, UI/UX Researcher, dan Analis Data.

Fenomena → Problem
  Fenomena yang diamati             : Aplikasi perbankan digital menerima ribuan ulasan harian di Play Store yang berisi masukan berharga terkait usability.
  Gejala (symptom) yang terukur     : Pihak pengembang kesulitan melacak fitur apa yang paling sering bermasalah karena data keluhan tercampur aduk dengan pujian dan komentar tidak relevan dalam format teks bebas.
  Masalah yang didiagnosis          : Tidak adanya sistem otomatisasi yang mampu secara akurat menyeleksi ulasan bersentimen negatif dan mengekstrak topik utamanya secara sistematis.
  Masalah riset (researchable)      : Belum diketahui seberapa tinggi tingkat akurasi K-NN dalam memisahkan sentimen ulasan SeaBank, serta seberapa koheren topik keluhan usability yang mampu diekstrak oleh model LDA dari ulasan negatif tersebut.
  Variabel yang terukur             : Performa K-NN (Accuracy, Precision, Recall, F1-Score) dan performa LDA (Coherence Score c_v).

Problem Quality Check
  [X] Clarity — Apakah satu orang membaca akan paham?
  [X] Measurability — Apakah ada metrik kuantitatif?
  [X] Relevance — Apakah penting untuk domain?
  [X] Testability — Apakah bisa gagal?
  [X] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Dalam ekosistem perbankan digital seperti SeaBank, ulasan pengguna di Google Play Store merupakan sumber data yang sangat kaya untuk mengevaluasi usability antarmuka. Namun, volume ulasan yang mencapai ribuan setiap harinya membuat analisis manual menjadi tidak efisien, sehingga keluhan spesifik terkait fitur sering kali terabaikan karena tertimbun oleh data teks yang tidak terstruktur (unstructured). Masalah utamanya adalah ketiadaan pipeline otomatis yang mampu menyeleksi dan mengelompokkan keluhan tersebut secara akurat. Oleh karena itu, penelitian ini bertujuan untuk membangun dan menguji kinerja model berbasis algoritma K-Nearest Neighbor (K-NN) untuk mengklasifikasikan sentimen, dipadukan dengan Latent Dirichlet Allocation (LDA) untuk mengekstrak topik keluhan utama. Hasil riset ini diharapkan mampu memberikan bukti empiris mengenai keandalan kedua algoritma tersebut dalam mengotomatisasi pemetaan masalah usability secara cepat dan presisi.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Evaluasi Usability Aplikasi Digital Banking SeaBank.

| Tahap | Hasil |
|-------|-------|
| Reality | Aplikasi SeaBank mendapatkan ribuan ulasan teks setiap bulan yang berisi feedback terkait kenyamanan penggunaan (UI/UX) aplikasinya. |
| Observed Issue (Symptom) | Pengembang kesulitan mengidentifikasi bagian mana dari aplikasi yang paling bermasalah karena teks keluhan (bug, UI membingungkan, dsb.) bercampur menjadi satu. |
| Diagnosed Problem (Root Cause) | Tidak ada metode ekstraksi otomatis; data bersifat teks tidak terstruktur (unstructured) yang penuh dengan noise (bahasa slang, singkatan). |
| Researchable Problem | Mampukah algoritma K-NN mengklasifikasikan sentimen ulasan dengan akurat, dan mampukah LDA mengelompokkan teks sentimen negatif tersebut menjadi topik keluhan usability yang koheren secara otomatis?   |
| Measurable Variable | Accuracy, F1-Score (untuk K-NN), dan Coherence Score (untuk LDA). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data mentah ulasan pengguna SeaBank hasil scraping dari Google Play Store. |
| Process | Text preprocessing (Pembersihan teks), pembobotan kata (TF-IDF), pelatihan model klasifikasi K-NN, dan iterasi pemodelan topik LDA. |
| Output | Label sentimen pada setiap ulasan (Positif/Negatif) dan daftar kata kunci (keywords) yang membentuk klaster topik keluhan. |
| Outcome | Sebuah pipeline atau purwarupa analisis yang dapat membantu tim SeaBank mengetahui inti masalah usability tanpa harus membaca data satu per satu. |
| Constraints | Tingginya noise pada gaya bahasa netizen Indonesia dan risiko kelas data sentimen yang tidak seimbang (imbalanced data). |
| Stakeholders | Data Scientist, Tim Developer/UI-UX SeaBank. |

**Komponen mana yang paling relevan dengan masalah riset?** Process dan Output, karena riset ini berfokus murni pada evaluasi performa algoritma saat memproses data (Process) hingga menghasilkan metrik ukur yang valid (Output).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas: Tujuannya menguji K-NN untuk sentimen dan LDA untuk ekstraksi topik. |
| Measurability | 5 | Menggunakan metrik evaluasi Machine Learning yang standar (Accuracy, Coherence). |
| Relevance | 5 | Sangat relevan di bidang Data Science terapan untuk otomatisasi deteksi masalah perangkat lunak. |
| Testability | 5 | Dapat diuji langsung dengan menjalankan eksperimen komputasi berulang. Hasilnya bisa gagal (misal: Coherence Score sangat rendah). |
| Impact | 5 | Menawarkan efisiensi waktu yang masif bagi pihak developer dalam menganalisis keluhan pengguna. |

**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**
> Dalam ekosistem perbankan digital seperti SeaBank, ulasan pengguna di Google Play Store merupakan sumber data yang sangat kaya untuk mengevaluasi usability antarmuka. Namun, volume ulasan yang mencapai ribuan setiap harinya membuat analisis manual menjadi tidak efisien, sehingga keluhan spesifik terkait fitur sering kali terabaikan karena tertimbun oleh data teks yang tidak terstruktur (unstructured). Masalah utamanya adalah ketiadaan pipeline otomatis yang mampu menyeleksi dan mengelompokkan keluhan tersebut secara akurat. Oleh karena itu, penelitian ini bertujuan untuk membangun dan menguji kinerja model berbasis algoritma K-Nearest Neighbor (K-NN) untuk mengklasifikasikan sentimen, dipadukan dengan Latent Dirichlet Allocation (LDA) untuk mengekstrak topik keluhan utama. Hasil riset ini diharapkan mampu memberikan bukti empiris mengenai keandalan kedua algoritma tersebut dalam mengotomatisasi pemetaan masalah usability secara cepat dan presisi.
---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah coding (seperti error saat membuat skrip scraping atau bug pada antarmuka aplikasi) menuntut solusi praktis agar sistem kembali berjalan normal (solve). Sebaliknya, masalah riset menuntut pembuktian empiris atas fenomena yang belum diketahui nilainya (understand & prove). Misalnya, masalah coding adalah "bagaimana cara agar skrip Python tidak crash", sedangkan masalah riset saya adalah "seberapa tinggi akurasi dan koherensi topik yang dihasilkan algoritma K-NN dan LDA saat dihadapkan pada data ulasan yang penuh dengan noise?".