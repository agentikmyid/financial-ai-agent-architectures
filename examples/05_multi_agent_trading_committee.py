import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def self_refine_investment_thesis(ticker, raw_thesis):
    print("1. Menghasilkan Tesis Awal...")
    
    print("2. Agen Kritik sedang menguji kelemahan logika...")
    critique = client.chat.completions.create(
        model="claude-3-5-sonnet-20241022",
        messages=[
            {"role": "system", "content": "Anda adalah Chief Risk Officer yang sangat skeptis. Temukan celah asumsi yang tidak realistis dalam tesis ini."},
            {"role": "user", "content": f"Tesis {ticker}:\n{raw_thesis}"}
        ]
    ).choices[0].message.content

    print("3. Agen Penulis sedang merevisi tesis agar tahan uji...")
    refined = client.chat.completions.create(
        model="claude-3-5-sonnet-20241022",
        messages=[
            {"role": "system", "content": "Tulis ulang tesis investasi menjadi versi final institusional yang menjawab tuntas semua kritik risiko."},
            {"role": "user", "content": f"Tesis Awal:\n{raw_thesis}\n\nKritik Risiko:\n{critique}"}
        ]
    ).choices[0].message.content

    return refined

print("=== CONTOH BAB 6: SELF-REFINE REFLECTION LOOP ===")
sample = "Saham XYZ pasti naik 50% tahun ini karena meluncurkan produk AI baru dan revenue tumbuh 30%."
final_thesis = self_refine_investment_thesis("XYZ", sample)
print("\n--- TESIS REVISED (INSTITUTIONAL GRADE) ---")
print(final_thesis)
