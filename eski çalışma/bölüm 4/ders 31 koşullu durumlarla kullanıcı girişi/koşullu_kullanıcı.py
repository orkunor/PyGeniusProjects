print("""**********************************
  -------KULLANICI GİRİŞİ-------
**********************************
""")

sys_kullanıcı_adı = "orkun_or"
sys_parola = "12345"

kullanıcı_adı = input("KULLANICI ADI : ")
parola = input("PAROLA : ")

if  kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola:
    print("PAROLA HATALI...")
elif kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola:
    print("KULLANICI ADI HATALI ...")
elif kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola:
    print("GİRİLEN BİLGİLER HATALIDIR...")
else:
    print("GİRİŞ BAŞARILI...")


