def mükemmelsayı(sayı):
    toplam = 0
    for i in range(1,1001):
        if sayı % i == 0:
            toplam += i
            if sayı == toplam:
                print("MÜKEMMEL: ", toplam)
for x in range(1,1001):
    mükemmelsayı(x)