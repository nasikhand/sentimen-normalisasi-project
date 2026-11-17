"""Fungsi preprocessing untuk klasifikasi sentimen ulasan PRDECT-ID.

Skenario A  : case folding -> cleaning -> tokenisasi -> stopword removal
Skenario B  : case folding -> cleaning -> tokenisasi -> NORMALISASI -> stopword removal

Satu-satunya perbedaan antara kedua skenario adalah langkah normalisasi.
"""
import re
from pathlib import Path

import pandas as pd

RE_URL = re.compile(r"https?://\S+|www\.\S+")
RE_NON_HURUF = re.compile(r"[^a-z\s]")
RE_HURUF_BERULANG = re.compile(r"([a-z])\1{2,}")  # 3 huruf sama atau lebih berturut-turut
RE_SPASI = re.compile(r"\s+")


def case_folding(teks: str) -> str:
    return teks.lower()


def cleaning(teks: str) -> str:
    """Hapus URL, tanda tanya sisa emoji yang rusak ("??"), karakter rusak,
    tanda baca, dan angka, lalu pendekkan huruf yang diulang 3 kali atau lebih
    ("bagusss" -> "bagus", "mantaaap" -> "mantap")."""
    teks = RE_URL.sub(" ", teks)
    teks = teks.replace("�", " ")
    teks = RE_NON_HURUF.sub(" ", teks)  # termasuk "?" sisa emoji, tanda baca, angka
    teks = RE_HURUF_BERULANG.sub(r"\1", teks)
    return RE_SPASI.sub(" ", teks).strip()


def tokenisasi(teks: str) -> list[str]:
    return teks.split()


def muat_kamus(path) -> dict[str, str]:
    df = pd.read_csv(path)
    return dict(zip(df["slang"], df["formal"]))


def normalisasi(token: list[str], kamus: dict[str, str]) -> list[str]:
    """Ganti kata tidak baku dengan bentuk bakunya. Bentuk baku bisa lebih dari
    satu kata (misalnya "gpp" -> "tidak apa-apa"), jadi hasilnya dipecah lagi."""
    hasil = []
    for t in token:
        hasil.extend(kamus.get(t, t).split())
    return hasil


def muat_stopwords(path) -> set[str]:
    return set(Path(path).read_text(encoding="utf-8").split())


def hapus_stopwords(token: list[str], stopwords: set[str]) -> list[str]:
    return [t for t in token if t not in stopwords]


def preprocess(teks: str, stopwords: set[str], kamus: dict[str, str] | None = None) -> str:
    """kamus=None -> Skenario A, kamus diisi -> Skenario B."""
    token = tokenisasi(cleaning(case_folding(teks)))
    if kamus is not None:
        token = normalisasi(token, kamus)
    token = hapus_stopwords(token, stopwords)
    return " ".join(token)
