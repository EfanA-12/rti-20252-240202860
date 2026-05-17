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
  Domain   : Human-Computer Interaction (HCI) / Evaluasi Usability Antarmuka Aplikasi
  Konteks  : Evaluasi kegunaan (usability) aplikasi bank digital SeaBank pada nasabah/pengguna aktif.

System Context
  Input       : Interaksi motorik pengguna (ketukan layar, input data) saat mengeksekusi task scenario pada aplikasi SeaBank.
  Process     : Proses navigasi pengguna di dalam antarmuka aplikasi untuk menyelesaikan tugas (misal: mencari riwayat transaksi lama, membuka deposito) serta pengisian kuesioner SUS di akhir sesi.
  Output      : Metrik usability kuantitatif berupa success rate (%), time-based efficiency (detik), error rate, dan skor kepuasan SUS (0-100).
  Outcome     : Teridentifikasinya celah usability (pain points) dan perumusan rekomendasi perbaikan desain UI/UX aplikasi SeaBank.
  Constraints : Jumlah sampel partisipan yang terbatas serta lingkungan pengujian yang dikondisikan (tidak sepenuhnya mencerminkan situasi pengguna di dunia nyata).
  Stakeholders: Nasabah aplikasi SeaBank (pengguna akhir) dan Tim Pengembang/UI-UX Designer SeaBank.

Fenomena → Problem
  Fenomena yang diamati             : Aplikasi bank digital seperti SeaBank dituntut memiliki antarmuka yang sangat intuitif karena ketiadaan kantor cabang fisik untuk melayani nasabah secara langsung.
  Gejala (symptom) yang terukur     : Munculnya berbagai keluhan dari pengguna terkait kebingungan saat mencari riwayat transaksi lama atau kesulitan memahami alur pembukaan fitur deposito.
  Masalah yang didiagnosis          : Hirarki navigasi dan penempatan label fitur pada antarmuka aplikasi kurang sesuai dengan mental model pengguna awam, sehingga memicu tingginya beban kognitif (cognitive load).
  Masalah riset (researchable)      : Seberapa besar tingkat efektivitas, efisiensi, dan kepuasan pengguna dalam menyelesaikan skenario tugas utama di aplikasi SeaBank secara empiris?
  Variabel yang terukur             : Tingkat keberhasilan tugas (Learnability), kecepatan penyelesaian (Efficiency), jumlah kesalahan (Error rate), dan skor kepuasan (Satisfaction).

Problem Quality Check
  [X] Clarity — Pembaca dapat langsung memahami bahwa masalahnya adalah keluhan navigasi pada SeaBank yang memicu beban kognitif, sehingga perlu dievaluasi.
  [X] Measurability — Menggunakan metrik kuantitatif yang jelas: persentase keberhasilan, waktu (detik), rasio kesalahan, dan skor SUS.
  [X] Relevance — Sangat relevan karena kelancaran UI/UX adalah ujung tombak retensi nasabah bagi sebuah bank digital (branchless banking).
  [X] Testability — Dapat diuji dan bisa gagal. Bisa saja hasil pengujian membuktikan bahwa UI SeaBank sebenarnya sudah sangat efisien dan keluhan yang ada hanya berasal dari anomali sebagian kecil pengguna.
  [X] Impact — Menghasilkan kontribusi praktis berupa data empiris kelemahan UI saat ini beserta rekomendasi redesign antarmuka untuk pihak SeaBank.

Problem Statement (1 paragraf):
Kehadiran bank digital seperti SeaBank menuntut antarmuka pengguna (UI/UX) yang sangat intuitif, mengingat seluruh layanan transaksi dilakukan tanpa intervensi fisik dari kantor cabang. Namun, observasi awal terhadap ulasan pengguna menunjukkan adanya gejala kesulitan dalam bernavigasi, seperti kebingungan saat melacak riwayat transaksi lama dan ketidakpahaman terhadap alur fitur deposito. Kesulitan tersebut mengindikasikan adanya celah pada hirarki informasi yang membebani kognitif pengguna (cognitive load) dan berisiko menurunkan kepercayaan nasabah. Mengingat belum adanya pengukuran empiris terkait kendala tersebut, penelitian ini bertujuan untuk mengevaluasi tingkat kegunaan (usability) aplikasi SeaBank secara kuantitatif melalui metode Usability Testing (mengukur aspek efektivitas dan efisiensi) serta kuesioner System Usability Scale (mengukur tingkat kepuasan). Hasil evaluasi ini akan digunakan sebagai landasan saintifik untuk merumuskan rekomendasi perbaikan desain antarmuka aplikasi SeaBank agar lebih sesuai dengan mental model penggunanya.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Evaluasi Tingkat Usability Aplikasi Bank Digital SeaBank Menggunakan Pendekatan Usability Testing dan System Usability Scale (SUS).

| Tahap | Hasil |
|-------|-------|
| Reality | Aplikasi bank digital (seperti SeaBank) menuntut antarmuka yang sangat intuitif karena berhubungan langsung dengan kelancaran dan keamanan transaksi finansial pengguna. |
| Observed Issue (Symptom) | Terdapat ulasan/keluhan dari pengguna (misal di Play Store/App Store atau forum) mengenai kebingungan saat mencari riwayat transaksi lama atau kesulitan memahami alur pembukaan fitur deposito. (Kamu bisa mengganti gejala ini dengan keluhan nyata yang kamu temukan). |
| Diagnosed Problem (Root Cause) | Hirarki navigasi atau penempatan label fitur pada antarmuka aplikasi kurang sesuai dengan mental model pengguna awam, sehingga memicu tingginya cognitive load (beban pikiran) saat bertransaksi. |
| Researchable Problem | Seberapa besar tingkat efektivitas, efisiensi, dan kepuasan pengguna (berdasarkan kerangka usability) dalam menyelesaikan skenario tugas utama di aplikasi SeaBank? |
| Measurable Variable | Tingkat keberhasilan tugas (success rate dalam %), waktu penyelesaian (time-based efficiency dalam detik), jumlah kesalahan (error rate), dan skor kepuasan SUS (skala 0-100). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Interaksi user (klik/sentuhan) pada antarmuka prototipe/aplikasi SeaBank, serta profil demografi user (usia, latar belakang perbankan). |
| Process | Pengguna melaksanakan task scenario (misal: transfer beda bank, cek mutasi), disusul dengan pengisian kuesioner SUS setelah tugas selesai. |
| Output | Metrik usability kuantitatif (waktu pengerjaan, jumlah error, skor SUS) dan data kualitatif (hasil wawancara keluhan pengguna). |
| Outcome | Teridentifikasinya celah usability (kelemahan UI) pada SeaBank dan terciptanya draf rekomendasi perbaikan desain antarmuka. |
| Constraints | Jumlah sampel partisipan uji yang mungkin terbatas dan lingkungan pengujian yang dikondisikan (tidak mencerminkan situasi pengguna saat sedang terburu-buru/panik di dunia nyata). |
| Stakeholders | Nasabah aplikasi SeaBank dan Tim pengembang (UI/UX Designer / Product Manager) SeaBank. |

**Komponen mana yang paling relevan dengan masalah riset?** Proses (eksekusi task scenario) dan Output (metrik yang dihasilkan).
---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas. Masalah langsung menunjuk pada keluhan spesifik pengguna SeaBank (kebingungan mencari riwayat transaksi & alur deposito) yang akan dievaluasi menggunakan metode Usability Testing dan kuesioner SUS. |
| Measurability | 4 | Sangat terukur. Variabel yang digunakan memiliki metrik kuantitatif yang jelas: persentase keberhasilan tugas (%), waktu penyelesaian (detik), rasio kesalahan, dan skor SUS (rentang 0-100). |
| Relevance | 5 | Sangat relevan. Sebagai bank digital murni tanpa kantor cabang (branchless), kelancaran antarmuka (UI/UX) SeaBank adalah kunci utama untuk mempertahankan kepercayaan dan kenyamanan nasabah. |
| Testability | 4 | Dapat diuji secara faktual dengan mensimulasikan task scenario kepada sampel partisipan (nasabah aktif SeaBank) dan membagikan kuesioner. Berpeluang mematahkan asumsi jika ternyata pengguna bisa menyelesaikannya dengan mudah. |
| Impact | 5 | Memberikan kontribusi praktis yang nyata. Hasilnya tidak sekadar angka, melainkan temuan akar masalah (pain points) yang dijadikan dasar rekomendasi perbaikan (redesign) antarmuka aplikasi. |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Kehadiran bank digital seperti SeaBank menuntut antarmuka pengguna (UI/UX) yang sangat intuitif, mengingat seluruh layanan transaksi dilakukan tanpa intervensi fisik dari kantor cabang. Namun, observasi awal terhadap ulasan pengguna menunjukkan adanya gejala kesulitan dalam bernavigasi, seperti kebingungan saat melacak riwayat transaksi lama dan ketidakpahaman terhadap alur fitur deposito. Kesulitan tersebut mengindikasikan adanya celah pada hirarki informasi yang membebani kognitif pengguna (cognitive load) dan berisiko menurunkan kepercayaan nasabah. Mengingat belum adanya pengukuran empiris terkait kendala tersebut, penelitian ini bertujuan untuk mengevaluasi tingkat kegunaan (usability) aplikasi SeaBank secara kuantitatif melalui metode Usability Testing (mengukur aspek efektivitas dan efisiensi) serta kuesioner System Usability Scale (mengukur tingkat kepuasan). Hasil evaluasi ini akan digunakan sebagai landasan saintifik untuk merumuskan rekomendasi perbaikan desain antarmuka aplikasi SeaBank agar lebih sesuai dengan mental model penggunanya.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan fundamentalnya terletak pada tujuan akhir dan batasannya (scope). "Masalah coding" (engineering) seperti bug, syntax error, atau fitur yang gagal dimuat, berorientasi murni pada solusi praktis (solve)—tujuannya adalah bagaimana membuat sistem kembali berfungsi secepat mungkin. Pendekatannya bersifat reaktif dan output-nya adalah sistem yang berjalan (working system).
> Sebaliknya, "masalah riset" berorientasi pada pemahaman dan pembuktian (understand & prove). Dalam konteks kasus SeaBank, aplikasinya mungkin secara teknis tidak memiliki bug dan berjalan lancar tanpa crash, tetapi pengguna tetap merasa kebingungan. Pendekatan riset tidak langsung bereaksi dengan "merombak kodingan UI", melainkan membuktikan fenomena tersebut secara empiris terlebih dahulu (misal mengukurnya dengan instrumen SUS). Output dari masalah riset bukanlah sekadar "aplikasi yang jalan", melainkan data valid, bukti terukur, dan temuan yang bisa dipertanggungjawabkan secara ilmiah sebelum diimplementasikan menjadi solusi.