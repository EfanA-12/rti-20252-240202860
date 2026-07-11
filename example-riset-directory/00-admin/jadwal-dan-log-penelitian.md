# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: riwayat commit git & dokumen `09-docs/tahap-N-*.md`). Tanggal mengikuti `git log`.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 11 Juli 2026 | Tahap 1 | Pengumpulan data sekunder: Scraping 50 ulasan aplikasi SeaBank dari Google Play Store menggunakan library google-play-scraper. | scraper_seabank.py, seabank_reviews_raw.csv |
| 11 Juli 2026 | Tahap 2 | Preprocessing Data: Melakukan case folding, pembersihan simbol (regex), stopword removal, dan stemming menggunakan Sastrawi. Menyisakan 44 data bersih. | preprocessing_seabank.py, seabank_reviews_clean.csv |
| 11 Juli 2026 | Tahap 3 | Eksekusi K-NN: Pembobotan TF-IDF dan pembagian data latih/uji (80:20). Mendapatkan tingkat akurasi klasifikasi sentimen sebesar 88.89%. | eksekusi_model.py |
| 11 Juli 2026 | Tahap 4 |Eksekusi LDA: Pemodelan 2 topik keluhan utama menggunakan Scikit-Learn. Ditemukan noise kata slang sebagai bahan Failure Analysis. | eksekusi_model.py, Bab 14 |
| 12 Juli 2026 | Tahap 5 |Penyusunan Laporan: Melengkapi dokumentasi metodologi (WS-1 s.d. WS-16). | Dokumen WS, Laporan Akhir |

## Status Ringkas

- **Tahap 1–4**: Selesai (dataset final: matrix 400 run / 40 replikasi per kombinasi, 2026-06-15).
- **Tahap 5**: Konten naskah selesai dengan statistik n=40 (termasuk tinjauan pustaka & verifikasi CVE-2026-48524); menyisakan keputusan bahasa final dan pemindahan ke template jurnal tujuan (dilakukan oleh peneliti).

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Menyelesaikan kode penarikan dan pembersihan data ulasan.
- [x] Mendapatkan nilai metrik performa K-NN (88.89%) dan hasil pemodelan LDA.
- [ ] Menyusun kamus stopword manual (Custom Dictionary) untuk mengatasi bahasa informal.
- [ ] Memindahkan seluruh kerangka draf tulisan ini ke dalam template proposal skripsi resmi.
- [ ] Mengecek ulang format sitasi dan daftar pustaka.

## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan pembimbing/editor jurnal di sini saat tersedia)*
