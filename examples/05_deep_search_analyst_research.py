import os
from openai import OpenAI

# Bab 05: Deep Search - Multi-Hop Query Expansion & Validasi Sumber Primer
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def deep_search_planner(target_subject):
    prompt = f"""
    Anda memimpin investigasi intelijen pasar saham untuk topik: "{target_subject}".
    Pecah investigasi ini menjadi 4 sub-query spesifik yang menyasar DOKUMEN PRIMER (SEC Filings, Keterbukaan Informasi BEI, Transaksi Afiliasi):
    
    1. Sub-query Forensik Utang & Likuiditas
    2. Sub-query Gugatan Hukum & Risiko Regulasi
    3. Sub-query Transaksi Orang Dalam (Insider Trading)
    4. Sub-query Pangsa Pasar vs Kompetitor Utama

    Sertakan instruksi parameter filter untuk masing-masing query.
    """

    res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content

if __name__ == "__main__":
    print("=== BAB 05: DEEP SEARCH RESEARCH QUERY PLANNER ===")
    plan = deep_search_planner("Restrukturisasi Utang dan Rencana Rights Issue Emiten Sektor Energi")
    print(plan)
