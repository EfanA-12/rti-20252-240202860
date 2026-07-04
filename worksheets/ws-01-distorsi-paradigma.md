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
   - Pendekatan: [X] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed (Campuran)
   - Alasan: Riset ini menggunakan pendekatan murni Positivis karena bertujuan mengukur dan mengevaluasi kinerja dua algoritma Machine Learning (K-NN untuk sentimen dan LDA untuk pemodelan topik) secara objektif dan terukur menggunakan metrik statistik performa (Accuracy, F1-Score, Coherence Score) pada data sekunder ulasan Play Store.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Bahwa teks ulasan di Google Play Store benar-benar ditulis oleh manusia, bukan bot atau buzzer yang dimobilisasi untuk memanipulasi rating aplikasi.
   - Sumber bias potensial: Sampling bias dari algoritma scraping, serta Selection bias di mana pengguna yang kecewa lebih termotivasi menulis ulasan panjang (mengandung banyak kata kunci untuk LDA) dibandingkan pengguna yang puas.
   - Langkah mitigasi: Menerapkan tahap text preprocessing yang sangat ketat (menghapus duplikasi teks spam, bot, dan rating bintang 5 yang tidak memiliki isi teks yang bermakna) sebelum data dimasukkan ke dalam model latih K-NN.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Rasio akurasi akhir dari K-NN dan metrik Coherence Score dari LDA, meskipun hasilnya ternyata menunjukkan bahwa model kesulitan memilah topik (hasil tidak signifikan).
   - Batasan yang diakui sejak awal: Data sekunder yang bersifat unstructured dan penuh dengan slang, singkatan, serta bahasa sarkasme khas netizen Indonesia yang sangat rentan menyebabkan misklasifikasi pada mesin.

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Evaluasi ANALISIS SENTIMEN KEPUASAN PENGGUNA BANK SAQU PADA   ULASAN GOOGLE PLAY STORE MENGGUNAKAN ALGORITMA K-NN DAN LEXICON BASED
> Penulis (Tahun): Dwi Setyabudi1, Sri Mulyati2*, Purwanto3 
> Sumber/Link DOI: https://journal.budiluhur.ac.id/bit/article/view/3948/1759

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan 500 ulasan dari Google Play Store pada rentang waktu Januari - Maret. | Sampling Bias: 500 ulasan mungkin terlalu kecil untuk melatih model ML yang stabil, dan rentang waktu yang terlalu sempit mungkin tidak menangkap update aplikasi yang menyebabkan bug. |
| Data → Processing | Melakukan stemming dan menghapus semua kata hubung (stopword). | Construct Validity: Menghapus stopword tanpa filter khusus bisa menghilangkan makna kalimat. Misalnya, penghapusan kata "tidak" dapat mengubah sentimen kalimat "Saya tidak suka aplikasi ini" menjadi "Saya suka aplikasi ini" yang menyesatkan K-NN. |
| Processing → Analysis | Menggunakan algoritma K-NN dengan nilai K=3 sebagai nilai mutlak (default) tanpa melakukan iterasi optimasi parameter. | Analysis Bias: Pemilihan K=3 yang arbiter tanpa justifikasi empiris bisa membuat model terlalu sensitif terhadap noise di ulasan yang tidak terstruktur. |
| Analysis → Inference | Menyimpulkan bahwa K-NN memiliki akurasi 82% dan sangat layak digunakan untuk analisis sentimen. | Overstatement: Klaim "sangat layak" terlalu berlebihan jika akurasi 82% tersebut didapat dari data uji (test set) yang sangat kecil atau data yang sudah di-cherry-pick. |
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

**Topik riset:** Analisis Sentimen dan Ekstraksi Topik Keluhan Usability pada Aplikasi SeaBank Menggunakan Algoritma K-NN dan Latent Dirichlet Allocation (LDA).

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 5 | 1 | 2 |
| Jenis data yang dikumpulkan | Metrik Machine Learning (Accuracy, F1-Score, Coherence) dan persentase probabilitas topik. | (Kosong - tidak digunakan) | (Kosong - bukan fokus utama) |
| Limitasi paradigma | AngMesin (LDA) mungkin menghasilkan kelompok kata (topic) yang koheren secara matematis, namun tetap membutuhkan interpretasi manual manusia untuk memberi "label" yang masuk akal bagi developer. | - | - |

**Paradigma yang dipilih:** Positivis murni.
**Alasan:** Riset ini berfokus pada pembangunan eksperimen terukur untuk mengevaluasi kinerja algoritma (classifier K-NN dan topic modeling LDA) menggunakan data kuantitatif dan metrik uji performa Machine Learning, bukan pada interaksi sosial atau penafsiran makna wawancara.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Dulu saya menerima metrik akurasi Machine Learning sebagai kebenaran mutlak. Kini, melalui Research Trust Model, saya sadar tingginya risiko distorsi di tahap pemrosesan data (seperti cherry-picking). Untuk riset SeaBank (K-NN & LDA), besarnya bias ulasan Play Store menuntut saya melakukan preprocessing yang sangat ketat dan pengujian parameter objektif, agar kesimpulan yang ditarik benar-benar valid dan bukan ilusi algoritma semata.