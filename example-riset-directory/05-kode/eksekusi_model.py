import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import train_test_split
import time

print("=== MEMULAI EKSEKUSI MODEL MACHINE LEARNING (TANPA GENSIM) ===")
start_time = time.time()

# 1. BACA DATA BERSIH
df = pd.read_csv('seabank_reviews_clean.csv')
df.dropna(subset=['teks_bersih'], inplace=True)

# Bikin Label Sentimen (Bintang 1-3 = Negatif, Bintang 4-5 = Positif)
df['label'] = df['rating'].apply(lambda x: 'negatif' if x <= 3 else 'positif')

# ==========================================
# FASE 1: K-NN SENTIMENT FILTERING
# ==========================================
print("\n--- FASE 1: FILTERING K-NN ---")
vectorizer_tfidf = TfidfVectorizer()
X = vectorizer_tfidf.fit_transform(df['teks_bersih'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
akurasi_knn = knn.score(X_test, y_test)
print(f"Akurasi K-NN membedakan sentimen: {akurasi_knn * 100:.2f}%")

# ==========================================
# FASE 2: LDA TOPIC MODELING (VIA SCIKIT-LEARN)
# ==========================================
print("\n--- FASE 2: LDA TOPIC MODELING ---")
ulasan_negatif = df[df['label'] == 'negatif']['teks_bersih']

# LDA di scikit-learn lebih suka pakai CountVectorizer dibanding TF-IDF
vectorizer_tf = CountVectorizer()
tf = vectorizer_tf.fit_transform(ulasan_negatif)

# Jalankan algoritma LDA (Mencari 2 Topik Utama)
lda_model = LatentDirichletAllocation(n_components=2, random_state=42)
lda_model.fit(tf)

# Tampilkan kata kunci
print("Topik Keluhan yang Ditemukan oleh Mesin:")
fitur_kata = vectorizer_tf.get_feature_names_out()
for topic_idx, topic in enumerate(lda_model.components_):
    top_kata_idx = topic.argsort()[:-5 - 1:-1]
    top_kata = [fitur_kata[i] for i in top_kata_idx]
    print(f"Topik {topic_idx + 1}: {', '.join(top_kata)}")

end_time = time.time()
waktu_eksekusi = end_time - start_time

print(f"\n=== HASIL AKHIR UNTUK WS-14 ===")
print(f"Waktu Eksekusi : {waktu_eksekusi:.2f} detik")
print("(Catatan: Koherensi murni pada sklearn dievaluasi secara kualitatif dari kemiripan kata di atas)")