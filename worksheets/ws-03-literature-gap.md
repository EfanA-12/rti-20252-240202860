# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Evaluasi Tingkat Usability Aplikasi Bank Digital SeaBank Menggunakan Pendekatan Usability Testing dan System Usability Scale (SUS)
Database   : Google Scholar, IEEE Xplore
Query      : ("usability testing" OR "System Usability Scale" OR "SUS") AND ("mobile banking" OR "digital bank" OR "SeaBank")
Tahun      : 2019 - 2024
Hasil awal : 58 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Dewi et al. | 2022 | Task Scenario & SUS | BCA Mobile (6 uji task, 20 SUS) | SUS: 76.38 (Good). Learnability rendah. | Fokus pada nasabah bank konvensional yang bertransisi ke mobile. |
| Kusumawardhana | 2019 | Usability Testing & SUS | BNI Mobile Banking | SUS: 72.5 (Acceptable). | Tidak mengukur time-based efficiency secara mendetail. |
| Santoso & Wijaya | 2023 | Kuesioner SUS | Bank Jago (Digital Bank) | SUS: 80.1 (Excellent). | Hanya kuesioner mandiri tanpa observasi Task Scenario. |
| Pratama et al. | 2021 | Heuristic Evaluation | Aplikasi Jenius | Ditemukan 15 masalah navigasi. | Berbasis evaluator ahli, tidak melibatkan pengguna akhir (nasabah). |
| Siregar | 2024 | SUS & Wawancara | Aplikasi SeaBank | SUS: 68 (Marginal). | Sampel sangat kecil dan tidak mengukur error rate kuantitatif. |

Pola yang ditemukan:
  Metode dominan     : Kuesioner System Usability Scale (SUS) menjadi standar pengukuran kepuasan.
  Dataset umum       : Aplikasi mobile banking dari bank konvensional (BCA, BNI).
  Limitasi berulang  : Jarang ada penelitian yang menggabungkan kuantitatif (SUS) dengan observasi langsung (Task Scenario) pada bank digital murni (branchless banking).

GAP IDENTIFICATION

Gap 1: Context Gap
  Deskripsi    : Sebagian besar literatur usability testing perbankan berfokus pada perbankan konvensional (BCA, BNI) yang memiliki kantor cabang fisik pendukung, bukan bank digital murni seperti SeaBank.
  Bukti        : Dari literature matrix, penelitian Dewi et al. (2022) dan Kusumawardhana (2019) berfokus pada bank tradisional.
  Signifikansi : Bank digital murni memiliki UI/UX sebagai satu-satunya titik sentuh (touchpoint) dengan nasabah, sehingga evaluasinya memiliki urgensi dan mental model yang berbeda.

Gap 2: Method Gap
  Deskripsi    : Penelitian bank digital (seperti Santoso & Wijaya pada Bank Jago) kebanyakan hanya mengandalkan penyebaran kuesioner SUS tanpa mengukur efficiency (goals/sec) dan error rate melalui simulasi task scenario langsung.
  Bukti        : Santoso & Wijaya (2023) hanya menggunakan kuesioner. Siregar (2024) tidak menghitung error rate.
  Signifikansi : Menggabungkan Task Scenario (performa objektif) dan SUS (kepuasan subjektif) akan menghasilkan rekomendasi desain antarmuka yang jauh lebih komprehensif dan akurat.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Evaluasi Usability BCA Mobile | Sama-sama mengevaluasi mobile banking dgn kombinasi Task Scenario + SUS | Ya, sangat representatif karena metodenya identik | Dewi et al., 2022 |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Evaluasi Usability Aplikasi Bank Digital SeaBank (Task Scenario & SUS)
**Query pencarian:** "usability testing" OR "System Usability Scale" OR "SUS" dan "mobile banking" OR "digital bank" OR "SeaBank"
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Dewi et al. | 2022 | Task Scenario & SUS | BCA Mobile (6 pengguna task, 20 kuesioner) | Skor SUS 76.38 (Acceptable). | Subjek adalah bank konvensional berskala raksasa, bukan bank digital murni. |
| 2 | Kusumawardhana | 2019 | Usability Testing & SUS | BNI Mobile Banking | Skor SUS 72.5 (Acceptable). | Tidak mengukur kecepatan (time-based efficiency) saat pengguna mengeksekusi tugas. |
| 3 | Santoso & Wijaya | 2023 | Kuesioner SUS kuantitatif | Bank Jago (Digital Bank) | Skor SUS 80.1 (Excellent). | Hanya menggunakan kuesioner evaluasi diri tanpa adanya pengujian skenario terukur. |
| 4 | Pratama et al. | 2021 | Heuristic Evaluation | Aplikasi Jenius (Bank BTPN) | Ditemukan 15 isu navigasi UI. | Evaluasi dilakukan oleh ahli/desainer UI, tidak mewakili cognitive load nasabah asli. |
| 5 | Siregar | 2024 | SUS & Wawancara bebas | Aplikasi SeaBank | Skor SUS 68 (Marginal). | Tidak menghitung error rate rasio kesalahan klik secara kuantitatif. |

**Pola yang terlihat — Metode dominan:** Penggunaan System Usability Scale (SUS) sebagai alat ukur kepuasan akhir (satisfaction).
**Limitasi yang berulang:** Mayoritas studi hanya menyebar kuesioner tanpa melakukan observasi task scenario untuk melihat langsung metrik penyelesaian tugas (kecepatan & jumlah error).
---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [ ] Ya / [X] Tidak | - |
| Method Gap | [X] Ya / [ ] Tidak | Penelitian bank digital murni jarang memadukan kuesioner SUS dengan observasi Task Scenario secara bersamaan untuk mengukur efficiency dan error rate. |
| Data Gap | [ ] Ya / [X] Tidak | - |
| Context Gap | [X] Ya / [ ] Tidak | Fokus evaluasi literatur saat ini didominasi oleh perbankan konvensional yang beralih ke mobile, bukan pada aplikasi branchless digital bank (seperti SeaBank) di mana UI adalah ujung tombak tunggal. |

**Gap utama yang dipilih:** Context Gap & Method Gap (Kombinasi).
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena mental model pengguna bank digital murni berbeda dengan bank konvensional. Jika bank konvensional error, nasabah bisa datang ke kantor cabang. Pada bank digital (SeaBank), jika UI membingungkan, transaksi gagal total. Oleh karena itu, sekadar menyebar kuesioner (seperti studi sebelumnya) tidak cukup; diperlukan metode kombinasi antara simulasi Task Scenario (untuk melihat kebingungan objektif) dan SUS (untuk persepsi subjektif) pada konteks branchless banking.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Evaluasi BCA Mobile (Task + SUS) | Domain sama (mobile banking), metode identik (Task Scenario + SUS). | Merupakan common practice evaluasi UI/UX aplikasi perbankan lokal yang solid. | Bukan SOTA algoritma, tapi metodologi evaluasi standar. | Dewi et al., 2022 |
| 2 | Evaluasi Bank Jago (SUS saja) | Domain paling mirip (Digital Bank). | Sering menjadi referensi utama mahasiswa dalam mengukur aplikasi keuangan. | Bukan SOTA | Santoso & Wijaya, 2023 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [X] Tidak
> Justifikasi: Baseline yang dipilih bukanlah metode yang sengaja dilemahkan. Baseline Dewi et al. (2022) justru adalah salah satu jurnal referensi yang kuat karena metodologinya lengkap. Menggunakan penelitian mereka sebagai landasan (baseline) akan memastikan pengujian SeaBank ini memenuhi standar evaluasi industri yang sama.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Klaim "belum ada yang meneliti ini" biasanya muncul dari asumsi pribadi atau rasa malas mencari paper (solution-first thinking). Seringkali, topiknya sebenarnya sudah banyak diteliti, hanya saja menggunakan istilah kunci yang berbeda.

Sebaliknya, sebuah research gap yang valid adalah posisi yang dibangun setelah membaca batas-batas pengetahuan saat ini. Cara membuktikannya adalah melalui metode Systematic Search (pencarian dengan Query Boolean) dan pemetaan Concept-centric (seperti Literature Matrix). Dengan memetakan apa yang sudah dilakukan oleh penelitian kita bisa membuktikan secara tertulis dan empiris letak "lubang" (gap) yang luput dari penelitian mereka, baik itu dari segi metode yang kurang lengkap, data yang bias, atau konteks sistem yang berbeda