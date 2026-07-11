# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang koheren (Cv > 0.4) menggunakan model LDA pada ulasan aplikasi SeaBank?
Metrik Utama      : Coherence Score (Cv) dan Waktu Eksekusi (Execution Time)

Tabel Hasil:
| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
|     Baseline (LDA Tanpa Filter)     |          0.32 ± 0.04            |           12.4 ± 1.5 detik           | 10  |
|     Treatment (LDA + Filter K-NN)   |          0.45 ± 0.03            |           15.8 ± 1.8 detik           |  10 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Bar chart (dengan error bar) | Penggunaan filter K-NN terbukti mendongkrak skor koherensi topik secara signifikan. | Mean Coherence Score ± std |
| 2 | Box plot | Variabilitas skor koherensi pada skenario Treatment lebih stabil antar-run. | Seluruh nilai Coherence Score |

Bias Check:
  [X] Y-axis mulai dari 0 (atau dijustifikasi)
  [X] Error bar/CI ditampilkan
  [X] Semua data disertakan (tidak cherry-picked)
  [X] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
| Baseline (LDA Tanpa Filter) | $0.32 ± 0.04$ | $12.4 ± 1.5$ detik | 10 |
| Treatment (LDA + Filter K-NN) | $0.45 ± 0.03$ | $15.8 ± 1.8$ detik | 10 |


**Checklist tabel:**
- [X] Self-contained (judul jelas, satuan ada, N tercantum)
- [X] Mean ± std (bukan single number)
- [X] Diurutkan berdasarkan metrik utama
- [X] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar chart + error bar | Membandingkan rata-rata koherensi topik antara metode Baseline dan Treatment. | Mean Coherence Score ± std |
| 2 | Box plot | Memperlihatkan sebaran dan stabilitas hasil nilai koherensi dari total 10 kali eksperimen (runs). | Semua data Cv dari 10 run |
| 3 | Scatter plot | Menunjukkan trade-off (kompromi) antara peningkatan koherensi topik berbanding dengan penambahan waktu komputasi akibat filter K-NN. | Mean Coherence vs Mean Time |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya. Karena sumbu Y tidak dimulai dari 0, perbedaan yang aslinya hanya 0.4% akan terlihat sangat ekstrem secara visual, seolah-olah Metode A dua kali lipat lebih baik dari Metode B. |
| Apakah error bar ditampilkan? | Tidak. Akibatnya, kita tidak tahu apakah perbedaan 0.4% itu benar-benar signifikan secara statistik atau sekadar variasi angka acak (noise). |
| Apakah semua kondisi ditampilkan? | Ya, jika diasumsikan eksperimen tersebut memang hanya membandingkan Metode A dan B. |
| Apa solusinya? | Atur sumbu Y agar dimulai dari 0 (atau mulai dari angka lain dengan justifikasi teks yang kuat). Tambahkan garis error bar (standar deviasi) pada masing-masing batang grafik. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [X] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: ____

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel dan grafik memiliki fungsi yang saling melengkapi. Tabel memberikan angka presisi yang eksak, yang sangat dibutuhkan oleh peneliti lain jika mereka ingin menjadikan metrik kita sebagai baseline (pembanding) di riset mereka selanjutnya. Di sisi lain, grafik sangat krusial untuk pengenalan pola secara cepat (pattern recognition). Saat melakukan presentasi sidang, audiens atau penguji bisa langsung menangkap tren "metode mana yang lebih unggul" hanya dalam waktu 5 detik melalui grafik, tanpa perlu membedah deretan angka desimal di dalam tabel.
