def not_hesapla(satır):

    satır = satır[:-1] #yöntemlerden biri de bu !!!

    liste = satır.split(",")

    isim = liste[0]

    not1 = int(liste[1])
    not2 = int(liste[2])
    final = int(liste[3])
    son_not = not1 * 0.3 + not2 * 0.3 + final * 0.4

    if son_not >= 90:
        harf = "AA"
    elif son_not >= 85:
        harf = "BA"
    elif son_not >= 80:
        harf = "BB"
    elif son_not >= 75:
        harf = "CB"
    elif son_not >= 70:
        harf = "CC"
    elif son_not >= 65:
        harf = "DC"
    elif son_not >= 60:
        harf = "DD"
    elif son_not >= 55:
        harf = "FD"
    else:
        harf = "FF"

    return isim + "============>" + harf + "\n"



with open("dosya.txt","r",encoding = "utf-8") as file:

    eklenecekler_listesi = list()

    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("notlar.txt", "w", encoding = "utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)