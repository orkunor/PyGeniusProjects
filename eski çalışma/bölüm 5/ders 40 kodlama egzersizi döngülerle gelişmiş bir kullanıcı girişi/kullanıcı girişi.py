print("""***********************************
    KULLANICI GİRİŞİ PROGRAMI 
***********************************
""")

sys_kullanıcı_adı = "orkun_or"

sys_parola = "12345678"

giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı : ")
    parola = input("Parola:")
    if (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("KULLANICI ADI HATALI....")
        giriş_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("HATALI PAROLA...")
        giriş_hakkı -= 1
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("İKİ BİLGİ DE HATALI...")
        giriş_hakkı -= 1
    else:
        print("SİSTEME BAŞARIYLA GİRİŞ YAPILDI....")
        break
    if giriş_hakkı == 0:
        print("GİRİŞ HAKKINIZ BİTTİ...")
        break