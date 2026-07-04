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

Domain & Konteks
  Domain   : Human-Computer Interaction (HCI) / Evaluasi Usability Antarmuka Aplikasi Digital Banking
  Konteks  : Validasi tingkat kebergunaan (usability) aplikasi SeaBank melalui pendekatan hibrida (objektif & subjektif).
System Context
  Input       : Data interaksi pengguna (hasil task scenario) dan data sekunder berupa ulasan pengguna dari Google Play Store.
  Process     : Evaluasi performa navigasi aplikasi (Task Scenario) dan analisis sentimen terhadap ulasan publik untuk memetakan friction points.
  Output      : Metrik usability kuantitatif (Skor SUS, Success Rate) dan klasifikasi sentimen pengguna (Positif/Negatif).
  Outcome     : Dokumen bukti empiris tingkat kelayakan usability serta rekomendasi teknis perbaikan antarmuka yang ramah pengguna.
  Constraints : Data ulasan publik yang bersifat tidak terstruktur (unstructured data) dan batasan akses terhadap log internal aplikasi.
  Stakeholders: Nasabah SeaBank, Tim UI/UX Designer SeaBank, dan Pengembang platform digital.

Fenomena → Problem
  Fenomena yang diamati             : Aplikasi perbankan digital menuntut antarmuka yang sangat intuitif untuk menjaga efisiensi transaksi nasabah.
  Gejala (symptom) yang terukur     : Munculnya keluhan pada ulasan publik Google Play Store mengenai alur transaksi yang kompleks dan skor usability yang belum teruji secara empiris.
  Masalah yang didiagnosis          : Adanya ketidaksesuaian antara struktur antarmuka fitur utama dengan mental model pengguna yang memicu beban kognitif tinggi.
  Masalah riset (researchable)      : Belum ada validasi apakah persepsi positif/negatif publik di Google Play Store berkorelasi dengan hasil pengujian performa usability yang objektif.
  Variabel yang terukur             : Skor System Usability Scale (SUS), Task Success Rate, dan Persentase Sentimen Ulasan (Positif/Negatif).

Problem Quality Check
  [X] Clarity — Apakah satu orang membaca akan paham?
  [X] Measurability — Apakah ada metrik kuantitatif?
  [X] Relevance — Apakah penting untuk domain?
  [X] Testability — Apakah bisa gagal?
  [] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Pergeseran layanan keuangan ke arah bank digital murni menuntut tingkat kebergunaan (usability) antarmuka yang sangat tinggi. Meskipun aplikasi SeaBank memiliki basis pengguna yang besar, muncul banyak keluhan di Google Play Store mengenai kerumitan alur navigasi pada fitur esensial, namun keluhan tersebut belum pernah divalidasi secara empiris melalui pengujian objektif. Adanya kesenjangan antara sentimen publik dan performa nyata pengguna ini menimbulkan ketidakpastian mengenai tingkat kelayakan desain aplikasi tersebut. Oleh karena itu, penelitian ini bertujuan untuk memvalidasi usability aplikasi SeaBank melalui studi komparatif antara pengujian Task Scenario (performa objektif) dan analisis sentimen ulasan publik (persepsi subjektif) guna menghasilkan rekomendasi perbaikan desain antarmuka yang berbasis bukti.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Evaluasi Usability Aplikasi Digital Banking SeaBank.

| Tahap | Hasil |
|-------|-------|
| Reality | Aplikasi bank digital murni seperti SeaBank menjadi kanal utama transaksi nasabah tanpa kantor cabang, sehingga kualitas antarmuka sangat menentukan kepercayaan dan loyalitas nasabah. |
| Observed Issue (Symptom) | Adanya keluhan nasabah pada ulasan Google Play Store mengenai kompleksitas fitur deposito dan kesulitan pelacakan mutasi, serta hasil riset awal yang menunjukkan skor usability yang masih marginal. |
| Diagnosed Problem (Root Cause) | Terdapat celah (gap) antara rancangan UI/UX aplikasi dengan mental model pengguna awam, sehingga memicu beban kognitif (cognitive load) berlebih yang menghambat efisiensi tugas. |
| Researchable Problem | Belum adanya validasi empiris yang membandingkan performa usability objektif (Task Scenario) dengan persepsi sentimen subjektif (ulasan Google Play Store) untuk mengonfirmasi kelayakan desain aplikasi SeaBank.   |
| Measurable Variable | Task Success Rate (%), Time-based Efficiency (detik), skor SUS (0-100), dan skor sentimen ulasan (positif/negatif). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [ ] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Aksi interaksi pengguna (klik, scroll, pengisian formulir) selama skenario tugas, serta data mentah ulasan pengguna dari Google Play Store. |
| Process | Evaluasi efektivitas dan efisiensi melalui Task Scenario serta klasifikasi sentimen menggunakan algoritma pemrosesan teks pada data ulasan. |
| Output | Metrik usability kuantitatif (Success Rate, waktu, skor SUS) dan klasifikasi sentimen publik (positif, netral, atau negatif). |
| Outcome | Teridentifikasinya pain points (titik masalah) pada UI SeaBank dan rekomendasi perbaikan desain yang berbasis pada validasi data objektif dan subjektif. |
| Constraints | Keterbatasan akses ke log aktivitas internal aplikasi, serta adanya noise atau komentar tidak relevan pada data ulasan publik. |
| Stakeholders | Nasabah SeaBank sebagai pengguna, tim UI/UX Designer SeaBank, serta peneliti (Anda). |

**Komponen mana yang paling relevan dengan masalah riset?** Outcome, karena tujuan utama dari riset ini adalah untuk menghasilkan bukti empiris (validasi) mengenai kelayakan desain antarmuka aplikasi melalui penggabungan data performa dan persepsi publik.

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Masalah sangat jelas: memvalidasi usability melalui triangulasi data antara performa objektif dan sentimen subjektif pada SeaBank. |
| Measurability | 5 | Menggunakan metrik kuantitatif terukur yaitu skor SUS, task success rate, waktu, dan klasifikasi sentimen. |
| Relevance | 5 | Sangat relevan karena aplikasi perbankan digital murni bergantung sepenuhnya pada UI/UX sebagai kanal interaksi nasabah. |
| Testability | 4 | Dapat diuji melalui eksperimen task scenario dan analisis data sekunder dari Google Play Store. |
| Impact | 5 | Memberikan kontribusi berupa bukti empiris dan rekomendasi desain berbasis data bagi pihak SeaBank. |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
> Pergeseran layanan keuangan ke arah bank digital murni menuntut tingkat kebergunaan (usability) antarmuka yang sangat tinggi. Meskipun aplikasi SeaBank memiliki basis pengguna yang besar, muncul banyak keluhan di Google Play Store mengenai kerumitan alur navigasi pada fitur esensial, namun keluhan tersebut belum pernah divalidasi secara empiris melalui pengujian objektif. Adanya kesenjangan antara sentimen publik dan performa nyata pengguna ini menimbulkan ketidakpastian mengenai tingkat kelayakan desain aplikasi tersebut. Oleh karena itu, penelitian ini bertujuan untuk memvalidasi usability aplikasi SeaBank melalui studi komparatif antara pengujian Task Scenario (performa objektif) dan analisis sentimen ulasan publik (persepsi subjektif) guna menghasilkan rekomendasi perbaikan desain antarmuka yang berbasis bukti.
---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah coding bertujuan memperbaiki bug agar sistem berjalan (solve), sementara masalah riset bertujuan membuktikan fenomena secara empiris (understand & prove) melalui instrumen ilmiah seperti SUS dan analisis sentimen, bukan sekadar membenahi kode.
