import datetime

print("\n--- MFUMO WA ODA: WILLY-PROJECT ---")
print("1. Vyeti vya Kuzaliwa")
print("2. Kutengeneza Logo")
print("3. Website Development")
print("4. Automotive System Service")

jina = input("\nWeka Jina la Mteja: ")
chaguo = input("Chagua Namba ya Huduma (1-4): ")

huduma_map = {
    "1": "Vyeti vya Kuzaliwa",
    "2": "Kutengeneza Logo",
    "3": "Website Development",
    "4": "Automotive System Service"
}

if chaguo in huduma_map:
    jina_h = huduma_map[chaguo]
    muda = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"""
======================================
         WILLY-PROJECT RECEIPT
======================================
Tarehe: {muda}
Mteja: {jina}
--------------------------------------
Huduma: {jina_h}
======================================
""")
else:
    print("\nChaguo si sahihi!")

