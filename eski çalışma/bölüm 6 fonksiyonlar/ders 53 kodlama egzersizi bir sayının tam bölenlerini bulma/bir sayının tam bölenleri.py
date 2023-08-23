def tambölen(sayı):
    tambölenler = list()

    for i in range(2,sayı):
        if sayı % i == 0:
            tambölenler.append(i)
    return tambölenler

while True:
    sayı = input("SAYINIZI giriniz çıkmak için -q- tıklayınız: ")

    if sayı == "q":
        print("program sonlandırlıyor...")
        break
    else:
        sayı = int(sayı)
        print(tambölen(sayı))

