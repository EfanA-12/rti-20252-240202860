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
| 1 | K-NN Sentiment (K=5) & Uji Korelasi | 42 | test_size=0.2, metric=cosine | Planned | 10:00 | run_01_results.csv |
| 2 | K-NN Sentiment (K=5) & Uji Korelasi | 123 | test_size=0.2, metric=cosine | Planned | 10:15 | run_02_results.csv |
| 3 | K-NN Sentiment (K=5) & Uji Korelasi | 777 | test_size=0.2, metric=cosine | Planned | 10:30 | run_03_results.csv |
| 4 | K-NN Sentiment (K=5) & Uji Korelasi | 1024 | test_size=0.2, metric=cosine | Planned | 10:45 | run_04_results.csv |
| 5 | K-NN Sentiment (K=5) & Uji Korelasi | 2024 | test_size=0.2, metric=cosine | Planned | 11:00 | run_05_results.csv |

Jumlah runs per skenario : 5 (Untuk menguji stabilitas pembagian data latih/uji K-NN)
Total runs               : 5

DATA LOG (per run):
  Run ID    : run_knn_sus_01
  Timestamp : 2026-07-05T10:00:00
  Skenario  : ____________________
  Input     : ____________________
  Output    : ____________________
  Anomali   : ____________________
  Catatan   : ____________________
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| *1* | *Contoh: BERT-base, DS-1* | *42* | *lr=2e-5, epoch=10* | *Planned* |
| *2* | *BERT-base, DS-1* | *123* | *lr=2e-5, epoch=10* | *Planned* |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Total skenario:** ____
**Run per skenario:** ____
**Total run keseluruhan:** ____

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | *run-001* |
| Timestamp | *2025-03-15T10:30:00* |
| | |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | *42* |
| Code version | *commit abc1234* |
| | |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| *Contoh: Accuracy* | *float* | *0.0 – 1.0* |
| | | |
| | | |

**Format output:** [ ] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | *Contoh: OOM pada batch_size=64* | *Contoh: Dokumentasi, re-run batch_size=32, catat perubahan* |
| Hasil ekstrem | | |
| Waktu eksekusi anomali | | |
| Inkonsistensi dengan run lain | | |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> ___________________________________________________
**Yang akan dilakukan berbeda:**
> ___________________________________________________
