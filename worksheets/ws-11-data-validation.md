# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [X] Semua skenario tercakup
  [ ] Jumlah run sesuai rencana
  [X] Tidak ada file output hilang
  Missing: 1 dari 20 data points

Format Consistency:
  [X] Semua file format sama (CSV/JSON/...)
  [X] Header konsisten
  [X] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [X] Nilai dalam range masuk akal
  [X] Tidak ada waktu negatif
  [X] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: Coherence Score anjlok drastis pada Run ke-4 di skenario Treatment.

Cross-Validation:
  [X] Run identik → hasil mendekati
  [X] Trend konsisten dengan ekspektasi teori

Keputusan:
  [ ] Data siap analisis
  [ ] Perlu cleaning
  [X] Perlu re-run (skenario: Treatment / Filter K-NN ON)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Baseline (LDA Tanpa Filter) | 10 | 10 | 0 | — |
| Treatment (LDA + K-NN Filter) | 10 | 9 | 1 | Skrip terhenti (crash) karena MemoryError saat iterasi Gensim pada Run ke-7. |

**Total expected:** 20 | **Total actual:** 19 | **Missing:** 1

**Keputusan untuk data missing:**
> _Melakukan re-run (eksekusi ulang) khusus untuk 1 run yang gagal pada skenario Treatment. Sebelum eksekusi, cache RAM akan dibersihkan (garbage collection) agar tidak terjadi MemoryError lagi, sehingga data point kembali genap menjadi 20.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | 0.45 |
| 2 | 0.46 |
| 3 | 0.44 |
| 4 | 0.21 |
| 5 | 0.47 |

**Deteksi outlier:**
- Q1 = 0.44 | Q3 = 0.46 | IQR = 0.02
- Batas bawah (Q1 - 1.5×IQR) = 0.41
- Batas atas (Q3 + 1.5×IQR) = 0.49
- Outlier terdeteksi: 0.21 (Run 4)

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| Run 4 | 0.21 | Unlucky seed (angka acak) pada algoritma LDA secara kebetulan mengelompokkan kata-kata noise (stopword) menjadi satu topik dominan. | Tidak dihapus. Tetap dimasukkan ke dalam kalkulasi statistik karena algoritma LDA memang bersifat probabilistik. Ini adalah temuan sah, bukan error system. |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 95% data terkumpul
**2. Format:** [X] Konsisten / [ ] Ada inkonsistensi: ____
**3. Range check (anomali):** Ditemukan 1 outlier statistik pada nilai Cv, namun nilai tersebut masih berada dalam range logis (0.0 hingga 1.0).
**4. Logic check:** [X] Parameter sesuai plan / [ ] Ada ketidaksesuaian: ____

**Kesimpulan:** [ ] Data siap analisis / [X] Perlu tindakan:Melakukan 1 kali re-run untuk melengkapi data yang missing, setelah itu data valid untuk diuji statistik.

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Data yang benar adalah data yang dicatat oleh sistem persis seperti apa adanya tanpa manipulasi. Namun, itu belum tentu "data yang dipercaya" (Trusted Data). Data yang dipercaya adalah data yang telah melalui logic check dan divalidasi keabsahannya. Proses validasi formal mutlak diperlukan pada riset Machine Learning, karena meskipun logger Python bekerja otomatis, sistem bisa saja mencatat angka 0 bukan karena akurasi modelnya jelek, melainkan karena script-nya mengalami timeout atau datanya kosong. Validasi memastikan angka yang kita proses murni hasil kinerja algoritma, bukan hasil dari kelemahan sistem komputer.
