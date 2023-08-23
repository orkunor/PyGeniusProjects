print("""
*********************************************
       MÜKEMMEL SAYI BULAN PROGRAM 
*********************************************
""")

sayı = int(input("ARAŞTIRMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ :"))
toplam = 0
for i in range(1,sayı):
    if sayı % i == 0:
        toplam += i
if toplam == sayı:
    print("SAYINIZ MÜKEMMELDİR : ",sayı)
else:
    print("SAYINIZ MÜKEMMEL DEĞİLDİR : ",sayı)