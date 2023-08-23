sayı = input("SAYI:")
basamak_sayısı = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

geçiçi_sayı = sayı

while geçiçi_sayı > 0:
    basamak = geçiçi_sayı % 10
    toplam += basamak ** basamak_sayısı
    geçiçi_sayı //= 10
if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır")
else:
    print(sayı,"bir armstrong sayısı değildir")
