# Rencana Penelitian: Analisis Sentimen dan Ekstraksi Topik Keluhan Usability SeaBank dengan K-NN dan LDA

## 1. Ringkasan

| Item | Keterangan |
|---|---|
| Judul | Analisis Sentimen dan Ekstraksi Topik Keluhan Usability pada Aplikasi SeaBank Menggunakan Algoritma K-NN dan Latent Dirichlet Allocation (LDA) |
| Target Publikasi | Sinta 5 |
| Stack | Python, Scikit-Learn, Sastrawi, Regex, google-play-scraper |
| Masalah | Pemodelan topik (LDA) konvensional pada ulasan aplikasi sering mencampuradukkan sentimen positif dan negatif, serta adanya noise dari bahasa slang/informal. |
| Solusi | Arsitektur hibrida berurutan (K-NN K=3 sebagai filter awal sentimen negatif + LDA untuk ekstraksi topik spesifik) disertai Failure Analysis kelemahan pustaka Sastrawi. |

## 2. Alur Kerja (Roadmap)

Setiap tahap memiliki file rencana detail tersendiri agar lebih rapi:

- [x] **Tahap 1** — Pengumpulan dan Pra-pemrosesan Data (Scraping) — Selesai
- [x] **Tahap 2** — Ekstraksi Fitur & Klasifikasi K-NN — Selesai
- [x] **Tahap 3** — Pemodelan Topik (LDA) — Selesai
- [x] **Tahap 4** — Evaluasi Metrik K-NN & Failure Analysis — Selesai
- [X] **Tahap 5** — Draf Jurnal — Selesai

---

## 3. Catatan

Dokumen ini adalah indeks utama. Detail teknis, parameter algoritma (seperti K=3 dan n_components=2), serta hasil evaluasi Confusion Matrix masing-masing tahap dicatat pada file tahap-N-*.md terkait dan diperbarui seiring progres pengerjaan.