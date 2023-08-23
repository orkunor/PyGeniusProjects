"""
->Kullanıcıdan aldığınız bir sayının
"Armstrong" sayısı olup olmadığını bulmaya çalışın.

->Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin
4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

->Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

a = input("Kontrol etmek istediğiniz sayıyı lütfen giriniz : ")
b = int(a)

if len(a) == 4:
    toplam = int(a[0])**4 + int(a[1])**4 + int(a[2])**4 + int(a[3])**4
    if toplam == b:
        print("Sayınız ARMSTRONG sayısıdır ")
    else:
        print("Maalesef Sayınız ARMSTRONG sayısı değildir ")
elif len(a) == 3:
    toplam1 = int(a[0]) ** 3 + int(a[1]) ** 3 + int(a[2]) ** 3
    if toplam1 == b:
        print("Sayınız ARMSTRONG sayısıdır ")
    else:
        print("Maalesef Sayınız ARMSTRONG sayısı değildir ")
elif len(a) == 2:
    toplam2 = int(a[0]) ** 2 + int(a[1]) ** 2
    if toplam2 == b:
        print("Sayınız ARMSTRONG sayısıdır ")
    else:
        print("Maalesef Sayınız ARMSTRONG sayısı değildir ")























