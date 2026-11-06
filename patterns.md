# 🏛️ Financial AI Agent Design Patterns

Dokumentasi pola desain arsitektur yang terbukti tahan uji (*production-ready*) untuk sistem AI di bidang finansial dan perdagangan kuantitatif.

---

## Pattern 1: Tool-Augmented Fundamental Analyst
Model LLM tidak boleh melakukan kalkulasi rasio matematika secara mandiri karena rawan halusinasi. Model hanya bertugas memanggil tools (kalkulator & database API) lalu menganalisis hasilnya.

```
User Query -> LLM -> Tool Call (get_financials) -> Execution -> Observation -> LLM Synthesis
```

---

## Pattern 2: Adversarial Debate (Bull vs Bear)
Dua agen dengan prompt berkebalikan berdebat secara dialektis:
1. **Bull Agent:** Diberikan peran agresif mencari katalis pertumbuhan dan potensi upside.
2. **Bear Agent:** Diberikan peran skeptis mencari titik kegagalan, risiko utang, dan potensi kebangkrutan.
3. **CIO Agent:** Mengadili kedua argumen, menimbang bobot bukti empiris, dan memutuskan *Position Sizing* (0% - 100%).

---

## Pattern 3: Self-Refine Reflection Loop
Agen menghasilkan draf analisis investasi perdana, kemudian mengirimkannya ke modul *Critic* internal untuk mendeteksi kelemahan logika sebelum diserahkan ke pengguna.
