import os, json
from openai import OpenAI

# Bab 02: Design Patterns - State Memory Buffer & Dynamic Tool Registry
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

class FinancialAgentWithMemory:
    def __init__(self):
        self.conversation_memory = [
            {"role": "system", "content": "Anda adalah AI Portfolio Analyst. Anda mengingat portofolio pengguna dan batasan risiko mereka."}
        ]
        self.portfolio_state = {"CASH": 50000000, "HOLDINGS": {}}

    def chat(self, user_input):
        self.conversation_memory.append({"role": "user", "content": user_input})
        
        # Injeksi context state portofolio secara dinamis
        state_prompt = f"\n[PORTFOLIO STATE REAL-TIME: Kas Rp{self.portfolio_state['CASH']:,}, Aset: {self.portfolio_state['HOLDINGS']}]"
        augmented_messages = list(self.conversation_memory)
        augmented_messages[-1] = {"role": "user", "content": user_input + state_prompt}

        response = client.chat.completions.create(
            model="claude-sonnet-4-6",
            messages=augmented_messages,
            temperature=0.2
        )
        
        reply = response.choices[0].message.content
        self.conversation_memory.append({"role": "assistant", "content": reply})
        return reply

if __name__ == "__main__":
    print("=== BAB 02: DESIGN PATTERNS - MEMORY & STATE CONTEXT ===")
    agent = FinancialAgentWithMemory()
    print("Turn 1:", agent.chat("Saya mau beli saham BBCA senilai Rp15.000.000. Berapa sisa kas saya nanti?"))
    agent.portfolio_state["CASH"] -= 15000000
    agent.portfolio_state["HOLDINGS"]["BBCA"] = 15000000
    print("-" * 50)
    print("Turn 2:", agent.chat("Apakah kas saya masih aman untuk toleransi risiko konservatif?"))
