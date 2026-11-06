# 🏛️ Financial AI Agent Architectures & Quantitative Blueprints

[![Website](https://img.shields.io/badge/Gateway-agentik.my.id-0070f3?style=flat-square&logo=cloudflare&logoColor=white)](https://agentik.my.id)
[![Payment](https://img.shields.io/badge/TopUp-QRIS%20Instant-E31E24?style=flat-square)](https://agentik.my.id)
[![Models](https://img.shields.io/badge/Models-Claude%204.6%20%7C%20Gemini%203.8%20%7C%20GPT--OSS-00A67E?style=flat-square)](https://agentik.my.id)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

Cetak biru arsitektur lengkap (**12 Bab Komprehensif**), pola desain (*design patterns*), diagram sistem, dan implementasi kode Python untuk membangun **Autonomous Financial AI Agents**, **Multi-Agent Trading Committee**, dan **Agentic RAG Keuangan**.

Dirancang sebagai kerangka kerja referensi teknis institusional oleh tim rekayasa sistem Agentik, memadukan metodologi quantitative finance, arsitektur multi-agent otonom (Adversarial Debate & Committee), dan protokol mitigasi risiko trading berkecepatan tinggi.

Didukung penuh oleh **[Agentik.my.id](https://agentik.my.id)** (AI API Gateway lokal pertama di Indonesia dengan pembayaran instan QRIS).

---

## 📚 Kurikulum Lengkap (12 Bab Kajian)

| Bab | Judul Panduan | Fokus Rekayasa AI | Kode Praktis |
| :--- | :--- | :--- | :--- |
| **Bab 01** | [Fondasi LLM & Agen AI di Keuangan](chapters/ch01_what_are_ai_agents.md) | Mengatasi Knowledge Cutoff & Halusinasi Angka | [`examples/01_non_agentic_vs_agentic.py`](examples/01_non_agentic_vs_agentic.py) |
| **Bab 02** | [Design Patterns Agen Finansial](chapters/ch02_design_patterns_finance.md) | Tool Use, Memory (Vector DB), & Planning | [`patterns.md`](patterns.md) |
| **Bab 03** | [Komparasi Framework Agen Finansial](chapters/ch03_agent_frameworks_comparison.md) | LangGraph vs AutoGen vs CrewAI vs LlamaIndex | [`cheatsheet.md`](cheatsheet.md) |
| **Bab 04** | [Fundamental Analysis Agent](chapters/ch04_fundamental_analysis_system.md) | Audit Otomatis Neraca, Laba Rugi, & Rasio FCF | [`examples/02_fundamental_analysis_agent.py`](examples/02_fundamental_analysis_agent.py) |
| **Bab 05** | [Deep Search – Riset Saham Wall Street](chapters/ch05_deep_search_analyst_research.md) | Query Expansion & Verifikasi Sumber Primer | [`examples/03_deep_search_researcher.py`](examples/03_deep_search_researcher.py) |
| **Bab 06** | [Paradigma Penalaran (Reasoning Paradigms)](chapters/ch06_reasoning_paradigms_self_refine.md) | Self-Refine Reflection Loop & Tree of Thoughts | [`examples/04_self_refine_investment_thesis.py`](examples/04_self_refine_investment_thesis.py) |
| **Bab 07** | [Multi-Agent Systems & Arsitektur Tim](chapters/ch07_multi_agent_architectural_styles.md) | Hierarchical Supervisor vs Peer-to-Peer Networks | [`patterns.md`](patterns.md) |
| **Bab 08** | [Multi-Agent Trading System (Debat Bull vs Bear)](chapters/ch08_multi_agent_trading_systems.md) | Komite Investasi AI & Putusan Alokasi CIO | [`examples/05_multi_agent_trading_committee.py`](examples/05_multi_agent_trading_committee.py) |
| **Bab 09** | [Workflow Asuransi & Penyelesaian Klaim](chapters/ch09_insurance_and_settlement_agents.md) | Triage Klaim Medis, Deteksi Fraud, & Audit Trail | [`chapters/ch09_insurance_and_settlement_agents.md`](chapters/ch09_insurance_and_settlement_agents.md) |
| **Bab 10** | [Agentic RAG untuk Laporan Keuangan](chapters/ch10_agentic_rag_sec_filings.md) | Structure-Aware Table Chunking & Corrective RAG | [`chapters/ch10_agentic_rag_sec_filings.md`](chapters/ch10_agentic_rag_sec_filings.md) |
| **Bab 11** | [Evaluasi & Guardrails Agen (Kasus KYC)](chapters/ch11_evaluating_financial_agents_kyc.md) | Faithfulness Metrics & Hallucination Guardrails | [`chapters/ch11_evaluating_financial_agents_kyc.md`](chapters/ch11_evaluating_financial_agents_kyc.md) |
| **Bab 12** | [Menjalankan Agen di Lingkungan Produksi](chapters/ch12_production_harness_and_safety.md) | Idempotency Keys, Failover Fallback, & Timeouts | [`examples/08_production_harness_resilience.py`](examples/08_production_harness_resilience.py) |

---

## 🏛️ Desain Arsitektur: Multi-Agent Investment Committee

```
                         ┌─────────────────────────────────┐
                         │   Real-Time Data Feed & News    │
                         └────────────────┬────────────────┘
                                          │
                 ┌────────────────────────┼────────────────────────┐
                 ▼                        ▼                        ▼
       ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
       │Fundamental Analyst│    │Quantitative Agent│     │ Sentiment Analyst│
       │ (10-K / Ratios)  │     │(Regime/Volatility│     │(News/Social Flow)│
       └─────────┬────────┘     └────────┬─────────┘     └────────┬─────────┘
                 │                       │                        │
                 └───────────────────────┼────────────────────────┘
                                         │
                         ┌───────────────┴───────────────┐
                         ▼                               ▼
              ┌─────────────────────┐         ┌─────────────────────┐
              │   Bullish Advocate  │         │  Bearish Risk Guard │
              │ (Growth & Catalysts)│         │(Downside & Failures)│
              └──────────┬──────────┘         └──────────┬──────────┘
                         │                               │
                         └───────────────┬───────────────┘
                                         ▼
                         ┌───────────────────────────────┐
                         │    Chief Investment Officer   │
                         │   (Final Capital Sizing / HITL)│
                         └───────────────────────────────┘
```

---

## ⚡ Eksekusi Cepat dengan API Agentik.my.id (QRIS)

Semua script Python dalam repositori ini siap dijalankan menggunakan OpenAI SDK resmi tanpa membutuhkan kartu kredit internasional.

### 1. Pasang Library
```bash
pip install openai pandas
```

### 2. Jalankan Script Trading Debate
```bash
python examples/05_multi_agent_trading_committee.py
```

*Dapatkan API Key dan isi saldo instan mulai Rp10.000 via QRIS (GoPay, DANA, OVO, m-Banking) di [Agentik.my.id](https://agentik.my.id).*

---

## 📖 Kamus & Panduan Tambahan
- **[Kamus Istilah Finansial & Agen AI (Glossary)](glossary.md):** 15+ istilah teknis quant & AI agent.
- **[Design Patterns Lengkap (patterns.md)](patterns.md):** Panduan implementasi ReAct, Self-Refine, dan Tool Calling.
- **[Matriks Keputusan (cheatsheet.md)](cheatsheet.md):** Kapan menggunakan Single-Agent vs Multi-Agent.

---
*Dikelola oleh tim [Agentik.my.id](https://agentik.my.id) untuk riset rekayasa AI & quant trading Indonesia.*
