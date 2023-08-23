"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve
kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın
"""
print("""******************************
   ==> TOPLAMA PROGRAMI <==    
******************************
""")
toplam = 0

while True:
    a = input("Lütfen bir sayı giriniz (çıkmak için 'q' harfine basınız...): ")
    if a == "q":
        print("Program sonlandırılıyor...")
        break
    else :
        toplam += int(a)
print(toplam)