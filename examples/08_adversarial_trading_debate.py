import os
from openai import OpenAI

# Bab 08: Multi-Agent Trading System (Debat Dialektis Bull vs Bear + CIO Sizing)
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def run_adversarial_trading_debate(asset, context_data):
    print(f"=== ADVERSARIAL DEBATE COMMITTEE: {asset} ===
")

    # 1. Bull Advocate (Claude Sonnet)
    print("1. Bull Advocate merumuskan katalis upside...")
    bull_thesis = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "system", "content": "Anda adalah Wall Street Bullish Growth Fund Manager. Berikan argumen kenaikan harga terkuat."},
            {"role": "user", "content": f"Aset: {asset}. Data: {context_data}"}
        ],
        temperature=0.3
    ).choices[0].message.content

    # 2. Bear Risk Guard (Claude Sonnet / Opus)
    print("2. Bear Risk Guard membongkar risiko & potensi likuidasi...")
    bear_critique = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "system", "content": "Anda adalah Short-Seller & Risk Manager Skeptis. Serang setiap celah tesis Bull."},
            {"role": "user", "content": f"Tesis Bull:
{bull_thesis}"}
        ],
        temperature=0.3
    ).choices[0].message.content

    # 3. Chief Investment Officer (Gemini Flash High / Sonnet)
    print("3. Chief Investment Officer (CIO) memutuskan vonis alokasi modal...")
    verdict = client.chat.completions.create(
        model="gemini-3.8-flash-high",
        messages=[
            {"role": "system", "content": "Anda adalah Chief Investment Officer (CIO). Putuskan bobot portofolio (0%-100%), level stop-loss, dan rasio risk-to-reward."},
            {"role": "user", "content": f"ARGUMEN BULL:
{bull_thesis}

ARGUMEN BEAR:
{bear_critique}"}
        ]
    ).choices[0].message.content

    return {"bull": bull_thesis, "bear": bear_critique, "cio_verdict": verdict}

if __name__ == "__main__":
    print("=== BAB 08: MULTI-AGENT ADVERSARIAL TRADING COMMITTEE ===")
    news = "Volume transaksi on-chain memecahkan rekor all-time high, namun terjadi lonjakan biaya gas fee dan kemacetan mempool."
    hasil = run_adversarial_trading_debate("ETH (Ethereum)", news)
    print("
--- KEPUTUSAN FINAL CIO ---")
    print(hasil["cio_verdict"])
