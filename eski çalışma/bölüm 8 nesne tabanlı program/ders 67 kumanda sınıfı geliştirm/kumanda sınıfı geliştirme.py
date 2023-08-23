import random
import time

class Kumanda():

    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def __str__(self):
        return "Tv Durumu : {}\nSes: {}\nKanallar: {}\nŞu anki kanal: {}\n".format(self.tv_durum, self.tv_ses,self.kanal_listesi, self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)


    def tv_aç(self):

        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık ....")
        else:
            print("Televizyon açılıyor ....")
            self.tv_durum = "Açık"

    def tv_kapat(self):

        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı ....")
        else:
            print("Televizyon kapanıyor ....")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):

        while True:
            cevap = input("Sesi azalt '<'\nSesi arttır '>'\nÇıkış : 'exit' ")

            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("SES DÜZEYİ:",self.tv_ses)
            elif cevap == ">":
                if self.tv_ses != 31:
                    self.tv_ses += 1
                    print("SES DÜZEYİ:",self.tv_ses)
            else:
                print("SES GÜNCELLENDİ:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor....")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal eklendi....")

    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)

        self.kanal = self.kanal_listesi[rastgele]
        print("Kanal:",self.kanal)







kumanda = Kumanda()


print("""
****************************************
         TELEVİZYON UYGULAMASI

1. İŞLEM ==> Tv Aç 

2. İŞLEM ==> Tv Kapat

3. İŞLEM ==> Ses Ayarları 

4. İŞLEM ==> Kanal Ayarları 

5. İŞLEM ==> Kanal Sayısını Öğrenme 

6. İŞLEM ==> Rastgele Kanala Geçme 
 
7. İŞLEM ==> Televizyon Bilgileri 

Çıkmak için 'q' 
 
****************************************
""")

while True:
    işlem = input("İşlemi Seçiniz:")

    if işlem == "q":
        print("Program sonlandırılıyor...")
        time.sleep(1)
        break
    elif işlem == "1":
        kumanda.tv_aç()
    elif işlem == "2":
        kumanda.tv_kapat()

    elif işlem == "3":
        kumanda.ses_ayarları()

    elif işlem == "4":
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif işlem == "5":

        print("Kanal Sayısı:",len(kumanda))

    elif işlem == "6":
        kumanda.rastgele_kanal()

    elif işlem == "7":
        print(kumanda)

    else:
        print("Geçersiz İşlem")