# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
3. **Snowballing**: backward (telusuri referensi) + forward (cari yang mengutip)
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

Topik      : Evaluasi Usability dan Kualitas Antarmuka Aplikasi Keuangan / Mobile Banking
Database   : Google Scholar, J-PTIIK
Query      : ("mobile banking" OR "aplikasi keuangan") AND ("usability" OR "user experience" OR "ISO 25010" OR "heuristic")
Tahun      : 2022 - 2024
Hasil awal : 42 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Dewi, dkk. | 2022 |  Usability Testing & Kuesioner SUS | 6 partisipan task, 20 responden SUS | Skor SUS 76.38 (Acceptable). | Tidak membandingkan dengan aplikasi bank lain; tidak ada uji desain ulang. |
| Nurqamarani, dkk. | 2023 |  Kuesioner Standar ISO/IEC 25010 | Pengguna aplikasi keuangan UMKM | Aspek Functional Suitability mencapai 82,00% (Sangat Baik). | Rentan bias populasi dan skor rata-rata menutupi error spesifik di antarmuka. |
| Santoso & Sari | 2023 | User Experience Questionnaire (UEQ) | 100 nasabah pengguna m-banking | Skala "Daya Tarik" dan "Stimulasi" aplikasi dinilai di bawah rata-rata. | Hanya mengukur metrik emosional/persepsi, tidak menunjukkan di mana letak persis masalah desainnya. |
| Wijaya, dkk. | 2022 | Heuristic Evaluation (Nielsen's 10 Heuristics) | 3 orang ahli (Expert Evaluator) | Ditemukan 15 masalah usability utama pada navigasi aplikasi. | Kurang merepresentasikan sentimen dan pengalaman nyata dari pengguna akhir (end-user). |
| Pratama, dkk. | 2024 | Observasi Task Completion (Time & Error) | 15 pengguna awam | Kegagalan tertinggi terjadi pada menu pencarian riwayat transaksi. | Biaya dan waktu riset lebih tinggi, serta sampel partisipan sangat terbatas. |

Pola yang ditemukan:
  Metode dominan     : Terbagi dua kubu utama; evaluasi berbasis kuesioner pengguna (SUS, UEQ, ISO 25010) dan evaluasi berbasis inspeksi pakar/observasi (Heuristic, Task Completion).
  Dataset umum       : Kuesioner menggunakan sampel besar (20-100+ responden), sementara observasi/pakar menggunakan sampel kecil (3-15 orang).
  Limitasi berulang  : Metode kuesioner sangat baik untuk menilai skor kepuasan akhir, namun gagal mendeteksi koordinat pasti (pain points) dari error UI. Sebaliknya, evaluasi ahli tahu letak error secara presisi, namun tidak mencerminkan kepuasan pengguna nyata.

GAP IDENTIFICATION

Gap 1: [Jenis: performance / method / data / context]
  Deskripsi    : Belum ada integrasi yang kuat antara pengujian berbasis sentimen pengguna dengan inspeksi pakar antarmuka.
  Bukti        : Jurnal yang menggunakan SUS/UEQ/ISO rata-rata tidak mampu menunjukkan letak error desain secara spesifik, sedangkan jurnal Heuristic tidak memiliki data kepuasan nasabah.
  Signifikansi : Diperlukan pendekatan metode campuran (mixed-methods) yang menggabungkan instrumen kepuasan pengguna (seperti SUS) dengan metrik pengujian fungsional (Task Scenario) secara simultan untuk mendiagnosis masalah secara akurat.

Gap 2: [Jenis: Context Gap]
  Deskripsi    : Sebagian besar riset hanya terfokus pada evaluasi aplikasi satu arah tanpa adanya komparasi.
  Bukti        : Dari 5 literatur di atas, seluruhnya menguji aplikasi keuangan secara mandiri tanpa membandingkan metriknya dengan standar industri atau kompetitor (straw man comparison).
  Signifikansi : Evaluasi tanpa baseline kompetitor membuat hasil skor (seperti SUS 76) sulit dinilai apakah memang benar-benar kompetitif di pasar aplikasi perbankan digital saat ini.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Kuesioner System Usability Scale (SUS) | Standar pengukuran kepuasan pengguna (satisfaction). | Sangat representatif dan stabil digunakan untuk mengevaluasi aplikasi keuangan. | Dewi et al., 2022 |
| Heuristic Evaluation | Mampu mendeteksi pelanggaran desain antarmuka secara presisi. | Praktik umum (common practice) bagi desainer UI/UX. | Wijaya, dkk., 2022 |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan Google Scholar atau database lain.

**Topik riset:** Evaluasi Usability dan Kualitas Antarmuka Aplikasi Keuangan / Mobile Banking
**Query pencarian:** ("mobile banking" OR "aplikasi keuangan") AND ("usability" OR "user experience" OR "ISO 25010" OR "heuristic")
**Database:** Google Scholar, J-PTIIK

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Dewi, dkk. | 2022 | Usability Testing & Kuesioner SUS | 6 partisipan task, 20 responden SUS | Skor SUS 76.38 (Acceptable). | Tidak membandingkan dengan aplikasi bank lain; tidak ada uji desain ulang. |
| 2 | Nurqamarani, dkk. | 2023 | Kuesioner Standar ISO/IEC 25010 | Pengguna aplikasi keuangan UMKM | Aspek Functional Suitability 82,00% (Sangat Baik). | Rentan bias populasi dan skor rata-rata menutupi titik error spesifik di antarmuka. |
| 3 | Santoso & Sari | 2023 | User Experience Questionnaire (UEQ) | 100 nasabah pengguna m-banking | Skala "Daya Tarik" dan "Stimulasi" dinilai di bawah rata-rata. | Hanya mengukur metrik emosional/persepsi, tidak menunjukkan di mana letak persis masalah UI-nya.4Wijaya, dkk.2022Heuristic Evaluation (Nielsen)3 orang ahli (Expert Evaluator)Ditemukan 15 masalah usability utama pada navigasi aplikasi.Kurang merepresentasikan sentimen dan pengalaman nyata dari pengguna akhir (end-user).5Pratama, dkk.2024Observasi Task Completion15 pengguna awamKegagalan tertinggi terjadi pada menu pencarian riwayat transaksi.Biaya dan waktu riset lebih tinggi, serta sampel partisipan sangat terbatas. |
| 4 | Wijaya, dkk. | 2022 | Heuristic Evaluation (Nielsen) | 3 orang ahli (Expert Evaluator) | Ditemukan 15 masalah usability utama pada navigasi aplikasi. | Kurang merepresentasikan sentimen dan pengalaman nyata dari pengguna akhir (end-user). |
| 5 | Pratama, dkk. | 2024 | Observasi Task Completion |15 pengguna awam | Kegagalan tertinggi terjadi pada menu pencarian riwayat transaksi. | Biaya dan waktu riset lebih tinggi, serta sampel partisipan sangat terbatas. |

**Pola yang terlihat — Metode dominan:** Ada dua kubu utama, yaitu evaluasi berbasis kuesioner pengguna (SUS, UEQ, ISO 25010) dan evaluasi berbasis inspeksi pakar/observasi (Heuristic, Task Completion).
**Limitasi yang berulang:** Metode kuesioner sangat baik untuk menilai skor kepuasan akhir namun gagal mendeteksi koordinat pasti (pain points) dari error desain antarmuka. Sebaliknya, metode observasi ahli mampu menemukan presisi error, namun kurang mencerminkan sentimen kepuasan populasi pengguna secara luas.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [X] Ya / [ ] Tidak | Tingkat kemudahan dipelajari (learnability) pada eksekusi tugas oleh pengguna baru masih sangat rendah. |
| Method Gap | [X] Ya / [ ] Tidak | Belum ada integrasi yang kuat antara instrumen pelacak kepuasan (satisfaction) dengan instrumen pelacak error antarmuka (inspeksi visual). |
| Data Gap | [ ] Ya / [X] Tidak | |
| Context Gap | [X] Ya / [ ] Tidak | Riset didominasi evaluasi aplikasi secara mandiri (terisolasi) tanpa ada perbandingan metrik dengan kompetitor sejenis. |

**Gap utama yang dipilih:** Method Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena hanya dengan mengetahui bahwa pengguna "tidak puas" (dari skor kuesioner) tidak akan cukup untuk memberikan rekomendasi perbaikan aplikasi bagi pihak developer. Diperlukan pendekatan mixed-methods yang menggabungkan instrumen sentimen pengguna (seperti SUS/UEQ) dengan metrik pengujian fungsional dan inspeksi antarmuka secara simultan agar akar masalah UX bisa didiagnosis secara akurat dan tepat sasaran.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Kuesioner SUS | Mengukur kepuasan pengguna akhir secara kuantitatif. | Menjadi standar instrumen global yang tervalidasi di industri. | Bukan metode terbaru, tapi common practice terbaik. | Dewi et al., 2022 |
| 2 | Heuristic Evaluation | Mampu mendeteksi secara spesifik pelanggaran desain antarmuka. | Metode evaluasi standar oleh para desainer UI/UX profesional. | Bukan, tapi merupakan standar emas (gold standard) inspeksi pakar. | Wijaya et al., 2022 |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [X] Tidak
> Justifikasi: Penggunaan kuesioner SUS dan Evaluasi Heuristik dipilih karena keduanya merupakan instrumen validasi yang memiliki dasar teoretis kuat. Di lingkungan akademis dan industri TI, kedua metode ini telah lama diakui sebagai standar baku untuk mengevaluasi kelayakan perangkat lunak secara mendalam.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Identifikasi celah penelitian (research gap) menuntut verifikasi sistematis terhadap diskursus yang sudah ada. Alih-alih berasumsi pada kebaruan ide, validitas sebuah riset dibuktikan dengan menyajikan sintesis literatur yang terstruktur. Penggunaan matriks konsep memungkinkan peneliti mengidentifikasi pola yang berulang dan kelemahan metodologis dari sekumpulan studi sebelumnya, yang kemudian menjadi landasan kuat bagi urgensi penelitian yang diusulkan.