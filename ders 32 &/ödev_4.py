"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım.
İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi ,
dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı ,
eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın.
Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak.
Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz.
Kullanımı şu şekildedir ;

abs(-4) = 4
abs(7) = 7
"""

a = input("Lütfen istediğiniz şeklin geometrik ismini giriniz : ")

if a == "dörtgen":
    print("şimdi ise daha iyi analiz yapabilmek için kenarları lütfen teker teker giriniz => ")
    b = int(input("1. kenar : "))
    b2 = int(input("2. kenar : "))
    b3 = int(input("3. kenar : "))
    b4 = int(input("4. kenar : "))
    if b == b2 and b == b3 and b == b4:
        print("Dörtgeniniz KAREDİR")
    elif b == b2 and b3 == b4 and b != b3 and b2 != b4:
        print("Dörtgeniniz DİKDÖRTGENDİR....")
    elif b == b3 and b2 == b4 and b != b2 and b3 != b4:
        print("Dörtgeniniz DİKDÖRTGENDİR...")
    elif b == b4 and b2 == b3 and b != b2 and b != b3 and b4 != b2:
        print("Dörtgeniniz DİKDÖRTGENDİR...")
    else:
        print("sıradan bir dörtgen")
elif a == "üçgen":
    print("Üçgeninizi analiz edebilmek için lütfen kenar uzunluklarını giriniz : ")
    c = int(input("1. kenar : "))
    c2 = int(input("2. kenar : "))
    c3 = int(input("3. kenar : "))
    if c2 + c3 > c > abs(c2 - c3) or c2 + c > c3 > abs(c2 - c ) or c + c3 > c2 > abs(c - c3):
        print("Üçgen oluşturmaktadır")
        if (c == c2 and c != c3) or (c == c3 and c != c2 and c3 != c2) or (c2 == c3 and c2 != c and c3 != c):
            print("İKİZKENAR ÜÇGEN")
        elif c == c2 and c == c3 :
            print("EŞKENAR ÜÇGEN")
        else:
            print("çeşitkenar üçgen ")
    else:
        print("bilgileri verilen kenarlar herhangi bir üçgen oluşturmamaktadır...")
else:
    print("GİRMİŞ OLDUĞUNUZ BİLGİLER GEÇERSİZDİR...")


print("Program sonlandırılıyor...")