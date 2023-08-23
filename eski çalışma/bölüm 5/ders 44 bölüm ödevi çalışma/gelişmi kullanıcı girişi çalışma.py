print("""*************************************
     KULLANICI GİRİŞİ PROGRAMI 
*************************************
""")

sys_kullanıcı_girişi = "orkun_or"
sys_parola = "12345"

giriş_hakkı = 3

while giriş_hakkı > 0:
    kullanıcı_girişi = input("KULLANICI GİRİŞİ : ")
    kullanıcı_parola = input("PAROLA :")

    if sys_kullanıcı_girişi != kullanıcı_girişi and sys_parola == kullanıcı_parola:
        print("HATALI KULLAINICI GİRİŞİ LÜTFEN TEKRAR DENEYİNİZ")
        giriş_hakkı -= 1
    elif sys_kullanıcı_girişi == kullanıcı_girişi and sys_parola != kullanıcı_parola:
        print("HATALI PAROLA LÜTFEN TEKRAR DENEYİNİZ")
        giriş_hakkı -= 1
    elif sys_kullanıcı_girişi != kullanıcı_girişi and sys_parola != kullanıcı_parola:
        print("BİLGİLERİN HER İKİSİ DE HATALIDIR...")
        giriş_hakkı -= 1
    else:
        print("sisteme hoşgeldiniz :)")
        break