# Bab 11: Evaluasi & Guardrails Agen Finansial (Studi Kasus KYC)

## Tiga Lapisan Evaluasi Agen Finansial
1. **Input Guardrails:** Mencegah prompt injection, penyusupan instruksi jailbreak, dan memastikan data input valid.
2. **Reasoning Verification:** Memastikan setiap langkah deduksi logis didukung oleh data fakta, bukan asumsi.
3. **Output Guardrails:** 
   - *Hallucination Check:* Tidak ada angka rasio yang melenceng dari data mentah.
   - *Disclaimer Compliance:* Peringatan risiko finansial otomatis disematkan sesuai regulasi.

Lihat script demo: [`examples/07_kyc_compliance_agent.py`](../examples/07_kyc_compliance_agent.py)
