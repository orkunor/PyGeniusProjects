print("""
**************************************
-----HARF NOTU HESAPLAMA PROGRAMI-----
""")

vize1 = int(input("1. VİZE = "))
vize2 = int(input("2. VİZE ="))
final = int(input("FİNAL = "))

dönem_notu = vize1*0.3 + vize2*0.3 + final*0.4

if dönem_notu >= 90:
    print("AA")
elif dönem_notu >= 85:
    print("BA")
elif dönem_notu >= 80:
    print("BB")
elif dönem_notu >= 75:
    print("CB")
elif dönem_notu >= 70:
    print("CC")
elif dönem_notu >= 65:
    print("DC")
elif dönem_notu >= 60:
    print("DD")
elif dönem_notu >= 55:
    print("FD")
elif dönem_notu < 55:
    print("FF")
else:
    print("HATALI BİLGİ GİRİŞİ")





