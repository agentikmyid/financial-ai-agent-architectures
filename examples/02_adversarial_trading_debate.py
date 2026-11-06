import os
from openai import OpenAI

# Menggunakan endpoint terpadu Agentik.my.id (Bayar via QRIS)
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def run_adversarial_debate(asset_name, catalyst_news):
    print(f"=== MEMULAI SIMULASI DEBAT MULTI-AGENT UNTUK: {asset_name} ===\n")

    # 1. Bull Analyst Agent
    print("1. Bull Analyst sedang menyusun tesis pertumbuhan...")
    bull_resp = client.chat.completions.create(
        model="claude-3-5-sonnet-20241022",
        messages=[
            {"role": "system", "content": "Anda adalah Wall Street Bull Analyst. Bangun tesis kenaikan harga yang paling kuat dan agresif."},
            {"role": "user", "content": f"Aset: {asset_name}. Berita/Katalis: {catalyst_news}"}
        ]
    )
    bull_thesis = bull_resp.choices[0].message.content

    # 2. Bear Risk Agent
    print("2. Bear Risk Agent sedang menyerang tesis Bull...")
    bear_resp = client.chat.completions.create(
        model="claude-3-5-sonnet-20241022",
        messages=[
            {"role": "system", "content": "Anda adalah Short-Seller & Risk Manager Skeptis. Serang dan bongkar setiap kelemahan tesis Bull."},
            {"role": "user", "content": f"Aset: {asset_name}. Tesis Bull yang harus diserang:\n{bull_thesis}"}
        ]
    )
    bear_critique = bear_resp.choices[0].message.content

    # 3. Chief Investment Officer (CIO) Verdict
    print("3. Chief Investment Officer sedang mengadili kedua belah pihak...")
    cio_resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Anda adalah Chief Investment Officer (CIO) yang objektif dan rasional. Sintesis kedua argumen menjadi keputusan alokasi modal nyata (Alokasi: 0 - 100%, Stop-loss, dan Target)."},
            {"role": "user", "content": f"Tesis Bull:\n{bull_thesis}\n\nKritik Bear:\n{bear_critique}"}
        ]
    )
    verdict = cio_resp.choices[0].message.content

    return {
        "bull": bull_thesis,
        "bear": bear_critique,
        "verdict": verdict
    }

if __name__ == "__main__":
    result = run_adversarial_debate(
        asset_name="SOL (Solana)",
        catalyst_news="Volume DEX mencapai all-time high, ekspansi likuiditas Meteora, namun terjadi peningkatan kemacetan transaksi jaringan."
    )
    print("\n================ HASIL KEPUTUSAN CIO ================")
    print(result["verdict"])
