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

Research Question: Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang koheren (Coherence Score c_v >= 0.4) menggunakan model LDA pada ulasan aplikasi SeaBank?
Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Filter Sentimen (K-NN) | IV | Feature Toggle (Script Python) | Mengaktifkan/menonaktifkan (True/False) modul pemfilteran K-NN pada pipeline sebelum data masuk ke LDA. |
| Performa K-NN & LDA | DV | Modul Evaluator (Metrics Logger) | Mencatat F1-Score untuk klasifikasi K-NN dan menghitung Coherence Score (c_v) pada output model LDA secara otomatis. |
| Hyperparameters | CV | Configuration File (config.yaml) | Mengunci parameter nilai K pada K-NN, jumlah klaster topik pada LDA, dan random_state di file konfigurasi terpisah. |

4 Prinsip Desain:
  [X] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [X] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [X] Measurement Integration — Pengukuran DV built-in
  [X] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : Dataset CSV mentah hasil scraping ulasan Play Store SeaBank.
  Parameter      : Toggle 'use_knn_filter' (True/False), K_topics (misal: 3, 5, 7), num_words (10).
  Output format  : Matriks performa (Confusion Matrix, F1-Score) dan list kata kunci per topik beserta nilai Coherence-nya.
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah penggunaan algoritma K-NN sebagai filter sentimen negatif mampu menghasilkan ekstraksi topik keluhan usability yang koheren (Coherence Score c_v >= 0.4) menggunakan model LDA pada ulasan aplikasi SeaBank?
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Filter K-NN | IV | Python Conditional Logic (if/else) | Toggle switch pada kode utama untuk menentukan apakah teks disaring sentimen negatifnya atau tidak sebelum masuk LDA. |
| Performa (Coherence) | DV | Fungsi Gensim CoherenceModel | Dipanggil otomatis setiap epoch pelatihan LDA selesai untuk mencetak nilai Cv. |
| Hyperparameters (Nilai K, Topik, Seed) | CV | Modul pembaca Config YAML/JSON | Mengedit angka pada file config tanpa menyentuh satu baris pun logika core script algoritma. |

**Apakah semua variabel bisa di-map?** [X] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Modul K-NN terikat pada IV (Filter), Modul LDA & Gensim terikat pada DV (Koherensi Topik). |
| Modularity | ✅ | Modul LDA dapat menerima input berupa data mentah (raw) ataupun data tersaring K-NN (filtered) tanpa perlu merombak fungsi LDA-nya. |
| Controllability | ✅ | Jumlah topik (k-topics), random seed, dan batas kemunculan kata (min_df) disimpan rapi di config.yaml. |
| Measurability | ✅ | Nilai Accuracy, F1-Score, dan Coherence Score secara otomatis ditulis ke dalam file log .csv setiap kali eksperimen selesai running. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability pada tahap NLP preprocessing.
> Dalam riset NLP, langkah-langkah seperti stopword removal (menghapus kata sambung) dan stemming sering kali secara tidak sadar di-hardcode di tengah-tengah kode (script), bukan di parameter config, sehingga sulit dikontrol atau dimatikan saat melakukan iterasi eksperimen (Ablation Study).
---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ | ✅ | ✅ | F1-Score K-NN dan Coherence LDA mencapai nilai maksimal yang optimal. |
| – A | ❌  | ✅ | ✅ | Akurasi klasifikasi sedikit menurun karena kata bervariasi (berimbuhan) dianggap sebagai entitas/fitur yang berbeda oleh K-NN. |
| – B | ✅ | ❌  | ✅ | LDA akan menghasilkan topik noise (sampah), di mana kata seperti "dan", "yang" akan mendominasi hasil klaster keluhan. |
| – C | ✅ | ✅ | ❌  | Model kesulitan mendeteksi sentimen ekstrem (mengalami misklasifikasi) karena bobot kata kunci dan kata biasa disamaratakan. |

**Komponen mana yang diprediksi paling berkontribusi?** Stopword Removal (Komponen B).
**Mengapa?**
> Karena algoritma LDA bekerja berdasarkan frekuensi kemunculan kata yang berdekatan. Jika stopword (kata hubung) tidak dihapus, kata-kata tersebut akan muncul dengan frekuensi tertinggi di hampir setiap dokumen ulasan. Akibatnya, mesin akan menganggap kata hubung tersebut sebagai "topik utama", sehingga merusak nilai koherensi dan membuat topik tidak bisa diinterpretasikan.
---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Jika skrip eksperimen K-NN dan LDA ini dibangun seperti produk aplikasi utuh (monolithic) di mana scraping, preprocessing, filtering, dan evaluasi dijadikan satu file kode panjang tanpa pemisahan fungsi (modularitas), maka saat hasil eksperimen gagal (misal Coherence Score buruk), peneliti tidak akan tahu bagian mana yang salah. Apakah salah stemming-nya? Atau K-NN-nya yang bias? Arsitektur modular mutlak diperlukan dalam riset Data Science agar kita bisa melakukan sistem isolasi, menghidup-matikan fitur (Ablation Study) lewat config file, dan memastikan setiap variabel yang diuji benar-benar valid tanpa terdistorsi oleh tumpukan code yang rumit.
