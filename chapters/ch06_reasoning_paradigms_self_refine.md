# Bab 6: Paradigma Penalaran (Reasoning Paradigms) untuk Agen Finansial

## 1. Self-Refine (Reflection Loop)
Agen finansial yang baik adalah agen yang skeptis terhadap dirinya sendiri.
Siklus Self-Refine terdiri dari 3 tahap:
1. **Generate:** Menghasilkan draf tesis investasi awal.
2. **Critique:** Agen evaluator memeriksa draf tersebut berdasarkan kriteria ketat:
   - Apakah ada klaim tanpa data angka?
   - Apakah risiko penurunan (*downside*) sudah dihitung?
   - Apakah valuasi memperhitungkan skenario resesi?
3. **Refine:** Menulis ulang analisis dengan menambal semua kelemahan yang ditemukan.

## 2. Tree of Thoughts (ToT) untuk Skenario Portofolio
Alih-alih memilih 1 jalur analisis, agen mengeksplorasi cabang skenario:
- Skenario Bull (Suku bunga turun, margin naik).
- Skenario Base (Kondisi ekonomi stabil).
- Skenario Bear (Disrupsi kompetitor atau inflasi melonjak).

Lihat script demo: [`examples/04_self_refine_investment_thesis.py`](../examples/04_self_refine_investment_thesis.py)
