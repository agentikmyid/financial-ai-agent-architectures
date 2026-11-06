# Bab 5: Deep Search – Riset Saham Level Analis Wall Street

## 1. Mengapa Naive Search Gagal di Keuangan?
Pencarian web biasa menghasilkan artikel clickbait, ringkasan AI daur ulang, atau sentimen ritel yang bising. 

## 2. Arsitektur Deep Search Agent
Agen Deep Search bekerja secara iteratif:
1. **Query Expansion:** Mengubah pertanyaan pengguna menjadi 5 variasi query teknis (misal: "risiko konsentrasi pelanggan", "gugatan hukum tertunda").
2. **Source Whitelisting:** Memfilter hasil hanya dari sumber primer (SEC EDGAR, keterbukaan informasi bursa, filings resmi, siaran pers earnings).
3. **Cross-Verification:** Setiap klaim laba wajib diverifikasi minimal oleh 2 sumber independen.
4. **Synthesis with Citations:** Menghasilkan dokumen memo investasi dengan kutipan halaman dokumen asli.

Lihat contoh kode: [`examples/03_deep_search_researcher.py`](../examples/03_deep_search_researcher.py)
