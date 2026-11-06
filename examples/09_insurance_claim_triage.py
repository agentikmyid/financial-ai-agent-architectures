import os, json
from openai import OpenAI

# Bab 09: Insurance Claim Triage & Anti-Fraud Compliance Agent
client = OpenAI(
    base_url="https://api.agentik.my.id/v1",
    api_key=os.getenv("AGENTIK_API_KEY", "agtk_live_your_key_here")
)

def process_insurance_claim(claim_packet):
    prompt = f"""
    Bertindaklah sebagai Senior Insurance Claims Adjuster & Fraud Detector.
    Evaluasi berkas klaim asuransi berikut:
    - ID Klaim: {claim_packet['claim_id']}
    - Pemegang Polis: {claim_packet['holder_name']}
    - Limit Polis Tahunan: Rp{claim_packet['policy_limit']:,}
    - Total Klaim Terpakai Tahun Ini: Rp{claim_packet['used_to_date']:,}
    - Nilai Tagihan Klaim Baru: Rp{claim_packet['claimed_amount']:,}
    - Diagnosa Dokter: {claim_packet['diagnosis']}
    - Detail Tagihan Rumah Sakit: {claim_packet['hospital_items']}

    Tugas Analisis:
    1. Validasi kecukupan limit polis tersisa.
    2. Deteksi anomali harga obat/tindakan (indikasi *over-billing* atau fraud).
    3. Putusan Rekomendasi: [APPROVED / REJECTED / ESCALATE_TO_MANUAL_AUDIT] beserta alasannya.
    """

    res = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return res.choices[0].message.content

if __name__ == "__main__":
    print("=== BAB 09: INSURANCE CLAIM TRIAGE & FRAUD DETECTION ===")
    sample_claim = {
        "claim_id": "CLM-2026-8891",
        "holder_name": "Nasabah Prioritas A",
        "policy_limit": 100000000,
        "used_to_date": 82000000,
        "claimed_amount": 25000000,
        "diagnosis": "Rawat Inap Gastritis Akut (2 Hari)",
        "hospital_items": "Kamar VIP Rp4jt, Obat Injeksi Rp15jt, Biaya Administrasi Rp6jt"
    }
    hasil = process_insurance_claim(sample_claim)
    print(hasil)
