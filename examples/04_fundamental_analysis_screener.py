import os
from openai import OpenAI

# Bab 04: Fundamental Analysis Screener (3 Laporan Keuangan & Rasio Kunci)
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def audit_fundamental_emiten(ticker, metrics):
    prompt = f"""
    Bertindaklah sebagai Senior Equity Research Analyst berstandar CFA.
    Audit fundamental emiten {ticker} berdasarkan metrik laporan keuangan berikut:
    - Return on Invested Capital (ROIC): {metrics['roic']}%
    - Operating Cash Flow to Net Income: {metrics['ocf_ni_ratio']}x
    - Net Debt / EBITDA: {metrics['debt_ebitda']}x
    - Free Cash Flow Yield: {metrics['fcf_yield']}%
    - Piotroski F-Score: {metrics['piotroski_f_score']}/9

    Sajikan evaluasi:
    1. Kualitas Laba Akuntansi vs Arus Kas Riil
    2. Ketahanan Solvabilitas & Alokasi Modal
    3. Skor Kelayakan Fundamental (0 - 100) dan Rekomendasi
    """

    res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return res.choices[0].message.content

if __name__ == "__main__":
    print("=== BAB 04: FUNDAMENTAL FINANCIAL STATEMENT AUDITOR ===")
    sample_metrics = {
        "roic": 22.4,
        "ocf_ni_ratio": 1.25,
        "debt_ebitda": 0.8,
        "fcf_yield": 7.1,
        "piotroski_f_score": 8
    }
    hasil = audit_fundamental_emiten("BBCA", sample_metrics)
    print(hasil)
