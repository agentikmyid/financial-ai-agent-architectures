# 📖 Financial AI Agents Glossary

Kamus istilah penting quantitative finance, LLM, dan arsitektur agen otonom.

| Istilah | Definisi Teknis | Relevansi dalam Agen |
| :--- | :--- | :--- |
| **Adversarial Debate** | Pola arsitektur di mana 2 agen (Bull vs Bear) saling mendebat tesis investasi sebelum keputusan diambil. | Mengeliminasi bias konfirmasi model AI tunggal. |
| **Agentic RAG** | Sistem Retrieval-Augmented Generation yang mampu mengevaluasi dan mengoreksi hasil pencarian secara dinamis. | Mencegah halusinasi saat membaca tabel 10-K yang rumit. |
| **Alpha Factor** | Sinyal matematika atau metrik yang memprediksi pergerakan harga aset di masa depan. | Output yang dihitung oleh Quantitative Agent. |
| **Confirmation Bias** | Kecenderungan model AI untuk membenarkan pertanyaan atau asumsi awal pengguna. | Bahaya nomor satu dalam analisis saham dengan AI. |
| **EV/EBITDA** | Enterprise Value dibagi EBITDA; valuasi yang netral terhadap utang dan struktur permodalan. | Metrik fundamental utama dalam tool valuation. |
| **Function Calling** | Fitur LLM untuk menghasilkan struktur JSON yang memanggil fungsi/tool eksternal. | Jembatan antara LLM dan database bursa/kripto. |
| **Human-in-the-Loop (HITL)** | Titik persetujuan manual manusia sebelum tindakan berisiko tinggi dieksekusi. | Wajib untuk eksekusi order modal di atas batas limit tertentu. |
| **Idempotency** | Properti operasi di mana eksekusi berulang menghasilkan efek yang sama tanpa duplikasi transaksi. | Mencegah order beli saham tereksekusi 2 kali saat koneksi timeout. |
| **LangGraph** | Framework orkestrasi agen berbasis grafik keadaan (*state graph*) dan siklus deterministik. | Standar arsitektur agen finansial institusi. |
| **Piotroski F-Score** | Skor 0–9 yang mengukur kekuatan finansial emiten berdasarkan 9 kriteria akuntansi. | Filter screening saham otomatis pada Fundamental Agent. |
| **ReAct** | Paradigma penalaran yang menggabungkan Reasoning (pemikiran) dan Acting (tindakan pemanggilan tool). | Pola kerja default agen interaktif. |
| **ROIC** | Return on Invested Capital; persentase efisiensi alokasi modal perusahaan untuk mencetak laba. | Metrik kualitas emiten terbaik menurut Warren Buffett. |
| **Self-Refine** | Loop di mana agen mengkritisi dan memperbaiki draf jawabannya sendiri secara mandiri. | Meningkatkan kualitas laporan riset saham. |
| **Tree of Thoughts (ToT)** | Penjelajahan beberapa cabang skenario masa depan secara bersamaan. | Simulasi skenario ekonomi (Bull/Base/Bear). |
