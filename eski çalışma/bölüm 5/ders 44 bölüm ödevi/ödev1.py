print("""********************************
         MÜKEMMEL SAYI

PROGRAMDAN ÇIKMAK İÇİN : 'q'         
********************************
""")

sayı = int(input("SAYI:"))

i = 1
toplam = 0

while i < sayı:
    if sayı % i == 0:
        toplam += i
    i += 1
if toplam == sayı:
    print("TEBRİKLER SAYINIZ MÜKEMMEL")
else:
    print("MAALESEF SAYINIZ MÜKEMMEL DEĞİL...")