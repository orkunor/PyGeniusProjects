""""
ASAL SAYI BULMA PROGRAMI
"""

print("""
*********************************
 ==> ASAL SAYI BULAN PROGRAM <==
*********************************
""")

sayı = int(input("Lütfen kontrol edilecek sayıyı giriniz : "))

if sayı > 1:
    for i in range(2,sayı):
        if sayı % i == 0:
            print("Sayınız Asal değildir.")
            break
    else:
        print("Sayınız Asaldır")
else:
    print("Sayınız asal değildir")