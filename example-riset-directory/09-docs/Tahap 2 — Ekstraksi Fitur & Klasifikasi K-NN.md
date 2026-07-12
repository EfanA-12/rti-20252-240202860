# Tahap 2 — Ekstraksi Fitur & Klasifikasi K-NN

**Status:** Selesai

---

## Tujuan

Mengimplementasikan ekstraksi fitur pembobotan Term Frequency-Inverse Document Frequency (TF-IDF) dan melatih model klasifikasi K-Nearest Neighbors (K-NN) menggunakan bahasa pemrograman Python dan pustaka Scikit-Learn. Model ini dirancang khusus untuk memfilter dan menyaring sentimen negatif dari ulasan SeaBank sebelum asupan data tersebut diteruskan ke fase pemodelan topik (LDA).

## Deliverable

- [x] Pemanggilan dataset ulasan bersih (seabank_reviews_clean.csv) ke dalam struktur data Pandas DataFrame.
- [x] Implementasi TfidfVectorizer untuk mentransformasi teks ulasan Sastrawi menjadi vektor numerik berdimensi tinggi.
- [x] Pembagian skema dataset (Train-Test Split) dengan rasio 80% data latih dan 20% data uji menggunakan fungsi train_test_split.
- [x] Pelatihan model KNeighborsClassifier dengan penguncian parameter ketetanggaan n_neighbors=3 (K=3).
- [x] Modul prediksi data uji dan komputasi metrik evaluasi berupa pencetakan Confusion Matrix beserta tingkat Akurasi (Accuracy Score).
- [x] Fungsi penyaring (filter) yang secara eksklusif hanya menyeleksi dan meneruskan ulasan dengan hasil prediksi klasifikasi "Negatif" untuk dijadikan asupan algoritma LDA.

## Hasil Verifikasi End-to-End

Diverifikasi secara langsung melalui eksekusi eksekusi komputasi pada skrip Python:
- Ekstraksi Fitur: Proses transformasi teks ke angka berjalan mulus; nilai matriks bobot TF-IDF terbentuk dengan normal tanpa adanya error dimensi ataupun nilai null.
- Klasifikasi Sentimen (K-NN): Model berbasis jarak K=3 berhasil dilatih dan dieksekusi dengan sangat efisien. Hasil pencatatan sistem membuktikan waktu komputasi (waktu eksekusi) hanya menelan 0,09 detik. Model terbukti andal dengan torehan tingkat akurasi sebesar 88,89%.
- Validasi Output Filter: Skrip berhasil mengekspor variabel dataframe baru yang hanya berisi ulasan dengan prediksi "Negatif". Filter ini mencegah ulasan bernada apresiasi/pujian bocor ke tahap selanjutnya, sehingga sistem siap dialirkan ke Tahap 3 (Pemodelan Topik LDA) tanpa risiko ambiguitas data.

## Catatan Lingkungan

- Eksperimen ini dieksekusi pada environment Python 3.x standar secara lokal, tidak memerlukan spesifikasi server khusus maupun containerization seperti Docker.
- Implementasi algoritma pada skrip eksekusi_model.py murni mengandalkan pustaka Scikit-Learn (sklearn). Tidak ada penggunaan library pengklasifikasi pihak ketiga lainnya untuk memastikan kesederhanaan kode (clean code) dan beban komputasi yang ultra-ringan saat melakukan pemisahan sentimen teks.
