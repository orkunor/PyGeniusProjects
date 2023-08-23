"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın
ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

print("""************************************************

BEDEN KİTLE ENDEKSİ HESAPLAMA PROGRAMI 

************************************************
""")

a = float(input("lütfen boyunuzu giriniz(m) : "))
b = float(input("lütfen kilonuzu giriniz(kg) : "))

indeks = b/(a*a)

if indeks < 18.5:
    print("ZAYIF")
elif 25 > indeks >= 18.5 :
    print("NORMAL")
elif 30 > indeks >= 25:
    print("FAZLA KİLOLU")
elif  indeks >= 30:
    print("OBEZ")
else:
    print("TANIMLI DEĞİL")
print("program sonlandırılıyor.... ")