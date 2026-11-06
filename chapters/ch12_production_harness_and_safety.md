# Bab 12: Menjalankan Agen Finansial di Lingkungan Produksi

## Anatomi Harness Sistem Produksi
Sebuah agen AI tidak boleh dibiarkan memanggil API secara liar di production. Sistem membutuhkan **Production Harness**:

1. **Idempotency Keys:** Memastikan order trading atau transaksi finansial tidak tereksekusi dua kali jika terjadi gangguan jaringan.
2. **Graceful Degradation:** Jika model utama (misal Claude 3.5 Sonnet) mengalami rate-limit, sistem otomatis berpindah (*fallback*) ke GPT-4o atau DeepSeek R1 tanpa menghentikan workflow.
3. **Budget Caps & Rate Limiting:** Batasan maksimal konsumsi token per menit agar tidak terjadi tagihan membengkak akibat infinite loop.
4. **Structured Audit Logging:** Setiap panggilan LLM, tool input, dan tool output disimpan di database terenkripsi untuk pelaporan audit regulator.

Lihat script demo: [`examples/08_production_harness_resilience.py`](../examples/08_production_harness_resilience.py)
