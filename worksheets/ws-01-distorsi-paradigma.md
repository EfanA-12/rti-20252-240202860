# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Efan Aryanto Adli
Tanggal          : 4 Juli 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Bagaimana data ulasan (sentimen publik) diambil? Apakah terjadi sampling bias karena hanya pengguna yang sangat puas atau sangat marah yang memberikan ulasan?  
   - Data yang dibutuhkan untuk verifikasi: Dataset ulasan mentah dari Google Play Store, tanggal pengambilan data (snapshot), dan metode klasifikasi sentimen yang digunakan untuk memastikan validitasnya.

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [X] Mixed (Campuran)
   - Alasan: Riset ini menggabungkan pendekatan Positivis (pengujian usability terkontrol untuk metrik objektif seperti skor SUS) dengan Interpretivis (analisis sentimen ulasan publik untuk memahami konteks keluhan pengguna secara mendalam).

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Ulasan di Google Play Store mencerminkan opini seluruh basis pengguna SeaBank secara akurat.
   - Sumber bias potensial: Sampling bias pada data sekunder (ulasan publik) dan Hawthorne effect pada data primer (pengguna merasa diawasi saat task scenario).
   - Langkah mitigasi: Melakukan triangulasi data (membandingkan temuan dari kedua sumber) untuk memastikan konsistensi hasil, serta menggunakan kriteria inklusi partisipan yang ketat.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Skor mentah SUS dari partisipan dan hasil klasifikasi sentimen dari ulasan Google Play Store, meskipun hasilnya tidak sesuai dengan hipotesis awal.
   - Batasan yang diakui sejak awal: Keterbatasan akses terhadap log internal perusahaan SeaBank dan ketergantungan pada data publik yang mungkin mengandung noise (cacian atau komentar tidak relevan).

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Evaluasi Usability Aplikasi Mobile Banking BCA dengan Menggunakan Usability Testing dan System Usability Scale (Studi Kasus: BCA Kota Singaraja).
> Penulis (Tahun): Dewi, A. M. K., Wijoyo, S. H., & Perdanakusuma, A. R. (2022).
> Sumber/Link DOI: https://j-ptiik.ub.ac.id/index.php/j-ptiik/article/view/11640/5168

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan data evaluasi task scenario (penggunaan aplikasi) dari 6 partisipan dan kuesioner SUS dari 20 responden nasabah BCA Kota Singaraja. | Sampling Bias: Jumlah sampel sangat kecil (hanya 6 orang untuk uji task dan 20 orang untuk SUS) dan hanya terbatas pada demografi nasabah BCA di Kota Singaraja. Apakah ini bisa merepresentasikan jutaan pengguna BCA Mobile di seluruh Indonesia? |
| Data → Processing | Menghitung Learnability menggunakan rumus Success Rate, di mana tugas yang selesai sebagian (P) tetap diberi bobot nilai setengah (0.5). | Construct Validity: Pemberian bobot 0.5 untuk partial success bisa mendistorsi realita; di dunia nyata perbankan, transfer yang hanya "setengah berhasil" mungkin sama fatalnya dengan gagal total. |
| Processing → Analysis | Menganalisis error rate yang didapat (0.41 untuk kelompok 1 dan 0.16 untuk kelompok 2) dan membandingkannya dengan nilai rata-rata kesalahan Sauro (0.7). Mengonversi skor SUS menjadi metrik kualitatif | Penggunaan benchmark (acuan) yang kurang pas. Peneliti menggunakan batas toleransi kesalahan aplikasi umum (Sauro, 2012) untuk mengevaluasi aplikasi finansial. |
| Analysis → Inference | Menarik kesimpulan (inference) bahwa karena skor error rate (0.41 dan 0.16) berada di bawah angka 0.7, maka tingkat error pada aplikasi BCA Mobile "masih tergolong kecil". | Construct Validity: Menyimpulkan bahwa error "tergolong kecil" dalam konteks perbankan bisa sangat menyesatkan. Melakukan 4 kesalahan dari 10 langkah di aplikasi mobile banking berisiko fatal (salah transfer/nominal), sehingga threshold (ambang batas) kesuksesannya tidak bisa disamakan dengan aplikasi biasa. |
| Inference → Knowledge | Menghasilkan pengetahuan/solusi baru berupa 4 rekomendasi perubahan desain UI (misal: menggabungkan menu daftar transfer dan menu transfer menjadi 1 halaman). Peneliti menetapkan ini sebagai solusi mutlak perbaikan usability. | Overgeneralization & Lack of Validation: Peneliti menjadikan keluhan 6 orang sebagai landasan untuk merombak UI. Padahal, mengubah struktur menu secara drastis bisa menghancurkan mental model (kebiasaan) jutaan nasabah lama BCA yang sudah hafal di luar kepala. Selain itu, desain baru tersebut diusulkan tanpa diuji kembali (A/B testing) untuk membuktikan klaim bahwa desain itu "lebih baik". |

**Distorsi paling besar di tahap:** Reality → Data (Pengambilan Sampel).

**Dua distorsi spesifik yang teridentifikasi:**
1. External Validity (Generalisasi): Dataset terlalu kecil (6-20 orang)  untuk menarik kesimpulan general tentang aplikasi skala nasional.
2. Confounding Variable: Partisipan uji task scenario dibagi menjadi pengguna aplikasi mobile banking lain dan pengguna aktif BCA Mobile. Pengalaman masa lalu pengguna dengan UI bank lain bisa sangat memengaruhi metrik error dan efficiency, bukan murni karena desain BCA Mobile-nya saja.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti wajib melaporkan hasil apa adanya. Menghapus data outlier secara sengaja hanya untuk mendapatkan nilai "signifikan" (p-value < 0.05) adalah bentuk manipulasi data yang disebut cherry-picking atau p-hacking. |
| Transparansi | Peneliti harus terbuka mengenai adanya outlier. Jika outlier tersebut memang terjadi karena kesalahan teknis (misal: koneksi internet terputus saat task scenario), maka data tersebut boleh dibuang, namun alasan pembuangannya wajib didokumentasikan secara transparan dalam laporan. |
| Peer review | Reviewer dan komunitas ilmiah akan menganggap riset tidak kredibel jika data diubah untuk memanipulasi hasil. Jika manipulasi ini terdeteksi, hal ini dapat berujung pada penarikan (retraction) publikasi riset. |

**Keputusan akhir dan justifikasi:**
> Keputusan: Peneliti tidak boleh menghapus outlier secara diam-diam. Langkah yang benar adalah menyajikan hasil analisis dengan data utuh. Jika peneliti ingin menampilkan hasil tanpa outlier, ia wajib menyertakan kedua versi analisis (dengan dan tanpa outlier) di dalam proposal atau jurnal sebagai bahan perbandingan bagi pembaca.
Justifikasi: Tujuan utama riset bukan untuk mencari hasil yang "bagus" atau "signifikan" sesuai keinginan peneliti, melainkan mencari kebenaran empiris. Dalam riset usability SeaBank, data outlier (seperti pengguna yang sangat lambat karena bingung) justru merupakan temuan berharga yang mengungkap friction points nyata, bukan sekadar data sampah yang harus dihilangkan. Menghilangkan data tersebut justru akan menyesatkan pengembang aplikasi dalam melakukan perbaikan desain.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Analisis Validasi Usability Aplikasi SeaBank: Studi Komparatif Antara Eksperimen Task Scenario dan Sentimen Publik Google Play Store.

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 4 | 4 |
| Jenis data yang dikumpulkan | Metrik numerik (skor SUS, Success Rate, Time) | Data kualitatif (teks ulasan/sentimen pengguna) | Artefak (Rekomendasi redesign antarmuka) |
| Limitasi paradigma | Angka tidak menjelaskan alasan di balik kesulitan pengguna | Sangat subjektif dan sulit untuk divalidasi secara statistik | Fokus bisa bergeser ke teknis daripada evaluasi ilmiah |

**Paradigma yang dipilih:** Mixed Methods (Campuran)
**Alasan:** Pendekatan Positivis dominan digunakan karena riset ini mengukur tingkat usability secara objektif melalui eksperimen terkontrol (skor SUS dan Task Success Rate) untuk mendapatkan bukti empiris yang terukur.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Dulu, saya menganggap angka dalam riset sebagai kebenaran mutlak tanpa mempertanyakan proses di baliknya. Kini, saya sadar bahwa setiap riset rentan terhadap distorsi di setiap tahap transformasinya. Saat membaca riset atau mengevaluasi usability, saya kini lebih kritis mempertanyakan metode pengambilan sampel dan potensi sampling bias. Dalam riset saya sendiri (Analisis Validasi Usability SeaBank), saya menyadari bahwa data rating Google Play Store memiliki bias signifikan, sehingga saya wajib melakukan triangulasi data agar kesimpulan yang dihasilkan lebih valid dan tidak terjebak dalam generalisasi yang sempit.