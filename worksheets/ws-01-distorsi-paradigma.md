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
Tanggal          : 17 Mei 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Bagaimana tahap Reality → Data dilakukan? Apakah ada sampling bias saat pengumpulan data ujinya?
   - Data yang dibutuhkan untuk verifikasi: Karakteristik dataset yang digunakan, metode pengujian (misal: jumlah sampel responden), dan baseline yang digunakan sebagai pembanding.

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [ ] Design Science  [X] Mixed (Campuran)
   - Alasan: Topik riset UI/UX utamanya berfokus pada pengujian kuantitatif (waktu, rasio keberhasilan, skor SUS) yang bersifat Positivis. Namun, pendekatan ini harus dikombinasikan dengan interpretasi keluhan pengguna (Interpretivis) untuk dapat menghasilkan rancangan rekomendasi desain baru (Design Science).

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Klaim akurasi/kepuasan tinggi pada suatu aplikasi berlaku secara universal untuk semua profil pengguna di segala kondisi.
   - Sumber bias potensial: Sampling Bias (sampel terlalu homogen) dan Hawthorne Effect (partisipan berbohong/berperilaku berbeda karena merasa sedang diamati).
   - Langkah mitigasi: Menerapkan kriteria inklusi sampel yang ketat (beragam usia/profesi) dan memberikan briefing netral agar partisipan tidak merasa sedang diuji kecerdasannya.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Rekaman durasi waktu (stopwatch), jumlah klik yang salah (error/defect), serta angka kuesioner dari partisipan, meskipun hasilnya buruk atau tidak sesuai harapan (negative result).
   - Batasan yang diakui sejak awal: Keterbatasan ukuran sampel dan pengkondisian lingkungan uji yang mungkin tidak 100% merefleksikan kepanikan pengguna saat bertransaksi di dunia nyata.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Evaluasi Usability Aplikasi Mobile Banking BCA dengan menggunakan Usability Testing dan System Usability Scale
> Penulis (Tahun): Ayu Made Krisna Dewi, Satrio Hadi Wijoyo, Andi Reza Perdanakusuma (2022)
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
| Kejujuran ilmiah | Menghapus data outlier hanya demi mendapatkan angka yang bagus adalah bentuk manipulasi data (cherry-picking). Peneliti harus jujur melaporkan hasil apa adanya. Mendapatkan negative result (hipotesis tidak terbukti) tetaplah sebuah kontribusi ilmu pengetahuan yang valid. |
| Transparansi | Jika peneliti memiliki alasan kuat bahwa outlier tersebut adalah "data sampah" (misal: akibat sensor rusak atau human error saat input), ia harus transparan. Cara terbaik adalah melaporkan kedua hasil analisis (dengan dan tanpa outlier) dan menjelaskan alasan metodologis mengapa outlier tersebut dibuang. |
| Peer review | Menyembunyikan fakta bahwa ada outlier yang dihapus akan membodohi reviewer. Jika manipulasi ini terdeteksi oleh reviewer atau peneliti lain yang mencoba mereplikasi eksperimen, reputasi peneliti akan hancur dan paper berisiko ditarik mundur (retracted). |

**Keputusan akhir dan justifikasi:**
> Keputusan: Peneliti tidak boleh menghapus outlier secara diam-diam.Tetapi harus mempublikasikan hasil dengan data utuh yang menunjukkan hasil tidak signifikan. Jika ingin menampilkan versi tanpa outlier, wajib melampirkan kedua versi hasil (dengan dan tanpa outlier) secara eksplisit di dalam jurnal.
Justifikasi: Tujuan utama riset (research) berbeda dengan rekayasa (engineering). Dalam riset, kegagalan membuktikan hipotesis bukanlah sebuah kegagalan yang harus disembunyikan, melainkan kebenaran (realita) yang harus diungkapkan. Menghilangkan data demi "signifikansi" akan menciptakan pengetahuan palsu (distorted knowledge) yang merugikan peneliti selanjutnya.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Evaluasi Usability Sistem Perbankan Digital.

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 — Sangat cocok karena riset ini mengukur fenomena menggunakan metrik kuantitatif (learnability, efficiency, error rate, skor SUS). | 3 — Cukup sesuai. Paper ini juga melakukan wawancara kualitatif untuk memahami perasaan dan pengalaman kebingungan pengguna (misal: fitur mutasi sulit ditemukan). | 3 — Cukup sesuai. Peneliti tidak membangun sistem dari nol, tetapi mereka menghasilkan artefak berupa prototipe rekomendasi perbaikan UI di akhir studi (misal: menggabungkan menu transfer). |
| Jenis data yang dikumpulkan | Skor SUS numerik (76.38) , waktu pengerjaan (detik), dan rasio kesalahan (0.41 & 0.16). | Transkrip wawancara mengenai opini dan keluhan nasabah. | Desain mockup antarmuka baru sebagai solusi. |
| Limitasi paradigma | Terlalu kaku pada angka. Metrik/angka tidak bisa menjelaskan akar masalah secara mendalam (misal: mengapa pengguna bingung pada menu tertentu). Rawan distorsi jika sampel tidak representatif. | Subjektif & sulit digeneralisasi. Sangat bergantung pada penafsiran peneliti. Keluhan 6 orang tidak bisa diukur signifikansinya secara statistik untuk mewakili semua pengguna. | Fokus bisa melenceng ke engineering. Peneliti sering kali hanya sibuk mendesain UI baru (artefak), tapi lupa menguji kembali (memfalsifikasi) apakah desain baru tersebut benar-benar lebih baik dari yang lama secara empiris. |

**Paradigma yang dipilih:** Campuran (Mixed Methods) dengan dominasi Positivis.
**Alasan:** Penelitian ini utamanya bertumpu pada pengujian terukur yang menghasilkan data statistik mutlak (seperti skor kepuasan SUS dan waktu penyelesaian dalam goals/sec) untuk mengambil kesimpulan objektif. Namun, ia meminjam sedikit aspek interpretivis (wawancara) dan design science (rekomendasi desain) untuk melengkapi konteks di balik angka-angka tersebut.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> sebelumnya saya jarang mempertanyakan klaim tersebut. Saat membaca klaim bahwa sebuah model Neural Network atau optimasi dengan Algoritma Genetika mencapai akurasi 95% ke atas, saya cenderung langsung percaya dan menganggap metode itu pasti superior, tanpa memikirkan bagaimana data pengujiannya diproses.
Setelah memahami rantai distorsi, cara pandang saya berubah. Sekarang, saat membaca paper, pertanyaan pertama yang akan saya ajukan adalah: "Bagaimana tahap Reality → Data dilakukan?" Saya akan mencari tahu apakah ada sampling bias—misalnya, apakah model tersebut diuji menggunakan data yang terlalu seragam, atau apakah peneliti diam-diam membuang data outlier yang membuat akurasinya turun (cherry-picking). Saya juga akan mempertanyakan apakah hasil 95% tersebut valid untuk digeneralisasi (External Validity) jika diterapkan di lingkungan nyata.