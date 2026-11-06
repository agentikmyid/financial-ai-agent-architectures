import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

# 1. Non-Agentic Call (Passive LLM - Rentan Halusinasi & Outdated)
def non_agentic_analysis(query):
    return client.chat.completions.create(
        model="claude-3-5-sonnet-20241022",
        messages=[{"role": "user", "content": query}]
    ).choices[0].message.content

# 2. Agentic Tool Calling (Verifiable, Real-Time Data)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_quote",
            "description": "Mengambil harga saham terkini dan volume harian.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {"type": "string", "description": "Ticker saham, misal BBCA, TLKM, AAPL"}
                },
                "required": ["symbol"]
            }
        }
    }
]

def mock_get_stock_quote(symbol):
    # Simulasi data bursa riil
    return {"symbol": symbol, "price": 9850, "currency": "IDR", "change_pct": 1.54, "volume": 54200000}

print("=== CONTOH BAB 1: NON-AGENTIC VS AGENTIC TOOL CALLING ===")
response = client.chat.completions.create(
    model="claude-3-5-sonnet-20241022",
    messages=[{"role": "user", "content": "Berapa harga saham BBCA hari ini dan bagaimana performanya?"}],
    tools=tools
)

msg = response.choices[0].message
if msg.tool_calls:
    print("Agen memutuskan memanggil Tool:", msg.tool_calls[0].function.name)
    print("Argumen:", msg.tool_calls[0].function.arguments)
