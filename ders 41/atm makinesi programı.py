print("""********************************
 ==> ATM MAKİNESİ PROGRAMI <==
 
 İşlemler : 
 1. işlem = bakiye sorgulama
 2. işlem = para yatırma 
 3. işlem = para çekme
 Programdan çıkmak için 'q' ya basınız
********************************
""")
bakiye = 1000 #biz bununu üzerinde işlemlerimizi gerçekleştireceğiz...

while True:
    işlem = input("Lütfen yapmak istediğiniz işlem numarasını giriniz : ")
    if işlem == "q":
        print("PROGRAM SONLANDIRILIYOR")
        break
    elif işlem == "1":
        print(bakiye)
    elif işlem == "2":
        yatırılan_tutar = int(input("lütfen yatırmak istediğiniz tutarı giriniz : "))
        bakiye = bakiye + yatırılan_tutar
        print("YENİ BAKİYE : ",bakiye)
    elif işlem == "3":
        çekilen_tutar = int(input("lütfen çekmek istediğiniz tutarı giriniz : "))
        if çekilen_tutar > bakiye:
            print("bakiyeniz yetersizdir...")
            continue
        bakiye = bakiye - çekilen_tutar
        print("YENİ BAKİYE : ",bakiye)
    else:
        print("girmiş olduğunuz işlem geçersizdir. ")