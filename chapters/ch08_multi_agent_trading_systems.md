# Bab 8: Multi-Agent Trading Systems (Investment Committee & Adversarial Debate)

## 1. Struktur Komite Investasi AI
Meniru operasional hedge fund papan atas:

```
                  ┌───────────────────────────────┐
                  │    Incoming Market Signals    │
                  └───────────────┬───────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ Fundamental Agent│    │ Quantitative Agent│   │ Sentiment Agent  │
│ (Financial Ratio)│    │(Volatility/Regime│    │(News/Social Flow)│
└────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                  ┌──────────────┴──────────────┐
                  ▼                             ▼
       ┌─────────────────────┐       ┌─────────────────────┐
       │   Bullish Advocate  │       │  Bearish Risk Guard │
       │ (Upside Projection) │       │ (Downside Scenarios)│
       └──────────┬──────────┘       └──────────┬──────────┘
                  │                             │
                  └──────────────┬──────────────┘
                                 ▼
                  ┌─────────────────────────────┐
                  │   Chief Investment Officer  │
                  │   (Final Sizing & Decision) │
                  └─────────────────────────────┘
```

## 2. Peran Agen:
- **Bull Advocate:** Menemukan katalis ekspansi pendapatan, adopsi produk baru, dan peluang valuasi.
- **Bear Risk Guard:** Mengaudit risiko utang jatuh tempo, ancaman regulasi, dan potensi jebakan likuiditas.
- **Chief Investment Officer (CIO):** Memberikan vonis alokasi kapital rasional:
  - *Strong Buy (Full Allocation)*
  - *Speculative Long (Small Size with Tight Stop-Loss)*
  - *Neutral / Cash*
  - *Short / Hedge*

Lihat script demo: [`examples/05_multi_agent_trading_committee.py`](../examples/05_multi_agent_trading_committee.py)
