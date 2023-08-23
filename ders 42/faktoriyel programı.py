"""
girilen sayının faktoriyelini for döngüsüyle bulmaya çalışacağız...

-> for döngüsü kullanırız çünkü liste üzerinde gezineceğiz
"""

faktoriyel = int(input("lütfen faktoriyelini istediğiniz sayıyı giriniz : "))
çarpım = 1
liste = list(range(1,faktoriyel+1))

for i in liste:
    çarpım = çarpım * i
print("Faktoriyel : ",çarpım)