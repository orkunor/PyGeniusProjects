import time

from kütüphane import *

print("""
*****************************************
 ==> Kütüphane Programına Hoşgeldiniz <==

İşlemler : 

Kitapları Göster => 1

Kitap Sorgula    => 2

Kitap Ekle       => 3

Kitap Sil        => 4

Baskı Yükselt    => 5 

Çıkmak İçin      => q
 
*****************************************

""")

kütüphane = Kütüphane()


while True:
    işlem = input("Lütfen Yapacağınız İşlemi Giriniz : ")

    if işlem == "q":
        print("Program Sonlandırılıyorr...")
        print("Yine Bekleriz .....")
        break
    elif işlem == "1":
        kütüphane.kitapları_göster()

    elif işlem == "2":
        isim = input("Hangi Kitabı İstiyorsunuz ? ")
        print("Kitap Sorgulanıyor ... ")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)

    elif işlem == "3":
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayınevi = input("Yayınevi:")
        tür = input("Tür:")
        baskı = int(input("Baskı:"))

        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)

        print("Kitap Ekleniyor...")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)

        print("Kitap Eklendi...")

    elif işlem == "4":
        isim = input("Hnagi Kitabı Silmek İstiyorusunuz....")

        cevap = input("Emin misiniz (E/H)")

        if cevap == "E":
            print("Kitap Siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap Silindi....")

    elif işlem == "5":
        isim = input("Hangi Kitabın Baskısını Yükseltmek İstiyorsunuz ? ")
        print("Baskı Yükseltiliyor....")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı Yükseltildi... ")

    else:
        print("Geçersiz İşlem...")








































































