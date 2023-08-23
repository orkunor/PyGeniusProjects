def not_hesapla(satır):

    satır = satır[:-1]

    print(satır)


with open("dosya.txt","r",encoding = "utf-8") as file:

    for i in file:

        not_hesapla(i)




















































