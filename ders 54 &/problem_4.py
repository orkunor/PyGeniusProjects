"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi
"""
liste1 = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
liste2 = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
def fonkiyon(a):
    liste = list()
    birinci = a%10 # bu şekilde birler basamağını bulduk
    ikinci = a // 10 #bu şekilde onlar basamğını bulduk
    return print("",liste1[ikinci],liste2[birinci])


sayı = int(input("Lütfen yazdırmak istediğiniz sayıyı giriniz : "))

fonkiyon(sayı)

# kendimiz yaptık => **********************************************************

birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"] #indexler
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"] #indexler

def okunuş(sayı):
    a = sayı % 10 #birler basamağı
    b = sayı // 10 #onlar basamağı
    return onlar[b],birler[a]

while True:
    sayı = int(input("Lütfen bir sayı giriniz : "))
    if sayı == 777:
        print("Program sonlandırılıyor...")
    else:
        print("",okunuş(sayı))