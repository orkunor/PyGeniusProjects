""""
=> ASAL SAYILAR 1'E VE KENDİNDEN BAŞKA HERHANGİ BİR SAYIYA BÖLÜNMEYEN SAYILARA ASAL SAYILAR DENİR
"""
# girilen sayının asal olup olmadığını önce kendimiz deneyelim sonra fonksiyonla deneyelim

sayı = int(input("Lütfen sayıyı giriniz : "))

if sayı > 1 :
    for i in range(2,sayı):
        if sayı % i == 0 :
            print("Sayınız asal değildir.")
            break
    else:
        print("Sayınız asaldır")
else:
    print("Sayınız Asal değildir...")







