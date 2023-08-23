"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

"""
print("""
***********************************************
  ==>FONKSİYONLARLA MÜKEMMEL SAYI PROGRAMI<==
  
->ÇIKMAK İÇİN 'q'
***********************************************
""")
def mükemmel_sayı(sayı):
    liste = list()
    toplam = 0
    for i in range(1,sayı):
        if sayı % i == 0:
            liste.append(i)
    for x in liste:
        toplam += x
    if toplam == sayı:
        return print("Sayınız MÜKEMMELDİR")
    else:
        return print("Sayınız MÜKEMMEL Değildir.")

while True:
    sayı = input("Lütfen göndermek istediğiniz sayıyı giriniz : ")

    if sayı == "q":
        print("Program sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        mükemmel_sayı(sayı)