import random # random modülünün içerisindeki sadece bir tane fonksiyonu kullanıcaz ve rastgele sayı üreticez
import time # " "

print("""
*********************************
      SAYI TAHMİN OYUNU
      
1 - 40 ARASINDA BİR SAYI TAHMİN EDİN        
*********************************
""")

rastgele_sayı = random.randint(1,40) # bu sayılar dahil unutma !!!
tahmin_hakkı = 7

while True:
    tahmin = int(input("TAHMİNİNİZİ GİRİNİZ :"))

    if tahmin < rastgele_sayı:
        print("Tahmininiz sorgulanıyor...")
        time.sleep(1)
        print("DAHA YÜKSEK BİR SAYI DENEYİNİZ...")
        tahmin_hakkı -= 1

    elif tahmin > rastgele_sayı:
        print("Tahmininiz sorgulanıyor...")
        time.sleep(1)
        print("DAHA DÜŞÜK BİR SAYI DENEYİNİZ...")
        tahmin_hakkı -= 1
    else:
        print("Tahmininiz sorgulanıyor...")
        time.sleep(1)
        print("TEBRİKLER SAYINIZ DOĞRU ==> ",rastgele_sayı)
        break

    if tahmin_hakkı == 0 :
        print("HAKKINIZ BİTTİ ")
        print("Sayımızı : ",rastgele_sayı)