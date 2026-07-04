# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah terdapat korelasi yang signifikan antara rasio sentimen negatif publik (berbasis K-NN pada ulasan Play Store) dengan metrik performa objektif (Skor SUS dan Task Success Rate) pada aplikasi SeaBank?
Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
|     Sentimen Publik     | IV   |        Pipeline NLP & Modul Klasifikasi K-NN         |             Mengubah parameter nilai K atau teknik ekstraksi fitur (TF-IDF).              |
|     Skor SUS & Success Rate     | DV   |        Modul Usability Testing (Task Tracker & Kuesioner Digital)         |              Pencatatan log otomatis (waktu/keberhasilan) dan kalkulasi skor otomatis.             |
|     Demografi Pengguna     | CV   |        Modul Screening Responden         |             Filter parameter pada kuesioner pra-task (lama penggunaan SeaBank).              |

4 Prinsip Desain:
  [X] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [X] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [X] Measurement Integration — Pengukuran DV built-in
  [X] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : Dataset CSV ulasan Play Store dan Aksi klik partisipan saat eksperimen.
  Parameter      : Nilai K pada K-NN, Ambang batas waktu skenario tugas.
  Output format  : Matriks kebingungan (Confusion Matrix) untuk sentimen, dan skor rata-rata SUS.
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah terdapat korelasi yang signifikan antara rasio sentimen negatif publik (berbasis K-NN pada ulasan Play Store) dengan metrik performa objektif (Skor SUS dan Task Success Rate) pada aplikasi SeaBank?
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Sentimen Publik | IV | Skrip Analisis K-NN (Python) | Konfigurasi hyperparameter nilai K pada model classifier. |
| Performa Objektif | DV | Platform Evaluasi (misal: Maze / Google Forms) | Data diukur dari log timestamp dan rekaman layar otomatis pengguna. |
| Pengalaman Pengguna | CV | Screening Form (Penyaring Awal) | Mengunci partisipan yang minimal sudah 3 bulan menggunakan SeaBank. |

**Apakah semua variabel bisa di-map?** [X] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Modul K-NN melayani IV (Sentimen), Modul Evaluasi melayani DV (SUS & Performa). |
| Modularity | ✅ | Algoritma preprocessing teks (K-NN) terpisah dari skrip scraping data Play Store. |
| Controllability | ✅ | Parameter nilai K dan kriteria screening disimpan dalam file config terpisah, bukan di-hardcode. |
| Measurability | ✅ | Sistem kuesioner digital otomatis menghitung skor akhir SUS tanpa intervensi manual. |

**Prinsip mana yang paling sulit dipenuhi?** Measurability terotomatisasi pada bagian Task Success Rate.
> Jika tidak memiliki akses ke backend SeaBank untuk logging otomatis, pengumpulan data dilakukan dengan merekam layar gawai (screen recording) partisipan saat eksperimen, lalu error dicatat melalui observasi terstruktur.
---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ | ✅ | ✅ | Akurasi klasifikasi sentimen K-NN maksimal (Baseline penuh). |
| – A | ❌ | ✅ | ✅ | Penurunan akurasi karena kata berimbuhan dianggap kata berbeda. |
| – B | ✅ | ❌ | ✅ | Noise data tinggi karena kata hubung (dan, di, ke) ikut terhitung. |
| – C | ✅ | ✅ | ❌ | Model kesulitan mendeteksi sentimen karena bobot kata unik dan kata umum disamakan (Raw Count). |

**Komponen mana yang diprediksi paling berkontribusi?** TF-IDF Weighting (Komponen C).
**Mengapa?**
> Karena dalam analisis ulasan Play Store yang singkat dan padat, pemberian bobot (TF-IDF) sangat krusial untuk menonjolkan kata kunci sentimen (seperti "error", "lambat", "mantap") dibandingkan sekadar menghitung frekuensi kata biasa.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Sistem riset tidak boleh bersifat monolitik karena akan memicu noise pada data dan menyulitkan isolasi variabel. Sebaliknya, arsitektur riset wajib dibuat modular agar setiap komponennya dapat ditelusuri kaitannya dengan variabel (traceable), mudah dihidup-matikan untuk ablation study (feature toggles), dan parameternya dapat diatur melalui file konfigurasi tanpa perlu membongkar kode utama (controllability).
