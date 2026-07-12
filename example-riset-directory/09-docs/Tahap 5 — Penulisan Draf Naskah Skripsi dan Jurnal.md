# Tahap 5 — Penulisan Draf Naskah Skripsi dan Jurnal

**Status:** Konten naskah selesai — naskah konsolidasi tersedia di [../07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md) & [../07-manuskrip/naskah-jurnal.docx](../07-manuskrip/naskah-jurnal.docx), tinjauan pustaka lengkap dengan 18 referensi terverifikasi (BibTeX di [../02-literatur/daftar-pustaka.bib](../02-literatur/daftar-pustaka.bib)). Sisa pekerjaan: keputusan bahasa final & pemindahan ke template jurnal tujuan (lihat "Yang Masih Perlu Dilengkapi").
**Bergantung pada:** [tahap-4-analisis-data.md](tahap-4-analisis-data.md) — *Selesai*

---

## Tujuan

Menyusun draf naskah ilmiah dengan gaya bahasa akademis formal, objektif, dan pasif, sesuai target publikasi Sinta 2 / Scopus Q3-Q4.

## Rencana Deliverable (Struktur Naskah)

| Bagian | File | Status |
|---|---|---|
| Naskah Konsolidasi Utuh | [../07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md), [../07-manuskrip/naskah-jurnal.docx](../07-manuskrip/naskah-jurnal.docx) | Selesai — Gabungan komprehensif Bab 1–5 beserta Abstrak. |
| Abstrak | [../07-manuskrip/01-abstrak.md](../07-manuskrip/01-abstrak.md) | Draf selesai (Tersedia versi ID & EN). |
| BAB 1: Pendahuluan | [../07-manuskrip/02-pendahuluan.md](../07-manuskrip/02-pendahuluan.md) | Selesai — Memuat latar belakang usability SeaBank, rumusan masalah arsitektur K-NN & LDA, tujuan, dan kontribusi. |
| BAB 2: Tinjauan Pustaka | [../07-manuskrip/03-tinjauan-pustaka.md](../07-manuskrip/03-tinjauan-pustaka.md) | Selesai — Mengulas landasan teori K-NN, TF-IDF, probabilitas LDA, serta research gap dari penelitian terdahulu. |
| BAB 3: Metodologi | [../07-manuskrip/04-metodologi.md](../07-manuskrip/04-metodologi.md) | Selesai — Menjabarkan alur sistem (Scraping → Sastrawi → Ekstraksi TF-IDF → Filter K-NN → LDA). |
| BAB 4: Hasil & Pembahasan | [../07-manuskrip/05-hasil-analisis.md](../07-manuskrip/05-hasil-analisis.md) | Selesai — Melaporkan akurasi K-NN (88,89%), ekstraksi topik (CS & Pinjaman), dan Failure Analysis batasan Sastrawi. |
| BAB 5: Kesimpulan & Saran | [../07-manuskrip/06-kesimpulan.md](../07-manuskrip/06-kesimpulan.md) | Selesai — Menyimpulkan efisiensi arsitektur hibrida dan merekomendasikan perancangan Custom Stopword Dictionary. |
| Daftar Pustaka | [../07-manuskrip/07-daftar-pustaka.md](../07-manuskrip/07-daftar-pustaka.md) | Selesai — Format sitasi akademik yang merujuk pada jurnal sumber. |


## Yang Masih Perlu Dilengkapi Sebelum Submit

1. Pemindahan ke Template Resmi Kampus / Jurnal: Melakukan penyalinan (copy-paste) konten dari draf naskah_skripsi_final.docx ke dalam template Microsoft Word resmi yang diterbitkan oleh Universitas Putra Bangsa (atau template jurnal tujuan jika akan di-publikasikan).
2. Penempatan Visualisasi dan Tabel: Mengatur posisi dan resolusi gambar (seperti Confusion Matrix, Word Cloud, dan diagram batang probabilitas LDA) serta menomori tabel sesuai gaya selingkung.
3. Pengecekan Format Sitasi: Memastikan seluruh daftar pustaka telah di-format secara konsisten (misalnya menggunakan gaya IEEE atau APA) dan sinkron dengan kutipan di dalam teks (in-text citation).
4. Lengkapi Metadata: Mengisi data pribadi (NIM), nama dosen pembimbing, lembar pengesahan, dan afiliasi pada halaman sampul naskah.

## Catatan

Bagian Hasil & Pembahasan mengacu langsung pada output metrik algoritma Scikit-Learn (Tahap 4). Ringkasan eksekutif secara teknis juga telah dirangkum dalam format portofolio pada dokumen Laporan Penelitian.
