import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

# 1. Non-Agentic Call (Passive LLM - Rentan Outdated/Hallucination)
def non_agentic_analysis(query):
    return client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": query}]
    ).choices[0].message.content

# 2. Agentic Tool Calling (Verifiable, Real-Time Data)
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_quote",
            "description": "Mengambil harga saham terkini dan volume bursa.",
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

print("=== CONTOH BAB 1: NON-AGENTIC VS AGENTIC TOOL CALLING ===")
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Berapa harga saham BBCA hari ini dan bagaimana performanya?"}],
    tools=tools
)

msg = response.choices[0].message
if msg.tool_calls:
    print("✅ Agen berhasil memicu Tool Call:", msg.tool_calls[0].function.name)
    print("Argumen Parameter:", msg.tool_calls[0].function.arguments)
