"""
Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
"""

ad = input("Adınızı giriniz : ")
soyad = input("Soyadınızı giriniz : ")
numara = input("Numaranızı giriniz : ")

bilgiler = [ad,soyad,numara]

print("AD : {}\nSOYAD : {}\nNUMARA : {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))