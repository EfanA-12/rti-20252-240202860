# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     | LDA Tanpa Filter (Baseline) | 42   | K-NN=OFF, K-topics=5 | Planned | 09:00 | log_base_42.csv |
| 2     | LDA Tanpa Filter (Baseline) | 123  | K-NN=OFF, K-topics=5 | Planned | 09:10 | log_base_123.csv |
| 3     | LDA Tanpa Filter (Baseline) | 777  | K-NN=OFF, K-topics=5 | Planned | 09:20 | log_base_777.csv |
| 4     | LDA + Filter K-NN (Treatment)| 42   | K-NN=ON, K-topics=5  | Planned | 09:30 | log_treat_42.csv |
| 5     | LDA + Filter K-NN (Treatment)| 123  | K-NN=ON, K-topics=5  | Planned | 09:40 | log_treat_123.csv |
| 6     | LDA + Filter K-NN (Treatment)| 777  | K-NN=ON, K-topics=5  | Planned | 09:50 | log_treat_777.csv |

Jumlah runs per skenario : 3 (Minimal untuk menguji stabilitas Coherence Score)
Total runs               : 6

DATA LOG (per run):
  Run ID    : run-treat-042
  Timestamp : 2026-07-06T09:30:00
  Skenario  : Ekstraksi topik LDA menggunakan dataset ulasan yang sudah disaring sentimen negatifnya oleh K-NN.
  Input     : seabank_reviews_raw.csv (1000 ulasan)
  Output    : F1-Score K-NN: 85%, Coherence Score LDA: 0.45.
  Anomali   : Tidak ada.
  Catatan   : Proses stemming Sastrawi memakan waktu komputasi paling lama (~2 menit).
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| *1* | Baseline (Tanpa K-NN) | 42 | K-topics=5, passes=10 | Planned |
| *2* | Baseline (Tanpa K-NN) | 123 | K-topics=5, passes=10 | Planned |
| 3 | Baseline (Tanpa K-NN) | 777 | K-topics=5, passes=10 | Planned |
| 4 | Treatment (Dengan K-NN) | 42 | K-topics=5, passes=10 | Planned |
| 5 | Treatment (Dengan K-NN) | 123 | K-topics=5, passes=10 | Planned |
| 5 | Treatment (Dengan K-NN) | 777 | K-topics=5, passes=10 | Planned |

**Total skenario:** 2 (Baseline vs Treatment)
**Run per skenario:** 3
**Total run keseluruhan:** 6

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | 2 (Baseline vs Treatment) |
| Timestamp | 2026-07-06T09:05:12 |
| Skenario | LDA Tanpa Filter Sentimen |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | 42 |
| K-NN Filter Status | OFF / ON |
| LDA Parameters | num_topics=5, chunksize=100 |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| F1-Score (K-NN) | float | 0.0 – 1.0 |
| Coherence Score c_v (LDA) | float | 0.0 – 1.0 |
| Execution Time | float | > 0 (detik) |

**Format output:** [X] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Proses stemming Sastrawi memicu MemoryError di RAM. | Dokumentasikan error, kurangi ukuran batch (dari 1000 ke 500 ulasan), jalankan ulang, catat perubahan di config. |
| Hasil ekstrem | Coherence Score tiba-tiba anjlok menjadi 0.1 pada satu seed tertentu. | Jangan dihapus. Investigasi apakah seed tersebut memicu pengelompokan kata stopword menjadi satu klaster secara acak. Masukkan ke rata-rata akhir. |
| Waktu eksekusi anomali | Komputasi LDA berhenti merespons lebih dari 10 menit. | Hentikan paksa (kill process), periksa grafik usage CPU/RAM, bersihkan cache, lalu re-run. |
| Inkonsistensi dengan run lain | Topik yang diekstrak pada Run 1 sangat bagus, tapi di Run 2 isinya hanya kata acak. | Bukti bahwa algoritma tidak stabil. Tindakan: Dokumentasikan variabilitas ini, tambahkan nilai iterasi (passes=20) di LDA agar konvergen. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Dulu, saat melatih model Machine Learning untuk tugas kuliah, saya selalu menggunakan metode single run. Jika saat kode dijalankan akurasinya langsung mencapai 90%, saya langsung mengambil screenshot dan menjadikannya hasil akhir tanpa mencobanya lagi.
**Yang akan dilakukan berbeda:**
> Saya baru sadar bahwa algoritma seperti LDA bersifat sangat stokastik (probabilistik). Mendapat skor bagus pada single run bisa jadi hanyalah efek lucky seed (kebetulan angka acaknya pas). Ke depannya, saya wajib melakukan multiple runs dengan seed berbeda lalu merata-ratakan hasilnya. Ini akan menghapus bias kebetulan dan membuktikan bahwa pipeline K-NN dan LDA saya benar-benar tangguh dan bisa diandalkan (dapat direproduksi).