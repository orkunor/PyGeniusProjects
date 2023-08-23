"""
mükemmel sayı = pozitif bir sayının tam bölenleri toplamının sayının kendisinin 2 katı olmasına verilen ad
"""
print("""********************************
  ==>MÜKEMMEL SAYI PROGRAMI<==  
-> Lütfen programdan çıkmak için '0' ya baısınız
********************************
""")
while True :
    toplam=0
    a = int(input("Kontrol etmek istediğiniz sayıyı giriniz :"))
    if a == 0:
        print("Program sonlandırılıyor.")
        break
    else:
        for i in range(1,a+1):
            if a % i == 0:
                toplam += i
        if toplam == 2*a:
            print("Sayınız mükemmeldir.")
        else:
            print("Sayınız mükemmel değildir.")