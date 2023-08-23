"""
Fibonacci dizisindeki her yeni terim, önceki iki terimin eklenmesiyle oluşturulur.
1 ve 2 ile başlayarak ilk 10 terim şöyle olacaktır:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Değerleri dört milyonu geçmeyen Fibonacci dizisindeki terimleri dikkate alarak
çift değerli terimlerin toplamını bulunuz.
"""
a = 1
b = 1
liste = list()
toplam = 0
for i in range(1,50):
    a , b = b , a+b
    print(b)
    liste.append(b)
print(liste)
for j in liste:
    if j % 2 == 0:
        toplam += j
print("ÇİFT SAYILARIN TOPLAMI : ",toplam)