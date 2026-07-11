from google_play_scraper import reviews, Sort
import pandas as pd

# 1. Tentukan ID Aplikasi SeaBank
app_id = 'id.co.bankbkemobile.digitalbank'

print("Mulai mengambil data dari Google Play Store...")

# 2. Proses Scraping (Mengambil 35 data untuk tahap belajar)
result, continuation_token = reviews(
    app_id,
    lang='id',           # Bahasa ulasan (Indonesia)
    country='id',        # Negara asal (Indonesia)
    sort=Sort.NEWEST,    # Mengambil ulasan dari yang paling baru
    count=50             # Jumlah data yang diambil
)

# 3. Mengubah hasil scraping menjadi format Tabel (DataFrame)
df = pd.DataFrame(result)

# 4. Memilih kolom yang penting saja
df = df[['content', 'score', 'at']]

# Mengganti nama kolom agar lebih rapi
df.rename(columns={'content': 'teks_ulasan', 'score': 'rating', 'at': 'tanggal'}, inplace=True)

# 5. Menyimpan ke dalam file CSV
file_name = 'seabank_reviews_raw.csv'
df.to_csv(file_name, index=False)

print(f"Selesai! {len(df)} ulasan berhasil disimpan ke dalam file {file_name}")