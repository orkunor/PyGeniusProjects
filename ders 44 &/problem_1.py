"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı
kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
print("""******************************
==> MÜKEMMEL SAYI PROGRAMI <==
******************************
""")
a = int(input("Lütfen kontrol edilecek sayıyı giriniz : "))
toplam = 0
for i in range(1,a):
    if a % i == 0:
        toplam += i

if toplam == a:
    print("Girmiş olduğunuz sayı mükemmeldir.")
else:
    print("Girmiş olduğunuz sayı mükemmel değildir.")
