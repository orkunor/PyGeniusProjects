print("""
***********************************
   ==>  ATM'YE HOŞGELDİNİZ  <==    
***********************************

BAKİYE SORGULAMAK İÇİN    : 1
HESABA PARA YATIRMAK İÇİN : 2
HESAPTAN PARA ÇEKMEK İÇİN : 3

SİSTEMDEN AYRILMAK İÇİN   : 'q'
""")


bakiye = 1000

while True:
    seçim = input("ATM'DE YAPMAK İSTEDİĞİNİZ İŞLEMİ GİRİNİZ :")

    if seçim == "1":
        print("HESAP BAKİYENİZ :",bakiye)
    elif seçim == "2":
        eklenecek = int(input("HESABA EKLENECEK TUTAR:"))
        bakiye = bakiye + eklenecek
        print("YENİ BAKİYENİZ:",bakiye)
    elif seçim == "3":
        çekilecek = int(input("ÇEKİLECEK TUTAR :"))
        if bakiye >= çekilecek:
            print("İŞLEMİNİZ GERÇEKLEŞTİRİLİYOR...")
            bakiye -= çekilecek
            print("YENİ BAKİYENİZ :",bakiye)
        else:
            print("YETERSİZ BAKİYE")
    elif seçim == "q":
        print("SİSTEMDEN AYRILIYOR...")
        break
    else:
        print("HATALI VERİ GİRİŞİ LÜTFEN TEKRAR GİRİNİZ ==>  \n")
        continue