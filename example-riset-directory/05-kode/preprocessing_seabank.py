import pandas as pd
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

print("Mulai proses pembersihan 50 data...")

# 1. Membaca data mentah
df = pd.read_csv('seabank_reviews_raw.csv')

# Menghapus baris yang kosong (Missing Values) & Duplikat
df.dropna(subset=['teks_ulasan'], inplace=True)
df.drop_duplicates(subset=['teks_ulasan'], keep='first', inplace=True)

# 2. Menyiapkan alat dari Sastrawi
stopword_remover = StopWordRemoverFactory().create_stop_word_remover()
stemmer = StemmerFactory().create_stemmer()

# 3. Membuat fungsi pembersihan lengkap
def bersihkan_teks(teks):
    # a. Case Folding: Mengubah ke huruf kecil
    teks = teks.lower()
    
    # b. Text Cleansing: Menghapus angka, tanda baca, dan karakter aneh (Regex)
    teks = re.sub(r'[^a-z\s]', ' ', teks) # Hanya menyisakan huruf a-z dan spasi
    teks = re.sub(r'\s+', ' ', teks).strip() # Menghapus spasi ganda
    
    # c. Stopword Removal: Menghapus kata hubung (dan, di, ke, yang, dll)
    teks = stopword_remover.remove(teks)
    
    # d. Stemming: Mengubah kata berimbuhan jadi kata dasar (contoh: "membantu" -> "bantu")
    teks = stemmer.stem(teks)
    
    return teks

# 4. Menerapkan fungsi ke dalam kolom teks_ulasan
print("Sedang membersihkan teks dan mengubah ke kata dasar (Ini butuh waktu beberapa detik)...")
df['teks_bersih'] = df['teks_ulasan'].apply(bersihkan_teks)

# 5. Menyimpan hasil ke file baru
file_name = 'seabank_reviews_clean.csv'
# Kita simpan kolom rating dan teks_bersih saja
df[['rating', 'teks_bersih']].to_csv(file_name, index=False)

print(f"Sukses! Data bersih telah disimpan di {file_name}")
print("\nContoh Hasil Perbandingan:")
print("Sebelum :", df['teks_ulasan'].iloc[0])
print("Sesudah :", df['teks_bersih'].iloc[0])