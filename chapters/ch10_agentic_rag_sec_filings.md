# Bab 10: Agentic RAG untuk Laporan Keuangan (SEC Filings / 10-K)

## 1. Mengapa RAG Konvensional Gagal pada Tabel Finansial?
RAG biasa memotong teks berdasarkan jumlah karakter (*fixed chunking*). Hal ini merusak tabel neraca: angka laba terpisah dari judul barisnya, menghasilkan halusinasi fatal.

## 2. Solusi Agentic RAG
1. **Structure-Aware Chunking:** Memisahkan paragraf narasi naratif dan struktur tabel HTML/Markdown secara utuh.
2. **Metadata Enrichment:** Menempelkan tag tahun fiskal, nama emiten, dan jenis laporan di setiap potongan data.
3. **Corrective RAG (CRAG):** Agen mengevaluasi apakah dokumen yang diambil relevan sebelum mulai menjawab. Jika dokumen kurang lengkap, agen otomatis melakukan query ulang dengan kata kunci berbeda.

Lihat script demo: [`examples/06_agentic_rag_sec_tables.py`](../examples/06_agentic_rag_sec_tables.py)
