"""
Kumanda çalışma sistemini class'ları kullanarak yapacağız...
"""
import random
import time


class Kumanda():

    def __init__(self,tv_durum = "KAPALI",tv_ses = 0,kanal_listesi = ["TRT1"],kanal = "TRT1"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_aç(self):#bu fonksiyon sayesinde tv'nin o anki durumu değişecek...

        if(self.tv_durum == "AÇIK"):
            print("TV zaten açık...")
        else:
            print("TV açılıyor...")
            self.tv_durum = "AÇIK"
    def tv_kapat(self):
        if self.tv_durum == "KAPALI":
            print("TV zaten kapalı")
        else:
            print("TV kapanıyor...")
            self.tv_durum = "KAPALI"
    def ses_ayarları(self):
        while True:
            cevap = input("Sesi azalt : (<)\nSesi arttır : (>)\n Çıkış : (exit)")

            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses : ",self.tv_ses)
            elif cevap == ">":
                if self.tv_ses != 31:
                    self.tv_ses += 1
                    print("Ses : ",self.tv_ses)
            else:
                print("Ses güncellendi : ",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(2)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi...")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)- 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal : ",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durumu : {}\nTV Ses : {}\nKanal Listesi : {}\nŞu Anki Kanal : {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda = Kumanda() #Kumanda() class'ından kumanda objesini oluşturduk ki kullanabilelim...
print("""
*********************************
      ==> TV UYGULAMASI <==

1. TV Aç

2. TV Kapat 

3. SES Ayarları 

4. Kanal Ekle 

5. Kanal Sayısını Öğrenme 

6. Rastgele Kanala Geçme 

7. TV Bilgileri 


Çıkmak İçin 'q' ya basınız 
*********************************
""")
while True:
    işlem = input("İşlemi Seçiniz : ")

    if işlem == "q":
        print("Program Sonlandırılıyor...")
        time.sleep(2)
        break
    elif işlem == "1":
        kumanda.tv_aç()
    elif işlem == "2":
        kumanda.tv_kapat()
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem == "4":
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz")
        kanal_listesi = kanal_isimleri.split(",") #split fonksiyonunu kullanarak virgül görünce program ayıracak

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif işlem == "5":
        print("Kanal sayısı : ",len(kumanda))
    elif işlem == "6":
        kumanda.rastgele_kanal()
    elif işlem == "7":
        print(kumanda)
    else:
        print("Geçersiz işlem.... ")

