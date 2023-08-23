print("""
**********************************
BEDEN KİTLE İNDEKSİ HESAPLAYICISI
**********************************
""")

kilo = float(input("KİLO(kg):"))
boy = float(input("BOY(m):"))

indeks = kilo / (boy ** 2)

if indeks > 30:
    print("OBEZ")
elif indeks >=25:
    print("FAZLA KİLOLU")
elif indeks >= 18.5:
    print("NORMAL")
elif indeks < 18.5:
    print("ZAYIF")
else:
    print("GİRİLEN BİLGİLER HATALI .... ")





