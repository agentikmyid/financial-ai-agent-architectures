import os
from openai import OpenAI

# Bab 10: Agentic RAG untuk Laporan Keuangan (Structure-Aware Table Extraction)
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

# Simulasi tabel neraca padat SEC 10-K
SAMPLE_10K_BALANCE_SHEET = """
| (in Millions USD) | FY 2025 | FY 2024 | FY 2023 |
| :--- | :--- | :--- | :--- |
| Cash and cash equivalents | $29,965 | $28,155 | $24,977 |
| Marketable securities | $31,580 | $35,210 | $31,590 |
| Total Current Assets | $135,420 | $143,566 | $134,836 |
| Total Non-Current Debt | $98,450 | $104,500 | $108,200 |
| Shareholder Equity | $74,210 | $62,146 | $60,274 |
"""

def query_financial_table_rag(table_markdown, question):
    prompt = f"""
    Anda adalah Specialized Financial Document Parser.
    Gunakan hanya data tabel laporan keuangan berikut:
    
    {table_markdown}
    
    Pertanyaan: {question}
    
    Instruksi:
    1. Tunjukkan baris dan angka tepat yang digunakan dalam perhitungan.
    2. Hitung rasio kas terhadap utang jangka panjang (Cash-to-Debt Ratio) untuk FY 2025.
    3. Hindari asumsi angka di luar data tabel.
    """

    res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    return res.choices[0].message.content

if __name__ == "__main__":
    print("=== BAB 10: AGENTIC RAG TABLE PARSER ===")
    ans = query_financial_table_rag(SAMPLE_10K_BALANCE_SHEET, "Berapa rasio kas dan ekuivalen terhadap utang jangka panjang di FY 2025?")
    print(ans)
