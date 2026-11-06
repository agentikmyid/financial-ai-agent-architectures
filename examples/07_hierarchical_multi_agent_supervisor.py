import os
from openai import OpenAI

# Bab 07: Hierarchical Multi-Agent Supervisor Pattern
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def run_hierarchical_agents(ticker):
    print(f"=== SUPERVISOR MEMULAI AUDIT MULTI-AGENT UNTUK {ticker} ===
")
    
    # Worker 1: Macro Analyst
    print("1. Menjalankan Macro Analyst Agent...")
    macro_out = client.chat.completions.create(
        model="gemini-3.8-flash-high",
        messages=[{"role": "user", "content": "Evaluasi dampak tren suku bunga BI 2026 terhadap sektor perbankan Indonesia dalam 2 kalimat."}]
    ).choices[0].message.content

    # Worker 2: Quantitative Volatility Agent
    print("2. Menjalankan Quantitative Volatility Agent...")
    quant_out = client.chat.completions.create(
        model="gemini-3.8-flash-high",
        messages=[{"role": "user", "content": f"Aset: {ticker}. Volatilitas 30 hari = 18.5%, ATR = 120. Ringkas rezim risiko dalam 2 kalimat."}]
    ).choices[0].message.content

    # Supervisor Synthesis (Claude Sonnet)
    print("3. Supervisor mensintesis laporan kedua bawahan...")
    supervisor_res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "system", "content": "Anda adalah Executive Investment Supervisor. Buat arahan strategi akhir berdasarkan laporan tim spesialis Anda."},
            {"role": "user", "content": f"Laporan Makro:
{macro_out}

Laporan Kuantitatif:
{quant_out}"}
        ]
    ).choices[0].message.content

    return supervisor_res

if __name__ == "__main__":
    print("=== BAB 07: HIERARCHICAL SUPERVISOR MULTI-AGENT ===")
    print(run_hierarchical_agents("BBRI"))
