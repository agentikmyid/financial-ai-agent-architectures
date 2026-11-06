import os
from openai import OpenAI

# Bab 03: Orkestrasi State Machine Finansial (Pola LangGraph / Deterministik)
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def stage_1_ingest(ticker):
    print(f"[State 1: Ingestion] Mengambil data neraca untuk {ticker}...")
    return {"ticker": ticker, "revenue_growth": 15.2, "debt_equity": 0.35, "pe_ratio": 18.5}

def stage_2_valuation_node(data):
    print("[State 2: Valuation Node] Mengevaluasi kewajaran harga...")
    prompt = f"Data {data['ticker']}: P/E {data['pe_ratio']}x, Debt/Equity {data['debt_equity']}. Tentukan status: CHEAP / FAIR / EXPENSIVE dalam 1 kata."
    res = client.chat.completions.create(
        model="gemini-3.8-flash-high",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=10
    )
    status = res.choices[0].message.content.strip()
    data["valuation_status"] = status
    return data

def stage_3_router_condition(data):
    print(f"[State 3: Conditional Routing] Status valuasi = {data['valuation_status']}")
    if "CHEAP" in data["valuation_status"].upper() or "FAIR" in data["valuation_status"].upper():
        return "PROCEED_TO_RISK_AUDIT"
    return "ABORT_OVERVALUED"

if __name__ == "__main__":
    print("=== BAB 03: DETERMINISTIC STATE MACHINE ORCHESTRATION ===")
    payload = stage_1_ingest("TLKM")
    evaluated = stage_2_valuation_node(payload)
    next_step = stage_3_router_condition(evaluated)
    print("Arah Eksekusi StateGraph Selanjutnya:", next_step)
