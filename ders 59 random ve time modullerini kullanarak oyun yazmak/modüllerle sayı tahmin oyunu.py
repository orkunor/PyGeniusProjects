"""
Bu programda modülleri kullanarak sayı tahmin oyunu oluşturacağız...
"""
import random #öncelikle kullancağımız modülleri çektik
import time # bu modüllerin içerisindeki fonksiyonları programımızda kullancağız...

print("""*****************************
  ==> SAYI TAHMİN OYUNU <==  

-> 1 ile 40 arasındaki sayıyı tahmin edin   

*****************************
""")

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:
    tahmin = int(input("Lütfen bir sayı tahmin ediniz : "))

    if tahmin < rastgele_sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(3)
        print("tahmininiz bulmanız gereken sayıdan küçüktür.\nLütfen daha yüksek bir sayı söyleyiniz...")
        tahmin_hakkı -= 1
    elif tahmin > rastgele_sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(3)
        print("Tahmininiz bulmanız gereken sayıdan büyüktür .\nLütfen daha düşük bir sayı giriniz...")
        tahmin_hakkı -= 1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(3)
        print("TEBRİKLER;TAHMİNİNİZ DOĞRU :",rastgele_sayı)
        break
    if tahmin_hakkı == 0:
        print("Tahmin hakkınız dolmuştur;\nProgram sonlandırılıyor;\nLütfen daha sonra tekrar deneyiniz...")
        print("SAYIMIZ:",rastgele_sayı)
        break