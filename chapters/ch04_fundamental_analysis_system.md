# Bab 4: Membangun Fundamental Analysis Agent

## 1. Anatomi Tiga Laporan Keuangan
Agen analisis fundamental wajib memiliki parser khusus untuk tiga laporan utama:
1. **Income Statement (Laba Rugi):** Memeriksa kualitas pertumbuhan top-line (revenue) dan bottom-line (net income).
2. **Balance Sheet (Neraca):** Mengukur kesehatan struktur modal, kas bersih, dan rasio utang terhadap ekuitas (*Debt-to-Equity*).
3. **Cash Flow Statement (Arus Kas):** Membedakan laba akuntansi semu dengan *Free Cash Flow* (FCF) riil.

## 2. Golden Ratios yang Wajib Dihitung Tool:
- **ROIC (Return on Invested Capital):** Efisiensi pengalokasian modal manajemen.
- **EV/EBITDA:** Valuasi perusahaan netral terhadap struktur permodalan.
- **Current Ratio & Quick Ratio:** Ketahanan likuiditas jangka pendek.
- **Piotroski F-Score (0-9):** Skor komprehensif kesehatan fundamental emiten.

Lihat implementasi kodingan: [`examples/02_fundamental_analysis_agent.py`](../examples/02_fundamental_analysis_agent.py)
