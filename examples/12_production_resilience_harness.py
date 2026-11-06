import os, time
from openai import OpenAI

# Bab 12: Production Harness - Idempotency, Failover Fallback & Rate Limiter
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

# Idempotency Cache simulasi (mencegah double-execution order)
EXECUTED_TRANSACTIONS = set()

def robust_financial_executor(idempotency_key, order_payload):
    print(f"
[HARNESS] Memproses Order dengan Idempotency Key: {idempotency_key}...")
    
    # 1. Idempotency Check
    if idempotency_key in EXECUTED_TRANSACTIONS:
        return f"⚠️ PERINGATAN: Transaksi {idempotency_key} sudah pernah dieksekusi sebelumnya. Mengembalikan status sukses tanpa duplikasi order."
    
    # 2. Resilient Execution with Model Fallback
    models_tier = ["claude-sonnet-4-6", "gemini-3.8-flash-high"]
    
    for model_name in models_tier:
        try:
            print(f"-> Mencoba eksekusi melalui model: {model_name}...")
            res = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "Anda adalah Order Validation Engine institusi."},
                    {"role": "user", "content": f"Validasi parameter order: {order_payload}. Kembalikan status: EXECUTED_OK."}
                ],
                timeout=15
            )
            # Simpan transaksi ke memory idempotency
            EXECUTED_TRANSACTIONS.add(idempotency_key)
            return f"✅ SUCCESS ({model_name}): {res.choices[0].message.content.strip()}"
        except Exception as e:
            print(f"❌ Model {model_name} gagal: {e}. Mengalihkan ke model fallback...")
            time.sleep(1)
            
    raise RuntimeError("Semua node model gagal merespons!")

if __name__ == "__main__":
    print("=== BAB 12: PRODUCTION RESILIENCE HARNESS ===")
    key = "TX-IDEMP-9921820"
    order = {"symbol": "BBCA", "action": "BUY", "shares": 1000, "limit_price": 9850}
    
    # Eksekusi pertama
    print(robust_financial_executor(key, order))
    
    # Simulasi eksekusi kedua dengan key yang sama (uji proteksi duplikasi)
    print(robust_financial_executor(key, order))
