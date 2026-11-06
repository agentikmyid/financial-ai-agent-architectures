import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def deep_search_query_expander(user_topic):
    prompt = f"""
    Pengguna ingin riset mendalam tentang topik: "{user_topic}"
    Sebagai Analis Keuangan Senior, pecah topik ini menjadi 4 sub-query investigasi yang tajam untuk mencari data primer:
    1. Metrik Kinerja Keuangan & Margin
    2. Risiko Regulasi & Legal
    3. Posisi Kompetitif Pasar
    4. Ketergantungan Rantai Pasok / Konsentrasi Klien
    Format output berupa list JSON.
    """

    res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content

if __name__ == "__main__":
    print("=== CONTOH BAB 5: DEEP SEARCH QUERY EXPANDER ===")
    print(deep_search_query_expander("Ekspansi Ekosistem Solana & Tren DeFi Meteora"))
