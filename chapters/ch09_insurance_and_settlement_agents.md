# Bab 9: Workflow Otomasi Asuransi & Klaim Finansial

## 1. Perbedaan Asuransi vs Trading
Jika trading berfokus pada kecepatan dan optimasi probabilitas keuntungan, workflow asuransi berfokus pada:
- **Kepatuhan Polis (Policy Compliance):** Verifikasi klausul pengecualian.
- **Deteksi Fraud (Kecurangan):** Analisis anomali klaim ganda atau manipulasi kuitansi.
- **Audit Trail:** Dokumentasi hukum yang tidak dapat diubah atas keputusan persetujuan klaim.

## 2. Agen Triage Klaim Multi-Tahap:
1. **Document Ingestion Agent:** Ekstraksi OCR kuitansi medis dan laporan kerugian.
2. **Policy Validator Agent:** Pengecekan aktifnya masa berlaku dan limit pertanggungan.
3. **Fraud Detection Agent:** Komparasi klaim terhadap database klaim historis.
4. **Adjudication Agent:** Memberikan rekomendasi: Approve, Reject, atau Escalate to Human Adjuster.
