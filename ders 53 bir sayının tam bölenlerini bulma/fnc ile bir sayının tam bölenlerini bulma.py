def tam_bölen(sayı):
    liste = list()
    for i in range(1,sayı+1):

        if sayı % i == 0 :
            liste.append(i)
    return liste


while True:
    a = input("Lütfen sayınızı giriniz (çıkmak için 'q'): ")
    if a == "q":
        break
    else:
        print(tam_bölen(int(a)))













