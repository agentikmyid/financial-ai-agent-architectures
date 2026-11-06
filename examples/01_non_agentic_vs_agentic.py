import os
from openai import OpenAI

# Bab 01: Fondasi Agen Finansial - Perbandingan Panggilan Pasif vs Tool Calling
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

# 1. Non-Agentic Call (Model biasa: tidak tahu harga riil detik ini)
def non_agentic_call(ticker):
    print(f"1. Meminta analisis biasa tanpa tool untuk {ticker}...")
    res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": f"Berapa harga saham {ticker} hari ini?"}],
        max_tokens=100
    )
    return res.choices[0].message.content

# 2. Agentic Tool Calling (Model otonom memanggil fungsi bursa live)
tools = [
    {
        "type": "function",
        "function": {
            "name": "fetch_live_market_data",
            "description": "Mengambil harga real-time dan volume orderbook dari bursa.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {"type": "string", "description": "Ticker aset finansial (cth: BBCA, TLKM, BTC)"}
                },
                "required": ["symbol"]
            }
        }
    }
]

def agentic_tool_call(ticker):
    print(f"2. Meminta analisis agentic dengan tool definition untuk {ticker}...")
    res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": f"Periksa harga terkini untuk {ticker} dan hitung jika ada anomali volume."}],
        tools=tools
    )
    msg = res.choices[0].message
    if msg.tool_calls:
        tool = msg.tool_calls[0]
        print(f"✅ Agen memutuskan memanggil fungsi eksternal: {tool.function.name}")
        print(f"✅ Parameter yang dikirim: {tool.function.arguments}")
    return msg

if __name__ == "__main__":
    print("=== BAB 01: NON-AGENTIC VS AGENTIC SYSTEM DEMO ===")
    print(non_agentic_call("BBCA"))
    print("-" * 50)
    agentic_tool_call("BBCA")
