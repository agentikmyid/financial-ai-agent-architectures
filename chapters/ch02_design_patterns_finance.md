# Bab 2: Design Patterns untuk Agen Finansial

## 1. Empat Pola Desain Kapabilitas Inti
Agen finansial tingkat produksi dibangun di atas 4 pilar arsitektur:

### A. Tool Use (Function Calling)
Agen tidak pernah menghitung angka sendiri. Agen mengubah intensi menjadi pemanggilan API terstruktur (JSON schema) ke penyedia data pasar, database SQL, atau kalkulator quant.

### B. Memory (Short-Term & Long-Term)
- **Working Memory (In-Context):** Riwayat percakapan dan status portfolio saat ini.
- **Episodic Memory (Vector DB):** Riwayat keputusan investasi masa lalu dan catatan performa kuartal sebelumnya.
- **Semantic Memory:** Pengetahuan aturan kepatuhan regulasi (OJK, SEC, KYC).

### C. Planning & Decomposition
Memecah pertanyaan kompleks: *"Apakah saham X layak dibeli?"* menjadi sub-tugas:
1. Ambil laporan laba rugi 3 tahun terakhir.
2. Hitung Compound Annual Growth Rate (CAGR) pendapatan.
3. Cek tren margin laba bersih.
4. Bandingkan valuasi P/E dengan rata-rata industri.

### D. Multi-Turn Reflection
Agen memeriksa draf outputnya sendiri sebelum dieksekusi atau ditampilkan ke pengguna.
