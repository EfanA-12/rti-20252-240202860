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
  Konteks  : Evaluasi kegunaan (usability) aplikasi mobile banking (BCA mobile) pada nasabah di Kota Singaraja

System Context
  Input       : Interaksi pengguna (partisipan) saat mengeksekusi skenario tugas (task scenario) seperti mengecek saldo, transfer antar bank, cek mutasi, dan top-up e-wallet.
  Process     : Navigasi pengguna di dalam antarmuka aplikasi BCA mobile untuk menemukan fitur dan memproses instruksi transaksi.
  Output      : Metrik pengujian berupa success rate (persentase keberhasilan), time-based efficiency (kecepatan), error rate (jumlah kesalahan), dan skor kuesioner
  Outcome     :Penemuan usability problems spesifik dan pembuatan rekomendasi perbaikan antarmuka UI/UX (seperti penyatuan menu transfer dan pemindahan info saldo).
  Constraints : Adanya perbedaan kebiasaan/pemahaman antara nasabah yang sudah terbiasa dengan BCA mobile (Kelompok 2) dengan pengguna aplikasi bank lain (Kelompok 1).
  Stakeholders: Nasabah (pengguna akhir) dan pihak pengembang/manajemen PT Bank Central Asia Tbk.

Fenomena → Problem
  Fenomena yang diamati             : Meskipun BCA mobile menempati peringkat 1 sebagai aplikasi keuangan terpopuler di Indonesia, ratingnya di Appstore hanya mencapai 3,4 dari 5.
  Gejala (symptom) yang terukur     : Keluhan nasabah terkait sulitnya melihat riwayat transaksi, kebingungan fitur transfer antar bank yang mengharuskan mendaftar nomor rekening terlebih dahulu, dan tampilan yang dianggap kurang up-to-date.
  Masalah yang didiagnosis          : Antarmuka dan alur navigasi fitur utama tidak efisien serta membingungkan, yang berdampak pada beban kognitif pengguna.
  Masalah riset (researchable)      : Diperlukan evaluasi komprehensif untuk mengukur secara empiris tingkat efektivitas, efisiensi, dan kepuasan pengguna aplikasi BCA mobile melalui Usability Testing dan System Usability Scale (SUS).
  Variabel yang terukur             : Learnability (success rate), Efficiency (time-based efficiency dalam goals/sec), Error rate, dan Satisfaction (skor SUS berskala 0-100).
Problem Quality Check
  [X] Clarity — Apakah satu orang membaca akan paham? Pembaca dapat langsung memahami bahwa masalah utamanya adalah pengguna aplikasi BCA Mobile merasa kesulitan pada fitur tertentu (seperti mencari riwayat transaksi dan proses transfer yang panjang), sehingga sistem tersebut perlu dievaluasi tingkat usability-nya.
  [X] Measurability — Apakah ada metrik kuantitatif? Penelitian ini menggunakan metrik berupa angka yang pasti, yaitu persentase Success Rate (untuk learnability), goals/sec (untuk efficiency), jumlah error/defect (untuk error rate), dan skor 0-100 (untuk kuesioner SUS).
  [X] Relevance — Apakah penting untuk domain? Sangat penting. Di era digital saat ini, nilai transaksi elektronik terus meningkat drastis (naik 30,7% di awal 2021). Perbankan wajib memiliki aplikasi dengan UX yang baik agar tetap bisa bersaing dan mempertahankan nasabahnya.
  [X] Testability — Apakah bisa gagal? Ya, dapat diuji dan berpeluang mematahkan asumsi awal. Bisa saja saat diuji dengan task scenario, para partisipan ternyata bisa menyelesaikan tugas dengan sangat cepat (0 error) dan skor SUS menunjukkan angka sempurna, yang berarti keluhan awal di App Store mungkin hanya dari segelintir pengguna saja. Namun, pengujian membuktikan sebaliknya, di mana learnability terbukti di bawah rata-rata.
  [X] Impact — Apakah ada kontribusi jika terjawab? Ada kontribusi nyata. Hasil evaluasi tidak hanya berupa deretan angka kepuasan, tetapi diterjemahkan menjadi rekomendasi desain User Interface (UI) yang konkret, seperti menyatukan menu transfer dan memindahkan info saldo ke beranda, yang bisa langsung diterapkan oleh pihak developer bank.

Problem Statement (1 paragraf):
  PT Bank Central Asia Tbk telah meluncurkan BCA mobile untuk menjawab tuntutan digitalisasi perbankan, menjadikannya aplikasi keuangan terpopuler di Indonesia dengan volume transaksi yang terus meningkat. Namun, di balik kepopuleran tersebut, berbagai ulasan dan wawancara awal menunjukkan keluhan nasabah terkait tingkat interaksi aplikasi; seperti sulitnya melacak riwayat transaksi, panjangnya proses transfer antar bank karena kewajiban registrasi rekening, hingga tata letak antarmuka yang kurang modern. Kesulitan-kesulitan tersebut merupakan indikasi adanya isu usability yang berpotensi menurunkan kenyamanan dan efisiensi pengguna. Mengingat belum adanya pengukuran empiris terhadap masalah tersebut, penelitian ini bertujuan untuk mengevaluasi tingkat usability BCA mobile dengan menerapkan uji task scenario (untuk mengukur aspek learnability, efficiency, dan error) serta kuesioner System Usability Scale (untuk mengukur kepuasan/satisfaction). Hasil pengukuran ini difungsikan untuk mendiagnosis letak spesifik kesulitan pengguna guna memberikan landasan perumusan rekomendasi perbaikan antarmuka aplikasi.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Evaluasi Usability Aplikasi Mobile Banking

| Tahap | Hasil |
|-------|-------|
| Reality | Perbankan menggencarkan teknologi seluler (BCA mobile) agar nasabah dapat bertransaksi dengan nyaman, cepat, dan mudah.  |
| Observed Issue (Symptom) | Pengguna sering kebingungan di dalam aplikasi, seperti mengeluhkan langkah panjang saat transfer antar bank dan fitur mutasi yang letaknya tidak intuitif. |
| Diagnosed Problem (Root Cause) | Terdapat kelemahan pada tata letak arsitektur informasi dan alur UI/UX fitur-fitur transaksi utama aplikasi saat ini. |
| Researchable Problem | Perlunya evaluasi tingkat learnability, efficiency, error, dan satisfaction pada aplikasi BCA mobile menggunakan instrumen standar usability. |
| Measurable Variable | Perhitungan success rate (%), rata-rata kecepatan eksekusi tugas (goals/sec), jumlah defect/error, dan skor SUS (System Usability Scale). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Interaksi motorik pengguna (ketukan layar, navigasi menu) dan input data (nomor rekening, nominal transaksi) ke dalam antarmuka aplikasi BCA mobile. |
| Process | Alur navigasi sistem (user flow), pencarian informasi (seperti mutasi atau saldo), serta proses transisi antarmuka dari satu halaman ke halaman lainnya. |
| Output | Keberhasilan atau penyelesaian tugas transaksi (task scenario), yang diukur melalui persentase keberhasilan, kecepatan waktu pengerjaan, dan jumlah kesalahan ketik/navigasi. |
| Outcome | Pengalaman pengguna yang nyaman, kepuasan bertransaksi (tercermin dari skor System Usability Scale), dan kemudahan nasabah dalam beradaptasi dengan layanan perbankan digital. |
| Constraints | Tingkat pemahaman dan kebiasaan yang berbeda antara pengguna baru dengan pengguna aktif, serta tata letak menu saat ini yang mengharuskan langkah terlalu panjang (seperti wajib mendaftar rekening tujuan sebelum transfer). |
| Stakeholders | Nasabah pengguna aplikasi (sebagai partisipan/pengguna akhir) dan pihak PT Bank Central Asia Tbk (sebagai penyedia layanan). |

**Komponen mana yang paling relevan dengan masalah riset?** Process (Alur desain UI/UX) dan Outcome (Kepuasan/Kemudahan Pengguna).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Sangat jelas. Masalah langsung menunjuk pada keluhan spesifik (sulit cek saldo, transfer rumit) yang akan dievaluasi menggunakan metode Usability Testing dan instrumen kuesioner SUS. |
| Measurability | 4 | Sangat terukur. Menggunakan metrik kuantitatif: success rate (%), efficiency (goals/sec), angka error, dan skor SUS (rentang 0-100). |
| Relevance | 5 | Sangat relevan karena transaksi e-money melonjak 30,7%, sehingga bank harus memastikan aplikasinya dapat bersaing dan memenuhi ekspektasi kenyamanan nasabah di era digital. |
| Testability | 3 | Peneliti secara faktual mampu mengujinya langsung kepada partisipan (menggunakan 6 responden untuk simulasi task scenario dan 20 responden untuk SUS). |
| Impact | 5 | Memberikan kontribusi nyata berupa temuan 4 pain points (masalah desain) dan solusi perbaikan antarmuka yang konkret (seperti usulan penambahan menu e-wallet khusus). |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Transformasi digital mendorong peningkatan volume transaksi melalui aplikasi BCA mobile. Namun, evaluasi awal menunjukkan bahwa pengguna kerap mengalami kebingungan terkait desain antarmuka sistem, seperti letak fitur mutasi yang tidak intuitif dan alur transfer antarbank yang memakan waktu terlalu lama. Saat ini, belum ada evaluasi yang mengukur tingkat interaksi dan beban kognitif pengguna tersebut secara empiris. Oleh karena itu, riset ini perlu dilakukan untuk mengevaluasi parameter kegunaan aplikasi secara kuantitatif melalui metode Usability Testing (mengukur learnability, efficiency, error) serta kuesioner System Usability Scale (mengukur kepuasan). Hasil evaluasi akan digunakan sebagai dasar saintifik dalam merumuskan rekomendasi redesign antarmuka aplikasi BCA mobile agar lebih berpusat pada pengguna (user-centric).

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Perbedaan mendasar keduanya ada pada tujuan akhir. Masalah engineering (koding) bertujuan memperbaiki sistem yang error, misalnya mencari bug saat aplikasi crash. Sebaliknya, masalah riset bertujuan memahami interaksi pengguna. Dalam riset UX, aplikasi mungkin berjalan lancar tanpa error teknis, tetapi pengguna tetap merasa kesulitan. Riset menggunakan metode ilmiah (seperti SUS) untuk mencari tahu akar masalah dari sisi perilaku manusia, sehingga keputusan redesign antarmuka nantinya didasari oleh data yang objektif, bukan sekadar asumsi visual.
