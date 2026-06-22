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

Research Question: Apakah tingkat kepuasan (SUS) dan keberhasilan tugas (success rate) pada antarmuka aplikasi SeaBank melampaui standar kelayakan rata-rata industri?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem (Setup Eksperimen) | Cara Manipulasi/Pengukuran |
|----------|------|------------------------------------|---------------------------|
| Antarmuka SeaBank | IV | Smartphone Testbed dengan aplikasi SeaBank terinstal | Mengatur alur task scenario (skenario tugas) yang harus diselesaikan pengguna. |
| Metrik Usability (Waktu, Error, SUS) | DV | Screen Recorder (waktu & error) & Google Forms (SUS) | Mengumpulkan log durasi dari video dan menarik data spreadsheet dari kuesioner. |
| Lingkungan & Alat Uji | CV | Ruangan pengujian, koneksi Wi-Fi, tipe Smartphone | Menyeragamkan device dan jaringan internet untuk semua partisipan agar tidak ada lag teknis. |

4 Prinsip Desain:
  [X] Traceability — Setiap variabel (waktu, kepuasan) diukur oleh alat spesifik (recorder, G-Forms).
  [X] Variable Isolation — Skenario tugas (IV) dapat diubah tanpa mengganggu format kuesioner SUS.
  [X] Measurement Integration — Perekaman layar otomatis menyimpan data waktu dan jumlah klik/error.
  [X] Reproducibility — Protokol pengujian tertulis jelas (device, jaringan, instruksi) sehingga eksperimen bisa diulang persis oleh orang lain.

Experimental Setup:
  Input data     : Interaksi layar dari partisipan (tap, scroll, input teks) saat menjalankan aplikasi SeaBank.
  Parameter      : 3 Skenario Tugas (Task A: Transfer, Task B: Cek Riwayat, Task C: Deposito) dengan durasi maksimal tiap tugas dibatasi 3 menit.
  Output format  : Video rekaman layar (MP4) untuk observasi error/waktu, dan Spreadsheet (CSV) berisi skor kuesioner SUS.
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** __________________________________________________

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Antarmuka SeaBank | *IV* | Aplikasi Mobile SeaBank (Production version) | Memberikan instruksi Task Scenario spesifik kepada partisipan. |
| Metrik Usability | DV | Alat Observasi (Screen Recorder & Kuesioner Digital) | Mencatat waktu di stopwatch, menghitung miss-click di video, dan merekap skor SUS. |
| Kondisi Pengujian | CV | Protokol Standar Lingkungan | Menggunakan satu tipe HP yang sama dan script instruksi yang identik untuk semua user. |

**Apakah semua variabel bisa di-map?** [X] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ Memenuhi | Sangat jelas. Jika ingin mengecek data efficiency (waktu), kita merujuk pada Screen Recorder. Jika data satisfaction, kita merujuk ke G-Forms. |
| Modularity | ✅ Memenuhi | Alat perekam layar, aplikasi SeaBank, dan G-Forms berjalan secara terpisah. Jika kita ingin mengganti aplikasi (misal membandingkan dengan Bank Jago), setup ini tetap bisa jalan. |
| Controllability | ✅ Memenuhi | Lingkungan fisik partisipan dan perangkat dikunci (CV). Interupsi eksternal (notifikasi HP, sinyal hilang) dimitigasi dengan mode Do Not Disturb dan Wi-Fi lab. |
| Measurability | ✅ Memenuhi | Pengambilan metrik tidak bersifat recall (ingatan partisipan), melainkan data empiris objektif yang terekam secara sinkron dalam format MP4 dan CSV. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability
**Strategi untuk mengatasinya:**
> Dalam pengujian usability manusia (HCI), mengontrol emosi atau kondisi internal partisipan sangat sulit (misal mereka sedang lelah atau moody). Strategi mitigasinya adalah melakukan sesi ice breaking ringan sebelum tes, dan membuat suasana pengujian sesantai mungkin agar kecemasan tidak memengaruhi error rate.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ Diuji | ✅ Diuji | ✅ Diuji | Baseline SUS keseluruhan |
| – A | ❌ (Tanpa task transfer) | ✅ | ✅ | Jika SUS naik drastis, berarti alur Transfer sangat buruk. |
| – B | ✅ | ❌ (Tanpa task riwayat) | ✅ | Melihat dampak UI Mutasi terhadap UX. |
| – C | ✅ | ✅ | ❌ (Tanpa task deposito) | Jika SUS naik drastis, UI Deposito adalah penyebab utama frustrasi pengguna. |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen C (Fitur Deposito)
**Mengapa?**
> Karena alur pembukaan fitur deposito bank digital biasanya memiliki term & condition yang kompleks, tombol navigasi berlapis, dan istilah finansial yang kurang dipahami pengguna awam. Hal ini akan meningkatkan cognitive load (beban kognitif) dan durasi waktu penyelesaian secara signifikan.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Jika sebuah pengujian dieksekusi secara monolitik (partisipan disuruh menggunakan seluruh aplikasi SeaBank secara acak lalu langsung disuruh mengisi SUS tanpa pemisahan task), risikonya adalah kita tidak akan tahu "titik penyakit" utamanya. Hasil eksperimen hanya akan menghasilkan kesimpulan "Aplikasi ini buruk/membingungkan", tetapi tidak menghasilkan data "Bagian mana yang buruk?".
