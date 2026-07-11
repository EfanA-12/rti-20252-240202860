# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : seabank_reviews_raw.csv (Data sekunder Google Play Store)
Jumlah data awal  : 50 ulasan 
Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing Values & Duplikat | 6 baris | Dihapus menggunakan listwise deletion (dropna) dan drop_duplicates di Pandas. | Teks kosong tidak bisa diproses NLP, dan data duplikat akan merusak pembobotan kata (TF-IDF). |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Case Folding | teks_ulasan | Mengubah semua huruf menjadi lowercase menggunakan fungsi .lower(). | Menyeragamkan format agar mesin tidak membedakan "SeaBank" dan "seabank". |
| Text Cleansing | teks_ulasan | Menghapus angka dan karakter non-alfabet menggunakan Regex (Regular Expression). | Menghilangkan noise yang tidak memiliki makna topikal. |
| Stopword Removal | teks_ulasan | Menghapus kata hubung menggunakan library Sastrawi. | Mencegah kata hubung mendominasi klaster topik pada algoritma LDA. |
| Stemming | teks_ulasan | Mengubah kata berimbuhan menjadi kata dasar (contoh: "membantu" -> "bantu") via Sastrawi. | Mengurangi dimensi fitur agar LDA dan K-NN lebih fokus pada makna inti kata. |

Normalization:
  Metode    : TF-IDF (Term Frequency-Inverse Document Frequency)
  Alasan    : Mengubah teks menjadi vektor numerik pembobotan sebelum masuk ke algoritma K-NN.
  Parameter : Dihitung dari: Training Set saja (untuk K-NN).

Leakage Check:
  [X] Parameter normalisasi dari training set saja
  [X] Tidak ada informasi test set dalam preprocessing
  [X] Cross-validation dilakukan setelah split

Jumlah data akhir : 44 ulasan bersih siap analisis.
Script tersedia   : [X] Ya → path: ____ | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing values (teks kosong) dan Duplikasi | 6 baris | Listwise deletion (dropna) dan penghapusan duplikat (drop_duplicates) | Teks kosong dan teks yang berulang-ulang tidak memiliki nilai informasi untuk diekstrak topiknya. |


**Jumlah data sebelum cleaning:** 50 ulasan
**Jumlah data setelah cleaning:** 44 ulasan
**Persentase data yang hilang/berubah:** 12%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Teks Ulasan | Panjang kata bervariasi | Beragam | Tidak Relevan | TF-IDF Vectorizer | K-NN membutuhkan input berupa angka (vektor), bukan teks. TF-IDF menormalisasi bobot kata berdasarkan kelangkaannya. |

**Apakah normalisasi diperlukan?** [X] Ya / [ ] Tidak
**Justifikasi:**
> Ya. Algoritma K-NN menghitung jarak antar data secara matematis. Teks ulasan yang berformat string mutlak harus diubah (dinormalisasi) menjadi matriks angka menggunakan TF-IDF.

**Leakage check:**
- [X] Parameter dihitung dari training set saja
- [X] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: seabank_reviews_raw.csv
2. Data awal: 50 records
3. Cleaning:
   - Missing & Duplikat: 6 kasus, metode: Listwise deletion (dropna & drop_duplicates)
4. Transformation: Case Folding -> Regex Cleansing -> Stopword Removal (Sastrawi) -> Stemming (Sastrawi).
5. Normalisasi: TF-IDF Vectorization, parameter dihitung (fit) dari Training Set.
6. Data akhir: 44 records yang tersimpan di seabank_reviews_clean.csv.
7. Leakage check: [X] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Pada pemrosesan teks, risiko over-preprocessing sangat nyata. Terkadang proses stemming bisa memotong kata secara agresif dan mengubah makna konteks. Dari uji coba 50 data awal, terbukti bahwa proses cleansing membuang simbol dan angka, sementara stemming Sastrawi sukses memadatkan dimensi kata (misal: "membantu" menjadi "bantu"). Minimal distortion harus dijaga agar ciri khas emosi atau keluhan pada ulasan pengguna tidak hilang sepenuhnya akibat proses pembersihan yang terlalu ketat.
