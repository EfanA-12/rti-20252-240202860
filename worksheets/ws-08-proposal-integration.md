# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment)
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [X] Problem → Gap: masalah terdokumentasi di literatur
  [X] Gap → RQ: pertanyaan menjawab gap spesifik
  [X] RQ → Hypothesis: hipotesis memprediksi jawaban
  [X] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [X] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [X] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [X] Istilah sama di semua bagian
  [X] Variabel di RQ = variabel di hipotesis = metrik di desain
  [X] Scope tidak berubah dari masalah ke eksperimen

Rubrik Self-Assessment:
| Kriteria | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor |
|----------|-----------|-----------|----------|------|
| Koherensi |          |           |     X     |      |
| Specificity |        |           |     X     |      |
| Feasibility |        |      X     |          |      |
| Rigor     |          |      X     |          |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Nasabah SeaBank mengalami kebingungan navigasi pada fitur esensial (riwayat transaksi dan deposito) yang memicu beban kognitif tinggi dan berisiko menurunkan kepercayaan pengguna. |
| Gap | WS-03 | Belum banyak evaluasi pada bank digital murni (branchless banking) yang memadukan pengujian observasi unjuk kerja (Task Scenario) secara bersamaan dengan kuesioner baku (SUS). |
| RQ | WS-04 | Apakah tingkat kepuasan (berdasarkan System Usability Scale) dan tingkat keberhasilan tugas (success rate) pada antarmuka aplikasi SeaBank secara signifikan melampaui standar kelayakan rata-rata industri (SUS > 68)? |
| Hipotesis | WS-04 | Rata-rata skor kepuasan (SUS) pengguna aplikasi SeaBank secara signifikan melampaui ambang batas standar kelayakan (Skor SUS > 68). |
| Variabel & Metrik | WS-05 | Variabel Independen (IV) = Antarmuka Aplikasi (UI/UX) SeaBank; Variabel Dependen (DV) = Tingkat Usability dengan metrik Task Success Rate (%), Time-based Efficiency (detik), dan Skor SUS (0-100 poin). |
| Sistem | WS-06 | Sistem yang diuji adalah aplikasi mobile SeaBank versi produksi terbaru dengan fokus pada modul pencarian mutasi dan simulasi deposito, diuji menggunakan gawai di lingkungan laboratorium yang terkontrol. |
| Desain Eksperimen | WS-07 | Eksperimen komparatif di mana performa antarmuka SeaBank (kondisi intervensi) diukur lewat 3 Task Scenario pada 6 partisipan dan kuesioner SUS pada 30 responden, lalu dibandingkan dengan baseline kelayakan global (kondisi kontrol SUS > 68) menggunakan uji One-Sample T-Test. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Gap muncul dari tinjauan 15 literatur nasional yang terbukti hanya menggunakan survei afektif (UEQ/PIECES) tanpa task scenario pada branchless banking. |
| Gap → RQ | ✅ | RQ secara langsung menanyakan pengukuran metrik objektif (success rate) dan subjektif (SUS) yang hilang di studi sebelumnya. |
| RQ → Hypothesis | ✅ | memprediksi bahwa nilai dari pengujian SUS akan melampaui standar (skor > 68) yang ditanyakan pada RQ. |
| Hypothesis → Metric | ✅ | Hipotesis secara spesifik menyebutkan "Skor SUS", yang mana merupakan metrik yang diukur dengan skala 0-100 poin. |
| Metric → System | ✅ | Metrik waktu (detik) dan success rate (%) dihasilkan langsung dari observasi interaksi pengguna dengan sistem (Aplikasi SeaBank) menggunakan screen recorder. |
| System → Experiment | ✅ | Desain eksperimen menggunakan skenario uji (3 Task Scenario) yang mengharuskan partisipan berinteraksi langsung dengan sistem aplikasi SeaBank. |

**Koneksi mana yang paling lemah?** _______________________
**Bagaimana cara memperkuatnya?**
> Koneksi yang mungkin paling rentan adalah "Metric → System" karena metrik waktu sangat bergantung pada latensi jaringan aplikasi saat diuji. Cara memperkuatnya adalah dengan memastikan variabel kontrol (seperti kecepatan Wi-Fi dan spesifikasi smartphone) benar-benar dijaga ketat (konstan) selama eksperimen berlangsung.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [X] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Alur logika dari rumusan masalah (beban kognitif pada antarmuka) hingga ke pemilihan metode pengujian (Task Scenario & SUS) sangat jelas, selaras, dan terhubung erat tanpa ada lompatan asumsi. |
| Specificity | 3 | Variabel dan metrik pengukuran telah didefinisikan dengan sangat spesifik dalam batasan angka pasti, yaitu Task Success Rate (%), Waktu Eksekusi (maksimal 180 detik), dan target Skor SUS (> 68). |
| Feasibility | 2 | Eksperimen cukup layak dijalankan, namun tantangan teknis berada pada proses rekrutmen. Mencari 6 partisipan purposive dan 30 responden aktif SeaBank (non-IT, usia 18-40 tahun) di wilayah Kebumen yang bersedia meluangkan waktu untuk uji lab terkontrol dalam batas waktu 8 minggu membutuhkan usaha ekstra. |
| Rigor | 2 | Ketelitian metode sudah cukup baik dengan adanya penetapan Control Variable (Wi-Fi & HP konstan) dan uji T-Test. Namun, skalanya masih terbatas karena pengujian Task Scenario hanya menggunakan 6 sampel dan belum menggunakan alat rekam jejak kognitif tingkat lanjut (seperti eye-tracking). |

**Skor total:** 10 / 12

**Apakah proposal siap untuk fase eksekusi?** [X] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Mengidentifikasi masalah awal (Problem Statement) dan menentukan sistem yang diuji (WS-02 & WS-06). Alasannya karena objek penelitian (SeaBank) sangat dekat dengan keseharian, dan bukti empiris berupa keluhan pengguna terkait kebingungan navigasi fitur mutasi dan deposito sangat mudah ditemukan di forum maupun ulasan aplikasi.
**Bagian tersulit:** Merumuskan Research Gap (WS-03) dan menurunkannya menjadi Desain Eksperimen yang ketat (WS-07). Sangat sulit untuk memastikan bahwa metrik yang dipilih (Task Success Rate dan batas waktu 180 detik) benar-benar bisa mengukur beban kognitif secara objektif. Selain itu, merangkai State of the Art agar riset ini terlihat berbeda dari 15 jurnal sebelumnya (yang mayoritas hanya memakai kuesioner tanpa observasi langsung) membutuhkan pemikiran analitis yang sangat menguras tenaga.
**Yang akan dilakukan berbeda:**
> Jika mengulang dari awal, saya akan mengumpulkan, membaca, dan membedah jurnal referensi secara lebih mendalam sejak WS-01, lalu langsung memasukkannya ke dalam tabel Concept-Centric Matrix. Pada pengerjaan kemarin, pencarian literatur dan penentuan baseline (seperti skor SUS > 68) baru dilakukan belakangan, sehingga saya harus beberapa kali membongkar ulang rumusan Gap dan Hipotesis agar logika proposalnya tidak saling bertabrakan. Selain itu, saya mungkin akan melakukan pilot test (uji coba kecil) skenario tugas ke satu orang teman terlebih dahulu sebelum mengunci desain eksperimen.