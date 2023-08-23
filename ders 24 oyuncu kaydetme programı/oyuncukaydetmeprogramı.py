print("Oyuncu kaydetme programı : ")

ad = input("Oyuncunun ismi nedir ? ")
soyad = input("Oyuncunun soyadı nedir ? ")
takim = input("Oyuncunun takimi nedir ? ")

# biz buradan bunu bir listenin içerisine atarak orada tutacağız...

bilgiler = [ad,soyad,takim]

print("Bilgiler kaydediliyor...")

print("Oyuncunun adi = {}\nOyuncunun soyadi : {}\nOyuncunun Takimi : {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))


print("Bilgiler kaydedildi...")