import os, time
from openai import OpenAI

# Production Harness dengan Model Fallback (Claude Sonnet -> Gemini Flash High)
PRIMARY_MODEL = "claude-sonnet-4-6"
FALLBACK_MODEL = "gemini-3.8-flash-high"

client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def robust_agent_execute(prompt, max_retries=3):
    models = [PRIMARY_MODEL, FALLBACK_MODEL]
    
    for model in models:
        for attempt in range(max_retries):
            try:
                print(f"Mencoba eksekusi dengan model: {model} (Percobaan {attempt + 1})...")
                res = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    timeout=30
                )
                return res.choices[0].message.content
            except Exception as e:
                print(f"Peringatan: Gagal pada model {model}: {e}")
                time.sleep(2)
                
    raise RuntimeError("Seluruh model cadangan gagal dieksekusi!")

if __name__ == "__main__":
    print("=== CONTOH BAB 12: PRODUCTION RESILIENCE HARNESS ===")
    hasil = robust_agent_execute("Berikan 3 metrik utama likuiditas dalam pasar uang.")
    print("Respon Berhasil:\n", hasil[:250], "...")
