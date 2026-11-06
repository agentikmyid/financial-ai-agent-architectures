# Bab 1: Fondasi LLM & Agen AI di Industri Keuangan

## 1. Evolusi: Dari LLM Pasif ke Autonomous Agent
Model bahasa besar tradisional (LLM) bekerja dengan pola satu arah (*stateless*): menerima input teks dan menghasilkan probabilitas teks berikutnya. Dalam industri finansial, pendekatan ini memiliki 4 keterbatasan fatal:
1. **Knowledge Cutoff:** Model tidak mengetahui harga saham atau berita detik ini.
2. **Lack of Domain Depth:** Model umum gagal menginterpretasikan catatan kaki (*footnotes*) audit 10-K.
3. **No Execution Capability:** Model tidak bisa mengeksekusi order beli/jual atau memverifikasi margin portofolio.
4. **Hallucination on Numbers:** LLM rentan mengarang kalkulasi rasio matematika.

**Definisi Agen AI Finansial:**
Sistem terprogram yang memanfaatkan penalaran (*reasoning*) LLM sebagai otak pusat, dilengkapi memori, kemampuan memanggil alat luar (*tool calling*), dan loop evaluasi mandiri untuk mencapai tujuan finansial secara otonom.

---

## 2. Taksonomi Model AI di Keuangan
- **General Frontier Models (Claude 3.5 Sonnet, GPT-4o):** Terbaik untuk penalaran deduktif, perdebatan thesis investasi, dan tool use multi-turn.
- **Reasoning Models (DeepSeek R1, OpenAI o1):** Unggul dalam pembuktian formula matematika, kalkulasi opsi Black-Scholes, dan validasi data kuantitatif.
- **Specialized Financial Models (FinGPT, BloombergGPT):** Model open-source atau proprietary yang telah di-fine-tune dengan miliaran token dokumen keuangan.

---

## 3. Implementasi: Perbedaan Non-Agentic vs Agentic Call
Lihat file kode perbandingan: [`examples/01_non_agentic_vs_agentic.py`](../examples/01_non_agentic_vs_agentic.py)
