print("""************************************
SAYININ FAKTORİYELİNİ BULAN PROGRAM 

ÇIKMAK İÇİN ==> 'q'

************************************
""")

while True:
    sayı = input("Faktoriyelini bulmak istediğiniz sayıyı giriniz : ")
    if sayı == 'q':
        print("TEKRAR BEKLERİZZ...")
        break
    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):
            print("FAKTORİYEL =",faktoriyel,"i =",i)
            faktoriyel *= i
        print("faktoriyel ==> ",faktoriyel)
