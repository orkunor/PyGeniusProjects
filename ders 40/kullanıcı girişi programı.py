"""
while döngüsüyle yazacağız ve programın tek seferde başlayıp sonlanmasının önüne geçeceğiz
ve biz doğru istenilen cevabı girene kadar programın devam etmesini sağlayacağız
-> While döngüsüyle yapmamızın sebebi bu döngüde girşte bir koşul beliteceğiz bu yüzden while döngüsüyle yapıyoruz...
-> öncelikle sistemde kayıtlı olan bi kullanıcı adının olduğunu varsayalım
-> istersek bunu inputlada alabiliriz
"""
print("""**********************************************
 ===> GELİŞMİŞ KULLANICI GİRİŞİ PROGRAMI <===
**********************************************
""")
a = 0
nick = "orkun_or"
şifre = "orkun12345678"
while a<3:
    sys_kullanıcı_girişi = input("Lütfen kullanıcı adınızı giriniz : ") # burada her seferde tekrar bilgileri almalıyız
    sys_şifre = input("Lütfen şifrenizi giriniz : ") # çünkü girilen bilgiler yanlış olunca tekrar girilmelidir...
    if sys_kullanıcı_girişi == nick and sys_şifre == şifre:
        print("Programa hoşgeldiniz")
        break
    elif a == 0:
        print("ilk denemeniz hatalıdır...")
    elif a == 1:
        print("son 1 giriş hakkınız kaldı...")
    elif a == 2:
        print("Girmiş olduğunuz bilgiler hatalı olduğundan sisteme girişiniz engellendi")
    a += 1
print("Program sonlanmıştır")