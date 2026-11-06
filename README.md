# 🏛️ Financial AI Agent Architectures & Quantitative Blueprints

[![Website](https://img.shields.io/badge/Gateway-agentik.my.id-0070f3?style=flat-square&logo=cloudflare&logoColor=white)](https://agentik.my.id)
[![Payment](https://img.shields.io/badge/TopUp-QRIS%20Instant-E31E24?style=flat-square)](https://agentik.my.id)
[![Models](https://img.shields.io/badge/Models-Claude%204.6%20%7C%20Gemini%203.8%20%7C%20GPT--OSS-00A67E?style=flat-square)](https://agentik.my.id)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

Cetak biru arsitektur lengkap (**12 Bab Komprehensif**), pola desain (*design patterns*), diagram sistem, dan implementasi kode Python untuk membangun **Autonomous Financial AI Agents**, **Multi-Agent Trading Committee**, dan **Agentic RAG Keuangan**.

Dirancang sebagai kerangka kerja referensi teknis institusional oleh tim rekayasa sistem Agentik, memadukan metodologi quantitative finance, arsitektur multi-agent otonom (Adversarial Debate & Committee), dan protokol mitigasi risiko trading berkecepatan tinggi.

Didukung penuh oleh **[Agentik.my.id](https://agentik.my.id)** (AI API Gateway lokal pertama di Indonesia dengan pembayaran instan QRIS).

---

## 📚 Kurikulum Lengkap & Kode Contoh per Bab

Setiap bab memiliki dokumen panduan arsitektur dan **1 script Python mandiri** yang siap dieksekusi langsung menggunakan API Agentik:

| Bab | Dokumen Panduan Arsitektur | Fokus Rekayasa AI | Kode Praktis Mandiri |
| :--- | :--- | :--- | :--- |
| **Bab 01** | [Fondasi LLM & Agen AI di Keuangan](chapters/ch01_what_are_ai_agents.md) | Mengatasi Knowledge Cutoff & Halusinasi Angka | [`examples/01_non_agentic_vs_agentic.py`](examples/01_non_agentic_vs_agentic.py) |
| **Bab 02** | [Design Patterns Agen Finansial](chapters/ch02_design_patterns_finance.md) | Tool Use, Memory Buffer, & State Ingestion | [`examples/02_design_patterns_memory_tools.py`](examples/02_design_patterns_memory_tools.py) |
| **Bab 03** | [Komparasi Framework Agen Finansial](chapters/ch03_agent_frameworks_comparison.md) | StateGraph, Siklus Deterministik, & Routing | [`examples/03_framework_orchestration_stategraph.py`](examples/03_framework_orchestration_stategraph.py) |
| **Bab 04** | [Fundamental Analysis Agent](chapters/ch04_fundamental_analysis_system.md) | Audit Otomatis Neraca, Laba Rugi, & Rasio FCF | [`examples/04_fundamental_analysis_screener.py`](examples/04_fundamental_analysis_screener.py) |
| **Bab 05** | [Deep Search – Riset Saham Wall Street](chapters/ch05_deep_search_analyst_research.md) | Query Expansion & Verifikasi Sumber Primer | [`examples/05_deep_search_analyst_research.py`](examples/05_deep_search_analyst_research.py) |
| **Bab 06** | [Paradigma Penalaran (Reasoning Paradigms)](chapters/ch06_reasoning_paradigms_self_refine.md) | Self-Refine Reflection Loop & Tree of Thoughts | [`examples/06_self_refine_reflection_loop.py`](examples/06_self_refine_reflection_loop.py) |
| **Bab 07** | [Multi-Agent Systems & Arsitektur Tim](chapters/ch07_multi_agent_architectural_styles.md) | Hierarchical Supervisor vs Peer-to-Peer Networks | [`examples/07_hierarchical_multi_agent_supervisor.py`](examples/07_hierarchical_multi_agent_supervisor.py) |
| **Bab 08** | [Multi-Agent Trading System (Debat Bull vs Bear)](chapters/ch08_multi_agent_trading_systems.md) | Komite Investasi AI & Putusan Alokasi CIO | [`examples/08_adversarial_trading_debate.py`](examples/08_adversarial_trading_debate.py) |
| **Bab 09** | [Workflow Asuransi & Penyelesaian Klaim](chapters/ch09_insurance_and_settlement_agents.md) | Triage Klaim Medis, Deteksi Fraud, & Audit Trail | [`examples/09_insurance_claim_triage.py`](examples/09_insurance_claim_triage.py) |
| **Bab 10** | [Agentic RAG untuk Laporan Keuangan](chapters/ch10_agentic_rag_sec_filings.md) | Structure-Aware Table Chunking & Corrective RAG | [`examples/10_agentic_rag_table_parser.py`](examples/10_agentic_rag_table_parser.py) |
| **Bab 11** | [Evaluasi & Guardrails Agen (Kasus KYC)](chapters/ch11_evaluating_financial_agents_kyc.md) | Faithfulness Metrics & Hallucination Guardrails | [`examples/11_kyc_compliance_guardrails.py`](examples/11_kyc_compliance_guardrails.py) |
| **Bab 12** | [Menjalankan Agen di Lingkungan Produksi](chapters/ch12_production_harness_and_safety.md) | Idempotency Keys, Failover Fallback, & Timeouts | [`examples/12_production_resilience_harness.py`](examples/12_production_resilience_harness.py) |

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

Semua script Python dalam direktori `examples/` siap dijalankan menggunakan OpenAI SDK resmi tanpa membutuhkan kartu kredit internasional.

### 1. Pasang Dependensi
```bash
pip install -r requirements.txt
```

### 2. Atur Variabel Lingkungan
Salin file `.env.example` menjadi `.env`:
```bash
cp .env.example .env
```
Lalu masukkan API Key dari dashboard **[Agentik.my.id](https://agentik.my.id)**.

### 3. Jalankan Contoh Skrip (Contoh: Bab 08 - Adversarial Debate)
```bash
python examples/08_adversarial_trading_debate.py
```

*Top-up saldo instan mulai Rp10.000 via QRIS (GoPay, DANA, OVO, BCA, Livin) langsung di [Agentik.my.id](https://agentik.my.id).*

---

## 📖 Kamus & Panduan Tambahan
- **[Kamus Istilah Finansial & Agen AI (Glossary)](glossary.md):** 15+ istilah teknis quant & AI agent.
- **[Design Patterns Lengkap (patterns.md)](patterns.md):** Panduan implementasi ReAct, Self-Refine, dan Tool Calling.
- **[Matriks Keputusan (cheatsheet.md)](cheatsheet.md):** Kapan menggunakan Single-Agent vs Multi-Agent.

---
*Dikelola oleh tim rekayasa sistem [Agentik.my.id](https://agentik.my.id) untuk riset AI otonom & quant trading Indonesia.*
