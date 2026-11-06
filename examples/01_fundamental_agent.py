import os
from openai import OpenAI

# Inisialisasi client via Agentik Proxy Gateway
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def analyze_fundamentals(ticker, pe_ratio, roe, debt_to_equity, revenue_growth):
    prompt = f"""
    Lakukan analisis fundamental institusional untuk emiten {ticker} dengan metrik berikut:
    - P/E Ratio: {pe_ratio}
    - ROE: {roe}%
    - Debt-to-Equity: {debt_to_equity}
    - Revenue Growth (YoY): {revenue_growth}%

    Berikan penilaian objektif mengenai:
    1. Valuasi saat ini (Undervalued / Fair / Overvalued).
    2. Kualitas profitabilitas dan efisiensi modal.
    3. Profil risiko solvabilitas.
    4. Kesimpulan kelayakan investasi.
    """

    response = client.chat.completions.create(
        model="claude-3-5-sonnet-20241022",
        messages=[
            {"role": "system", "content": "Anda adalah Senior Equity Research Analyst berstandar CFA."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    print("Menjalankan Fundamental Analysis Agent...")
    hasil = analyze_fundamentals("BBCA", pe_ratio=21.5, roe=19.8, debt_to_equity=0.15, revenue_growth=12.4)
    print("\n--- HASIL ANALISIS ---")
    print(hasil)
