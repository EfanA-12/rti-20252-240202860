# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 9 slides (Target optimal untuk presentasi ringkas dan padat)
  Time per slide : ~1.5 - 2 menit
  Total time     : 15 menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Judul & Konteks: Analisis Sentimen & Topik SeaBank | Logo SeaBank & Judul | 1 min |
| 2 | Problem: Jutaan ulasan menumpuk, sulit diekstrak manual | Screenshot tumpukan ulasan Play Store | 2 min |
| 3 | Gap + RQ: Belum ada yang memfilter sentimen sebelum LDA di konteks ini | Tabel perbandingan literatur singkat | 1.5 min |
| 4 | Method: Alur dari Scraping -> Preprocessing -> K-NN -> LDA | Diagram alir (Flowchart) sistem | 2 min |
| 5 | Key Result (K-NN): Akurasi sangat tinggi (88.89%) | Confusion Matrix / Bar Chart akurasi | 2 min |
| 6 | Key Result (LDA): Topik 1 (CS) & Topik 2 (Pinjaman) | Word Cloud dari masing-masing topik | 2 min |
| 7 | Interpretation + Failure: Waktu komputasi cepat (0.09s), tapi ada noise kata slang | Highlight teks kata gaul ("gua", "nya") | 2 min |
| 8 | Limitation + Future: Sastrawi tak cukup, butuh kamus custom | Bullet points limitasi | 1.5 min |
| 9 | Conclusion + Contribution: K-NN sukses jadi filter yang baik untuk LDA | 1 Kalimat penutup & ucapan terima kasih | 1 min |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Method   | Mengapa memilih K-NN, bukan Naive Bayes atau SVM? | K-NN tangguh terhadap noise dan berkinerja baik pada data dengan dimensi tinggi seperti TF-IDF teks. |
| Results  | Kenapa masih ada kata tidak baku di hasil topik LDA? | Keterbatasan library Sastrawi yang hanya membaca bahasa baku. Ini temuan (boundary condition) penting. |
| Generalization | Apakah model ini bisa dipakai untuk aplikasi selain SeaBank? | Bisa, asalkan menggunakan bahasa Indonesia. Namun akurasi mungkin sedikit berbeda tergantung rasio kata slang-nya. |

Latihan:
  Latihan 1: [Kosongkan untuk diisi nanti] — [catatan timing & feedback]
  Latihan 2: [Kosongkan untuk diisi nanti] — [catatan timing & feedback]
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Title & Context: Pemodelan Topik Keluhan Pengguna SeaBank (K-NN + LDA). | Judul presentasi dan identitas mahasiswa. | 1 min |
| 2 | Problem: Developer kesulitan membaca ribuan ulasan Play Store untuk mencari bug. | Grafik lonjakan jumlah ulasan di aplikasi keuangan. | 2 min |
| 3 | Gap + RQ: LDA murni sering tercampur pujian. Bisakah K-NN memfilter sentimennya dulu? | Tabel matriks penelitian terdahulu. | 1.5 min |
| 4 | Method Overview: TF-IDF -> K-NN Filter -> LDA Topic Modeling. | Diagram blok arsitektur Machine Learning. | 2 min |
| 5 | Key Result (Tabel/Angka): K-NN berhasil mencapai akurasi 88.89% dalam 0.09 detik. | Tabel metrik evaluasi klasifikasi (Akurasi). | 2 min |
| 6 | Key Result (Grafik): Ekstraksi 2 Topik Utama (Layanan CS & Pengajuan Pinjaman). | Visualisasi Word Cloud kata kunci per topik. | 2 min |
| 7 | Interpretation & Failure: Sistem efisien, namun ditemui noise berupa bahasa informal. | Potongan screenshot hasil terminal dengan kata "gua" dan "yg". | 2 min |
| 8 | Limitation & Future: Validasi K-NN diuji pada sampel uji coba. Masa depan butuh Custom Stopword. | Poin-poin peluru (bullet points) ringkas. | 1.5 min |
| 9 | Conclusion: Pendekatan hybrid (K-NN + LDA) layak dan cepat digunakan di lingkungan produksi. | Ringkasan 1 paragraf singkat. | 1 min |

**Total waktu estimasi:** 15 menit
---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Method | Mengapa nilai K=3 pada K-NN? Kenapa tidak 5 atau 7? | K=3 memberikan keseimbangan optimal untuk data latih yang jumlahnya tidak masif. | Pada uji coba dengan porsi data split 80:20, K=3 menghasilkan akurasi 88.89%. | Angka K ganjil mencegah hasil seri (tie), dan K=3 mencegah overfitting yang sering terjadi jika K terlalu besar pada dataset kecil. |
| 2 | Results | Adanya kata "gua" dan "yg" di LDA berarti pre-processing Anda gagal? | Bukan gagal, melainkan identifikasi boundary condition (batasan) dari tools NLP Indonesia saat ini. | Hasil output LDA secara jelas menampilkan noise tersebut mendampingi kata kunci utama (nelfon, pinjam). | Library Sastrawi memang dirancang untuk EYD. Menemukan celah ini justru membuktikan bahwa saya tidak memanipulasi data dan sistem perlu Custom Dictionary. |
| 3 | Gap | Apa bedanya penelitian Anda dengan sentimen analisis biasa? | Penelitian ini tidak berhenti di label sentimen, tapi menggali makna di baliknya. | Alur sistem: setelah K-NN mengelompokkan ulasan "Negatif", data itu tidak dibuang, melainkan diumpankan ke LDA. | Mengetahui pengguna marah (sentimen negatif) tidak cukup bagi developer. Mereka perlu tahu pengguna marah KARENA APA (Topik LDA). |


---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|| *1* | *Contoh: "Mengapa tidak membandingkan dengan metode Y?"* | *Contoh: "Karena Y memerlukan dataset labeled yang tidak tersedia. Disebutkan sebagai limitasi di halaman X."* | *[✓] Direct [✓] Data-based [✓] Honest* |
| 1 | "Berapa banyak data ulasan yang idealnya dibutuhkan jika sistem ini benar-benar di-deploy?" | "Untuk LDA yang optimal, idealnya dibutuhkan di atas 1.000 ulasan. Sample 44 data ini hanya Proof of Concept." | [X] Direct [X] Data-based [X] Honest |
| 2 | "Apakah K-NN tidak terlalu lambat untuk memproses teks?" | "Di tahap training ya, tapi pada uji coba sistem saya, klasifikasi selesai dalam 0.09 detik karena TF-IDF sudah mereduksi dimensi teks." | [X] Direct [X] Data-based [X] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Menjelaskan metrik matematis dari algoritma pemodelan topik (bagaimana mesin menentukan bahwa "pinjam" dan "tahun" itu saling berkaitan).

**Apa yang perlu disiapkan lebih baik:**
> Harus membaca kembali rumus dasar probabilitas kemunculan kata pada Latent Dirichlet Allocation agar tidak gagap jika ditanya soal teori matematika di baliknya.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Bahwa "kegagalan" (seperti lolosnya kata gaul di proses Sastrawi) bukanlah sesuatu yang harus ditutupi. Jika dianalisis dengan kerangka Failure Analysis, kegagalan tersebut justru menjadi kontribusi ilmiah yang sangat berharga untuk mencegah peneliti lain melakukan kesalahan yang sama.

**Yang akan selalu diterapkan:**
> Prinsip Claim-Evidence-Reasoning (CER) saat menjawab pertanyaan. Saya tidak akan lagi menjawab pertanyaan penguji hanya dengan opini ("menurut saya..."), melainkan akan langsung menunjuk ke bukti data ("berdasarkan tabel akurasi di slide 5...").
