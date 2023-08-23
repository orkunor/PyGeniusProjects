print("""***********************************
==== A.T.M. GİRİŞ PROGRAMI ==== 
***********************************

BAKİYE SORGULAMAK İÇİN  ==> 1
PARA YATIRMAK İÇİN      ==> 2
PARA ÇEKMEK İÇİN        ==> 3

SİSTEMDEN AYRILMAK İÇİN ==> 'q'
""")

bakiye = 1000 # sisteme kayıtlı para miktarımız

while True:
    işlem = input("İŞLEMİ GİRİNİZ : ")

    if işlem == 'q':
        print("DAHA SONRA TEKRAR BEKLERİZ...")
        break
    elif işlem == '1':
        print("HESAPTA BULUNAN BAKİYE : {}".format(bakiye))
    elif işlem == '2':
        yatırılan_tutar = int(input("YATIRMAK İSTEDİĞİNİZ TUTARI GİRİNİZ : "))
        bakiye += yatırılan_tutar
        print("YENİ BAKİYENİZ : ",bakiye)
    elif işlem == '3':
        çekilecek_tutar = int(input("ÇEKMEK İSTEDİĞİNİZ TUTARI GİRİNİZ : "))
        if çekilecek_tutar > bakiye:
            print("YETERLİ BAKİYE BULUNMAMAKTADIR LÜTFEN TEKRAR DENEYİNİZ...")
            continue
        bakiye = bakiye - çekilecek_tutar
        print("YENİ BAKİYENİZ : ",bakiye)
    else:
        print("GEÇERSİZ İŞLEM GİRİŞİ....")