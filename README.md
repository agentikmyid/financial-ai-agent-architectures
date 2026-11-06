# 🏛️ Financial AI Agent Architectures & Trading Blueprints

[![Website](https://img.shields.io/badge/Gateway-agentik.my.id-0070f3?style=flat-square&logo=cloudflare&logoColor=white)](https://agentik.my.id)
[![Payment](https://img.shields.io/badge/TopUp-QRIS%20Instant-E31E24?style=flat-square)](https://agentik.my.id)
[![Models](https://img.shields.io/badge/Models-Claude%203.5%20%7C%20GPT--4o%20%7C%20DeepSeek-00A67E?style=flat-square)](https://agentik.my.id)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

Kumpulan cetak biru (*production-grade blueprints*), pola desain (*design patterns*), dan implementasi kode Python untuk membangun sistem **Autonomous Financial AI Agents**, **Multi-Agent Trading Committee**, dan **Agentic RAG Keuangan**.

Diekstrak dan diadaptasi dari riset mutakhir financial engineering global untuk komunitas developer, quant researcher, dan AI builder Indonesia.

Didukung penuh oleh **[Agentik.my.id](https://agentik.my.id)** (AI API Gateway lokal dengan pembayaran instan QRIS).

---

## 📌 Daftar Arsitektur & Bab

| Bab / Pola | Topik Utama | Kasus Penggunaan Riil | File Kode |
| :--- | :--- | :--- | :--- |
| **01. Fundamental Agent** | Tool Calling, Rasio Keuangan, 10-K Analysis | Audit otomatis laporan keuangan & valuasi | [`examples/01_fundamental_agent.py`](examples/01_fundamental_agent.py) |
| **02. Adversarial Debate** | Multi-Agent Bull vs Bear + CIO Verdict | Mencegah bias konfirmasi sebelum eksekusi trading | [`examples/02_adversarial_trading_debate.py`](examples/02_adversarial_trading_debate.py) |
| **03. Deep Search RAG** | Iterative Retrieval & Query Self-Correction | Riset pasar saham/kripto level analis Wall Street | [`examples/03_deep_search_financial_rag.py`](examples/03_deep_search_financial_rag.py) |
| **04. Design Patterns** | Memory, ReAct Loop, Hierarchical Supervisors | Dokumen panduan arsitektur sistem | [`patterns.md`](patterns.md) |
| **05. Decision Matrix** | Tabel keputusan kapan pakai single vs multi-agent | Cheatsheet evaluasi arsitektur | [`cheatsheet.md`](cheatsheet.md) |

---

## 🧠 Mental Model: Mengapa Multi-Agent di Bidang Trading?

### 1. Masalah Single Agent (Confirmation Bias)
Satu model LLM yang diminta menganalisis saham cenderung mengalami *hallucination* atau membenarkan hipotesis awal pengguna (*yes-man syndrome*).

### 2. Solusi: Arsitektur Komite Investasi (Investment Committee)
Dalam hedge fund kelas institusi, keputusan investasi tidak pernah diambil satu orang. Arsitektur multi-agent membagi tugas ke dalam 4 lensa informasi:
1. **Fundamental Lens:** Neraca, laba-rugi, arus kas, margin, dan rasio solvabilitas.
2. **Quantitative Lens:** Volatilitas, rezim likuiditas, order flow, dan tren momentum.
3. **Macro Lens:** Siklus suku bunga, tren komoditas, inflasi, dan rantai pasok global.
4. **Sentiment / Alternative Lens:** Berita breaking news, sentimen sosial, dan aktivitas insider.

```
       ┌───────────────────────┐
       │   Market / News Data  │
       └───────────┬───────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐ ┌─────────────────┐
│   Bull Analyst  │ │   Bear Analyst  │
│  (Upside Alpha) │ │ (Risk & Downsides│
└────────┬────────┘ └────────┬────────┘
         │                   │
         └─────────┬─────────┘
                   ▼
       ┌───────────────────────┐
       │ Chief Investment Off. │
       │ (Sizing & Allocation) │
       └───────────────────────┘
```

---

## ⚡ Quickstart: Menjalankan Agent dengan Saldo QRIS

Seluruh kode dalam repositori ini menggunakan format standar OpenAI SDK yang telah diarahkan ke endpoint proxy berkecepatan tinggi **[Agentik.my.id](https://agentik.my.id)**.

### 1. Install Dependensi
```bash
pip install openai pandas
```

### 2. Eksekusi Script Contoh
```bash
python examples/02_adversarial_trading_debate.py
```

*Catatan: Pastikan Anda telah memasukkan API Key dari dashboard [Agentik.my.id](https://agentik.my.id) (Bisa top-up mulai Rp10.000 via GoPay, DANA, OVO, atau m-Banking).*

---

## 🤝 Kontribusi & Dukungan
Repositori ini dikelola secara terbuka untuk memajukan riset kuantitatif dan rekayasa AI di Indonesia.

- **Website Resmi:** [https://agentik.my.id](https://agentik.my.id)
- **Repositori Terkait:** [Cara Pakai Claude di Cursor Tanpa Kartu Kredit](https://github.com/agentikmyid/cara-pakai-claude-cursor-tanpa-kartu-kredit)
