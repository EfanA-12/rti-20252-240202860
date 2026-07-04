# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : AMD Ryzen 5 6600H / AMD Ryzen 7 7735HS (Pilih sesuai varian Anda)
  RAM     : 16 GB LPDDR5
  GPU     : AMD Radeon Integrated Graphics (CPU-only untuk pipeline NLP)
  Storage : 512 GB SSD

Software:
  OS        : Windows 11
  Runtime   : Python 3.10.x
  Framework : Scikit-Learn Ecosystem & JASP v0.18.3

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
| scikit-learn | 1.3.2 | PyPI (pip) | Kunci via pip freeze |
| pandas | 2.1.4 | PyPI (pip) | Kunci via pip freeze |
| Sastrawi | 1.0.1 | PyPI (pip) | Kunci via pip freeze |
| google-play-scraper | 1.2.4 | PyPI (pip) | Kunci via pip freeze |
| scipy | 1.11.4 | PyPI (pip) | Kunci via pip freeze |

Konfigurasi:
  Config file     : config.yaml (Menyimpan parameter NLP dan batas skenario tugas)
  Random seed     : 42 (Dikunci untuk split dataset dan inisialisasi K-NN)
  Hyperparameters : K=5 (K-NN), Distance metric='cosine'

Reproducibility Check:
  [X] Dependency terdokumentasi (requirements.txt / lock file)
  [X] Seed ditetapkan di semua level (Python, NumPy, framework)
  [X] Config di version control
  [X] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | AMD Ryzen 5 6600H |
| RAM | 16 GB LPDDR5 |
| GPU | AMD Radeon Integrated Graphics |
| OS | Windows 11 |
| Runtime | Python 3.10.x |
| Framework | Scikit-Learn & JASP Kuantitatif |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| scikit-learn | 1.3.2 | Untuk pemodelan klasifikasi sentimen menggunakan algoritma K-NN. |
| Sastrawi | 1.0.1 | Melakukan proses stemming bahasa Indonesia pada ulasan Play Store. |
| google-play-scraper | 1.2.4 | Melakukan scraping data sekunder ulasan SeaBank langsung dari Play Store. |
| pandas | 2.1.4 | Melakukan manipulasi data, pembersihan teks, dan manajemen data tabular. |
| scipy | 1.11.4 | Menyediakan komputasi statistik pendukung untuk perhitungan korelasi akhir. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | Akurasi Sentimen K-NN & Koefisien Korelasi | — |
| 2 | 42 | Akurasi Sentimen K-NN & Koefisien Korelasi | [X] Ya / [ ] Tidak |
| 3 | 42 | Akurasi Sentimen K-NN & Koefisien Korelasi | [X] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**

Hasil bisa berbeda jika random_state pada pembagian data (train-test split) tidak dikunci di level NumPy, atau jika terdapat data ulasan baru yang masuk tanpa dikunci rentang tanggal penarikannya, sehingga menyebabkan state data berubah di setiap run.

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [X] Random seed di-set di semua level
- [X] Tidak ada background process yang mengganggu
- [X] Cache dibersihkan antar-run
- [X] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Triangulasi Usability SeaBank via K-NN Sentimen & Eksperimen SUS

## 1. Environment
> CPU: AMD Ryzen (Advan Workplus), RAM: 16 GB LPDDR5, OS: Windows 11
> Runtime: Python 3.10.x

## 2. Installation
> Pastikan Python sudah terinstal, lalu jalankan perintah: `pip install -r requirements.txt`

## 3. Data
> Data Sekunder: `seabank_reviews.csv` (1000 ulasan ter-scrape dari Google Play Store).
> Data Primer: `usability_matrix.csv` (Skor SUS & Success Rate dari 30 responden).

## 4. Execution
> Jalankan pipeline NLP dan analisis korelasi dengan command: `python run_experiment.py --config config.yaml`

## 5. Configuration
> Diatur melalui `config.yaml`: `model: {type: 'knn', k: 5}, experiment: {seed: 42}`

## 6. Expected Output
> File `results.txt` berisi evaluasi matriks K-NN (Accuracy, F1-Score) dan nilai p-value uji korelasi Spearman.
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [X] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Saat ini riset baru memenuhi level repeatability karena hasil komputasi K-NN dan korelasi statistik sudah konsisten saat diuji ulang di perangkat lokal (Advan Workplus). Namun, aspek reproducibility masih terhambat karena ketergantungan pada platform perekaman pengujian usability eksternal serta belum adanya isolasi environment berbasis container seperti Docker, yang berpotensi memunculkan perbedaan perilaku pustaka (library dependency) saat dijalankan oleh peneliti lain di mesin yang berbeda.