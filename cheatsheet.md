# 📋 Cheatsheet & Decision Matrices

Panduan memilih arsitektur AI agent yang tepat sesuai kebutuhan sistem keuangan Anda.

---

### Matrix 1: Kapan Menggunakan Single Agent vs Multi-Agent?

| Kriteria | Single Agent (ReAct) | Multi-Agent System |
| :--- | :--- | :--- |
| **Kompleksitas Tugas** | Rendah - Menengah (1 domain data) | Sangat Tinggi (Multi-perspektif) |
| **Kebutuhan Verifikasi** | Standar | Kritis (Keputusan Modal/Trading) |
| **Biaya Token** | Hemat (1x prompt cycle) | Lebih Tinggi (3-5x panggilan LLM) |
| **Latensi** | 2 - 5 detik | 10 - 25 detik |
| **Contoh Kasus** | Menjawab rasio P/E emiten | Komite Investasi Alokasi Portofolio |

---

### Matrix 2: Pemilihan Model LLM di Agentik API

| Tugas Finansial | Rekomendasi Model | Alasan |
| :--- | :--- | :--- |
| **Reasoning / Logic Debat** | `claude-3-5-sonnet-20241022` | Penalaran deduktif paling tajam, zero fluff |
| **Sintesis Cepat / Routing** | `gpt-4o` | Respon cepat, multimodal visual grafik saham |
| **Konteks Dokumen Panjang (10-K)** | `gemini-1.5-pro` | Kapasitas context window hingga jutaan token |
| **Kalkulasi Matematis Murah** | `deepseek-chat` / `deepseek-reasoner` | Efisiensi biaya komputasi kuantitatif |
