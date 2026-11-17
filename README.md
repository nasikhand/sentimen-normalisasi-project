# Klasifikasi Sentimen Ulasan Produk Tokopedia

Final Project Machine Learning B081 · Kelompok 2

**Judul:** Pengaruh Normalisasi Kata Tidak Baku terhadap Kinerja Naive Bayes dan K-Nearest Neighbor pada Klasifikasi Sentimen Ulasan Produk Tokopedia Berbasis TF-IDF

## Struktur folder

```
data/raw/            dataset asli PRDECT-ID
data/processed/      data bersih hasil preprocessing (teks_A, teks_B, label)
notebooks/           notebook berurutan (01_, 02_, ...)
resources/           kamus normalisasi, stopword, dan sumber aslinya
figures/             grafik untuk artikel
src/                 fungsi preprocessing yang dipakai ulang
```

## Cara menjalankan

```
pip install -r requirements.txt
jupyter notebook
```

Buka `notebooks/01_EDA_dan_Preprocessing.ipynb`, lalu jalankan semua sel (Run All). Seed acak yang dipakai adalah 42.

## Skenario

| Skenario | Preprocessing |
|---|---|
| A | case folding → cleaning → tokenisasi → stopword removal |
| B | case folding → cleaning → tokenisasi → **normalisasi** → stopword removal |

## Sumber data dan resource

- Dataset: R. Sutoyo dkk., "PRDECT-ID: Indonesian product reviews dataset for emotions classification tasks," *Data in Brief*, vol. 44, 2022. Lisensi CC BY 4.0. https://data.mendeley.com/datasets/574v66hf2v/1
- Kamus: N. A. Salsabila dkk., "Colloquial Indonesian Lexicon," IALP 2018. https://github.com/nasalsabila/kamus-alay
- Stopword: daftar stopword bahasa Indonesia dari NLTK, dengan kata negasi dan kata penilai dikeluarkan dari daftar.
