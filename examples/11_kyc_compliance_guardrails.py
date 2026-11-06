import os
from openai import OpenAI

# Bab 11: Guardrails Kepatuhan & Mitigasi Halusinasi Finansial (KYC / Suitability)
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def kyc_suitability_guardrail(client_profile, asset_recommendation):
    prompt = f"""
    Bertindaklah sebagai Chief Compliance Officer (Regulator & KYC Protection).
    Audit rekomendasi investasi berikut:
    
    [PROFIL NASABAH]:
    - Usia: {client_profile['age']} tahun
    - Toleransi Risiko: {client_profile['risk_tolerance']}
    - Horizon Investasi: {client_profile['horizon']}
    - Tujuan: {client_profile['goal']}
    
    [PROPOSAL INVESTASI]:
    {asset_recommendation}
    
    Tugas Guardrails:
    1. Apakah aset ini sesuai dengan profil risiko nasabah? (Suitability Check).
    2. Jika tidak cocok, tolak dan arahkan ke instrumen yang tepat.
    3. Sematkan Disclaimer Risiko Hukum resmi otomatis di bagian penutup.
    """

    res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return res.choices[0].message.content

if __name__ == "__main__":
    print("=== BAB 11: KYC SUITABILITY & COMPLIANCE GUARDRAIL ===")
    nasabah = {
        "age": 62,
        "risk_tolerance": "SANGAT KONSERVATIF",
        "horizon": "1 Tahun",
        "goal": "Dana Pensiun & Menjaga Modal Pokok"
    }
    proposal = "Alokasikan 70% dana pada koin meme kripto leverage tinggi dan 30% opsi saham volatilitas tinggi untuk gain cepat."
    audit_verdict = kyc_suitability_guardrail(nasabah, proposal)
    print(audit_verdict)
