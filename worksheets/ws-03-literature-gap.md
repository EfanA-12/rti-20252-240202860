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

Topik      : Analisis Sentimen dan Ekstraksi Topik Keluhan Usability pada Aplikasi SeaBank Menggunakan K-NN dan LDA.
Database   : Google Scholar, IEEE Xplore
Query      : ("sentiment analysis" OR "K-NN") AND ("topic modeling" OR "Latent Dirichlet Allocation" OR "LDA") AND ("mobile banking" OR "google play reviews")
Tahun      : 2020-2025
Hasil awal : 20 paper → Screening → 5 paper final
Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Setyabudi | 2024 | Sentiment Analysis (K-NN) | Ulasan Play Store | Akurasi klasifikasi sentimen | Hanya klasifikasi positif/negatif tanpa tahu konteks keluhan. |
| Jelni et al. | 2025 | Sentiment Analysis (K-NN) | Ulasan Play Store | Klasifikasi sentimen | Hanya sebatas sentimen, tidak ada ekstraksi fitur bermasalah. |
| Rahman et al. | 2022 | Topic Modeling (LDA) | Ulasan E-commerce | Klaster topik pengguna | Memasukkan ulasan pujian yang membuat topik keluhan menjadi bias. |
| Wati & Budi | 2023 | LDA + SVM | Ulasan Twitter | Ekstraksi topik opini | Tidak diterapkan pada domain aplikasi perbankan murni (branchless banking). |
| Pratama | 2021 | K-NN + Naive Bayes | Ulasan FinTech | Perbandingan algoritma | Fokus komparasi akurasi, bukan pemetaan masalah (friction points). |

Pola yang ditemukan:
  Metode dominan     : K-NN sering digunakan untuk sentimen karena stabil pada data teks pendek, dan LDA populer untuk mengekstrak topik tanpa label.
  Dataset umum       : Ulasan dari Play Store atau Twitter.
  Limitasi berulang  : Riset sentimen K-NN jarang dilanjutkan ke tahap ekstraksi topik (berhenti di label positif/negatif saja). Sebaliknya, riset LDA sering memasukkan semua data sehingga topik keluhan bercampur dengan topik pujian.

GAP IDENTIFICATION

Gap 1: [Jenis: Method Gap]
  Deskripsi    : Belum ada integrasi pipeline yang menggunakan K-NN untuk menyaring ulasan negatif secara spesifik, yang kemudian diproses oleh LDA untuk mengekstrak topik keluhan usability.
  Bukti        : Paper terdahulu (Setyabudi, Jelni) hanya berhenti pada klasifikasi sentimen.
  Signifikansi : Pipeline gabungan ini dapat memfilter noise ulasan positif, sehingga LDA menghasilkan topik keluhan yang jauh lebih koheren dan relevan bagi pengembang.
Gap 2: [Jenis: Context Gap]
  Deskripsi    : Belum ada pemodelan topik keluhan usability secara otomatis pada aplikasi perbankan digital murni (branchless banking) seperti SeaBank.
  Bukti        : Studi LDA sebelumnya lebih banyak di domain E-Commerce atau FinTech P2P Lending.
  Signifikansi : SeaBank memiliki struktur fitur yang berbeda, sehingga leksikon (kosakata) dan topik keluhannya unik dan butuh pemetaan spesifik.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| K-NN Sentiment | Pemilah sentimen ulasan | Common practice | Setyabudi, 2024 |
| LDA Topic Modeling | Pengekstrak topik keluhan | State-of-the-Art (Unsupervised) | Rahman et al., 2022 |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Analisis Sentimen dan Ekstraksi Topik Keluhan Usability pada Aplikasi SeaBank Menggunakan Algoritma K-NN dan Latent Dirichlet Allocation (LDA).
**Query pencarian:** ("sentiment analysis" OR "K-NN") AND ("topic modeling" OR "Latent Dirichlet Allocation" OR "LDA") AND ("mobile banking" OR "google play reviews").
**Database:** Google Scholar
| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Setyabudi | 2024 | Sentiment Analysis (K-NN) | Ulasan Play Store | Akurasi klasifikasi sentimen | Berhenti pada sentimen, tidak membedah konteks keluhan. |
| 2 | Jelni et al. | 2025 | Sentiment Analysis (K-NN) | Ulasan Play Store | Klasifikasi sentimen | Tidak mengekstrak kata kunci fitur yang bermasalah. |
| 3 | Rahman et al. | 2022 | SUS + Usability Testing | 30 responden (BSI) | Skor SUS (Good) | Tanpa data sentimen |
| 4 | Wati & Budi   | 2023 | LDA + SVM | Ulasan Twitter | Opini layanan pelanggan | Tidak diuji pada aplikasi perbankan (branchless banking). |
| 5 | Pratama   | 2021 | K-NN + Naive Bayes | Ulasan FinTech  | Komparasi akurasi | Tidak ada aspek pemetaan masalah usability (HCI). |

**Pola yang terlihat — Metode dominan:** Algoritma K-NN banyak diandalkan sebagai baseline klasifikasi teks ulasan karena kinerjanya yang baik pada dimensi kata, sedangkan LDA menjadi metode unsupervised paling dominan untuk memetakan ulasan teks bebas menjadi klaster topik.
**Limitasi yang berulang:** Studi analisis sentimen jarang dilanjutkan untuk mencari tahu "apa yang sebenarnya dikeluhkan" oleh sentimen negatif tersebut. Di sisi lain, studi ekstraksi topik sering mengalami distorsi (topik tidak jelas) karena mencampur ulasan positif dan negatif ke dalam satu model latih.  

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [ ] Ya / [X] Tidak | - |
| Method Gap | [X] Ya / [ ] Tidak | Belum ada studi yang merangkai pipeline di mana K-NN digunakan sebagai filter (penyaring ulasan bernada negatif) sebelum data tersebut diekstrak menjadi topik keluhan antarmuka secara spesifik menggunakan LDA. |
| Data Gap | [ ] Ya / [X] Tidak | - |
| Context Gap | [X] Ya / [ ] Tidak | Mayoritas studi LDA berfokus pada E-Commerce atau Twitter, sehingga belum ada ekstraksi topik spesifik mengenai keluhan usability pada aplikasi branchless banking seperti SeaBank di Indonesia. |

**Gap utama yang dipilih:** Method Gap (Integrasi K-NN dan LDA).
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Menjalankan LDA pada seluruh kumpulan ulasan Play Store (yang bercampur antara pujian, cacian, dan spam) sering kali menghasilkan topik yang bias dan tidak dapat dipahami (incoherent). Dengan mengimplementasikan K-NN terlebih dahulu untuk mengisolasi ulasan bersentimen negatif, model LDA hanya akan memproses murni keluhan pengguna. Hal ini akan meningkatkan Coherence Score secara signifikan dan menghasilkan topik masalah (misalnya: gagal login, tombol transfer tersembunyi) yang langsung dapat ditindaklanjuti oleh developer SeaBank.
---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | K-Nearest Neighbor (K-NN) | Model dasar klasifikasi sentimen berbasis teks. | Lazim digunakan untuk analisis sentimen ulasan Google Play Store berbahasa Indonesia. | Tidak (Baseline) | Setyabudi, 2024 |
| 2 | Latent Dirichlet Allocation (LDA) | Digunakan untuk mengelompokkan keluhan usability ke dalam kategori spesifik secara otomatis. | Merupakan standar emas (gold standard) dalam algoritma Topic Modeling (Unsupervised Learning). | Ya | Rahman et al., 2022 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [X] Tidak
> Justifikasi: K-NN dan LDA adalah algoritma yang sangat representatif dan standar (common practice) di ranah Natural Language Processing (NLP). Keduanya dipilih bukan karena lemah (straw man), melainkan karena keduanya sangat cocok untuk karakteristik data teks pendek dari Play Store. Tujuan riset ini bukan untuk mengalahkan algoritma Transformer yang berat, tetapi membangun pipeline otomatisasi analisis keluhan yang efisien dan interpretable bagi pihak developer.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Dulu saya menganggap kalimat "belum ada yang meneliti ini" sudah cukup untuk dijadikan celah riset. Kini saya sadar bahwa itu hanyalah klaim lemah tanpa bukti. Research gap yang valid harus dibuktikan secara empiris melalui pemetaan literatur sistematis (concept-centric). Misalnya, dalam kasus aplikasi SeaBank ini, saya tidak sekadar berasumsi "belum ada yang mengekstrak topik keluhan", tetapi saya bisa membuktikan melalui tabel pemetaan literatur bahwa riset terdahulu memang selalu berhenti pada klasifikasi sentimen K-NN (label positif/negatif) dan tidak pernah dilanjutkan untuk membedah konteks spesifik keluhannya menggunakan LDA. Pemetaan yang terstruktur inilah yang membuat kebaruan (novelty) riset saya teruji dan valid secara ilmiah.
