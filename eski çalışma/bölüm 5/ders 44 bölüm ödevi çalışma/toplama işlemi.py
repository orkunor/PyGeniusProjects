print("""*************************************
     ==> TOPLAMA İŞLEMİ <==
*************************************     

SİSTEMDEN AYRILMAK İÇİN : 'q'
""")

toplam = 0

while True:
    sayı = input("TOPLAMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ : ")

    if sayı == "q":
        print("Program sonlandırılıyor...")
        break

    sayı = int(sayı)

    toplam += sayı

print("TOPLAM :",toplam)













