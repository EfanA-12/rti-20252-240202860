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

Topik      : Analisis Validasi Usability Aplikasi SeaBank (Task Scenario vs Sentimen Publik)
Database   : Google Scholar, ResearchGate, J-PTIIK
Query      : ("usability testing" OR "System Usability Scale") AND ("mobile banking" OR "digital banking") AND ("sentiment analysis" OR "google play store")
Tahun      : 2019-2025
Hasil awal : 15 paper → Screening → 5 paper final
Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Dewi et al. | 2022 | SUS + Task Scenario | 20 responden | Skor SUS (Good) | Sampling bias lokal |
| Kusumawardhana | 2019 | SUS + Usability Testing | 30 responden | Skor SUS (Good) | Subjektivitas tinggi |
| Santoso et al. | 2022 | SUS + Usability Testing | 30 responden | Skor SUS (Good) | Tanpa data sentimen |
| Setyabudi | 2024 | Sentiment Analysis (KNN) | Ulasan Play Store | Akurasi klasifikasi | Tanpa validasi objektif |
| Jelni et al. | 2025 | Sentiment Analysis (KNN) | Ulasan Play Store | Klasifikasi sentimen | Tanpa validasi objektif |

Pola yang ditemukan:
  Metode dominan     : Kombinasi SUS untuk evaluasi objektif dan KNN untuk analisis sentimen.
  Dataset umum       : Data primer skala kecil (SUS) dan data sekunder ulasan Play Store.
  Limitasi berulang  : Belum adanya triangulasi antara metode pengujian objektif dan analisis sentimen publik.

GAP IDENTIFICATION

Gap 1: [Jenis: performance / method / data / context]
  Deskripsi    : Belum ada triangulasi metode antara performa objektif (Task Scenario) dan sentimen subjektif (ulasan publik).
  Bukti        : Paper terdahulu hanya menggunakan salah satu pendekatan, bukan gabungan keduanya.
  Signifikansi : Mengurangi bias dari data subjektif dan meningkatkan akurasi validasi usability.
Gap 2: [Jenis: Context Gap]
  Deskripsi    : Belum ada evaluasi komprehensif pada aplikasi perbankan digital murni (branchless banking) seperti SeaBank.
  Bukti        : Studi sebelumnya mayoritas berfokus pada aplikasi bank konvensional (BCA, BNI, BSI).
  Signifikansi : Memberikan data empiris untuk perbankan digital yang memiliki perilaku nasabah berbeda.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| SUS Scoring | Standar evaluasi usability | Common practice | Dewi et al., 2022 |
| KNN Sentiment | Analisis ulasan publik | Umum digunakan | Setyabudi, 2024 |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Analisis Validasi Usability Aplikasi SeaBank: Studi Komparatif Antara Eksperimen Task Scenario dan Sentimen Publik Google Play Store.
**Query pencarian:** ("usability testing" OR "System Usability Scale") AND ("mobile banking" OR "digital banking") AND ("sentiment analysis" OR "google play store").
**Database:** Google Scholar
| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Dewi et al. | 2022 | SUS + Task Scenario | 20 responden (BCA) | Skor SUS (Good) | Sampling bias lokal |
| 2 | Kusumawardhana et al. | 2019 | SUS + Usability Testing | 30 responden (BNI) | Skor SUS (Good) | Subjektivitas tinggi |
| 3 | Santoso et al. | 2022 | SUS + Usability Testing | 30 responden (BSI) | Skor SUS (Good) | Tanpa data sentimen |
| 4 | Setyabudi   | 2024 | Sentiment Analysis (KNN) | Ulasan Play Store | Akurasi sentiment | Hanya sentimen publik |
| 5 | Jelni et al.   | 2025 | Sentiment Analysis (KNN) | Ulasan Play Store   | Klasifikasi sentimen | Tanpa validasi objektif |

**Pola yang terlihat — Metode dominan:** Penggunaan System Usability Scale (SUS) sebagai standar evaluasi objektif dan K-Nearest Neighbor (KNN) sebagai metode analisis sentimen pada data sekunder.
**Limitasi yang berulang:** Mayoritas studi hanya terfokus pada salah satu pendekatan (objektif atau subjektif) secara terpisah, sehingga tidak terdapat triangulasi untuk memvalidasi usability secara utuh.  

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [ ] Ya / [X] Tidak | - |
| Method Gap | [X] Ya / [ ] Tidak | Belum ada studi yang melakukan triangulasi antara pengujian usability objektif (Task Scenario) dengan analisis sentimen publik secara komprehensif pada aplikasi perbankan digital. |
| Data Gap | [ ] Ya / [X] Tidak | - |
| Context Gap | [X] Ya / [ ] Tidak | Mayoritas studi terdahulu berfokus pada aplikasi bank konvensional (BCA, BNI, BSI), sehingga belum ada evaluasi mendalam pada ekosistem branchless banking (SeaBank) di Indonesia. |

**Gap utama yang dipilih:** Methodological Triangulation Gap (penggabungan metode objektif dan subjektif).
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Gap ini penting karena pengujian usability yang hanya mengandalkan data subjektif (kuesioner/ulasan) rentan terhadap bias persepsi, sedangkan pengujian yang hanya mengandalkan task scenario terbatas pada skenario yang ditentukan peneliti. Dengan menggabungkan kedua metode tersebut, riset ini dapat memberikan validasi yang lebih kuat, akurat, dan representatif terhadap perilaku nasabah di perbankan digital, yang pada akhirnya menghasilkan rekomendasi desain antarmuka yang benar-benar berbasis bukti (data-driven).
---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | System Usability Scale (SUS) | Mengukur tingkat kepuasan pengguna secara kuantitatif dalam riset usability. | Merupakan instrumen standar yang digunakan secara global dalam banyak studi mobile banking. | Ya (Benchmark) | Dewi et al., 2022 |
| 2 | K-Nearest Neighbor (KNN) | Digunakan untuk mengklasifikasikan sentimen ulasan publik secara otomatis. | Metode yang lazim digunakan untuk klasifikasi teks pada data ulasan Google Play Store. | Tidak | Setyabudi, 2024 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [ ] Tidak
> Justifikasi: Pemilihan baseline ini bukan merupakan straw man karena menggunakan instrumen yang diakui secara luas dalam literatur ilmiah. System Usability Scale (SUS) adalah standar emas (gold standard) dalam evaluasi usability objektif, sementara algoritma KNN dipilih karena efektivitasnya yang terbukti dalam klasifikasi sentimen pada riset sejenis. Penggunaan baseline ini bertujuan untuk memastikan validitas hasil riset, bukan untuk melemahkan perbandingan agar metode saya terlihat lebih unggul secara artifisial.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Dulu saya menganggap literature review sekadar merangkum paper dan "belum ada yang meneliti" sebagai celah riset. Kini saya sadar bahwa riset yang valid harus berbasis concept-centric dan research gap harus dibuktikan melalui pemetaan literatur sistematis agar novelty riset teruji secara ilmiah.
