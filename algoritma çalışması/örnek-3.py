"""
13195'in asal çarpanları 5, 7, 13 ve 29'dur.


600851475143 sayısının en büyük asal çarpanı nedir
"""
print("""*************************************
  ==>ASAL ÇARPAN BULMA PROGRAMI<==  
  
-> programdan çıkmak inin : '0'
*************************************
""")



while True:
    c = input("Lütfen asal çarpanlarını aradığınız sayıyı giriniz(EXIT:0) : ")
    a = int(c)
    d = 1
    liste = list()
    liste2 = list()
    if a == 0:
        print("Program sonlandırılıyor...")
        break
    else:
        for j in range(1,a):
            if a%j == 0:
                liste2.append(j)
                d+=1
            else:
                d+=1
    print("liste2:",liste2)

    for i in liste2:
        x = 1
        if i%x == 0   and i != 1:





