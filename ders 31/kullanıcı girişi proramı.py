print("""*********************************

===>KULLANICI GİRİŞİ PROGRAMI<===  

*********************************
""")

a = input("Lütfen kullanıcı adınızı giriniz : ")
b = input("Lütfen parolanızı giriniz : ")

sys_kullanici_adi = "orkun_or"
sys_parola = "orkun12345678"

if a == sys_kullanici_adi and b != sys_parola:
    print("Kullanıcı adınız doğru fakat parolanız yanlıştır...")
elif a != sys_kullanici_adi and b == sys_parola:
    print("Parolanız doğru fakat kullanıcı adınız yanlıştır...")
elif a != sys_kullanici_adi and b != sys_parola:
    print("Girmiş olduğunuz bilgiler yanlıştır")
elif a == sys_kullanici_adi and b == sys_parola:
    print("Girmiş olduğunuz bilgiler doğrudur \nsisteme hoşgeldiniz")

print("Program sonlandırılıyor...")













