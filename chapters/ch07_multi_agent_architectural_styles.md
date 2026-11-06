# Bab 7: Multi-Agent Systems & Arsitektur Tim AI

## Gaya Arsitektur Multi-Agent di Bidang Finansial

### 1. Hierarchical Supervisor (Atasan - Bawahan)
Satu agen supervisor menerima order pengguna, lalu mendelegasikan sub-analisis kepada agen bawahan (Agen Analisis Laporan Keuangan, Agen Analisis Teknikal, Agen Makro). Hasil kerja dibaca kembali oleh supervisor untuk finalisasi.

### 2. Peer-to-Peer Collaborative (Kolaboratif Sejajar)
Agen bekerja secara estafet dalam alur pipa data (*pipeline*). Output Agen Ekstraksi Data langsung menjadi input Agen Valuasi.

### 3. Adversarial Arena (Debat Oposisi)
Dua agen dirancang saling menyerang logika satu sama lain. Pola ini terbukti paling efektif untuk keputusan alokasi modal besar di hedge fund kuantitatif.
