import os
from openai import OpenAI

# Bab 06: Self-Refine Reflection Loop (Penyusunan Tesis Bebas Bias)
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def self_refine_thesis(ticker, raw_idea):
    print(f"--- 1. GENERATE DRAFT THESIS ({ticker}) ---")
    draft = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": f"Buat draf tesis beli untuk {ticker}: {raw_idea}"}],
        max_tokens=200
    ).choices[0].message.content
    print(draft[:180], "...
")

    print("--- 2. ADVERSARIAL CRITIQUE NODE ---")
    critique = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "system", "content": "Anda adalah Senior Risk Auditor. Cari 3 lubang asumsi paling berbahaya dari draf tesis ini."},
            {"role": "user", "content": draft}
        ],
        max_tokens=250
    ).choices[0].message.content
    print(critique[:180], "...
")

    print("--- 3. INSTITUTIONAL REFINED THESIS ---")
    final_output = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "system", "content": "Tulis ulang tesis menjadi dokumen investasi institusi yang menjawab dan memitigasi semua kritik risiko."},
            {"role": "user", "content": f"Draf Awal:
{draft}

Kritik Risiko:
{critique}"}
        ]
    ).choices[0].message.content
    return final_output

if __name__ == "__main__":
    print("=== BAB 06: SELF-REFINE REFLECTION LOOP DEMO ===")
    res = self_refine_thesis("ASII", "Penjualan mobil listrik baru akan melonjak 100% dan mendongkrak laba bersih kuartal depan.")
    print(res)
