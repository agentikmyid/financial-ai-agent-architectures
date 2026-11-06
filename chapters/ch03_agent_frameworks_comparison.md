# Bab 3: Komparasi Framework Agen Finansial

## Evaluasi Framework di Lingkungan Finansial Institusi

| Framework | Kelebihan Utama | Kelemahan di Finansial | Tingkat Kematangan |
| :--- | :--- | :--- | :--- |
| **LangGraph** | Kontrol alur berbasis StateGraph, siklus deterministik, dukungan Human-in-the-Loop | Kurva belajar lebih curam | ⭐⭐⭐⭐⭐ (Standar Industri) |
| **CrewAI** | Mudah membuat tim berbasis peran (*Role-playing*) | Alur eksekusi kurang deterministik untuk transaksi modal | ⭐⭐⭐⭐ |
| **AutoGen** | Kemampuan percakapan multi-agen yang sangat luwes | Rawan terjadi loop obrolan tanpa henti (*infinite conversation*) | ⭐⭐⭐⭐ |
| **LlamaIndex Workflows** | Integrasi mendalam dengan dokumen finansial dan data terindeks | Kurang fokus pada orkestrasi tindakan trading | ⭐⭐⭐⭐⭐ (Khusus RAG) |

**Prinsip Desain:**
Untuk sistem trading dan eksekusi modal riil, pilih framework yang mendukung **State Machine Deterministik** (seperti LangGraph) agar keputusan dapat diaudit secara hukum (*auditability*).
