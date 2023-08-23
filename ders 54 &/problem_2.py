"""
Kullanıcıdan 2 tane sayı alarak bu sayıların
en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;
"""
print("""***********************
  ==>EBOB PROGRAMI<==
***********************
""")
def ebob_fonk(sayı1,sayı2):
    i = 1 # bu sayıyı sürekli olarak arttırıp en büyük aynı anda ikisini de böleni bulmaya çalışıyoru
    ebob = 1 # bu bizim ebob değerimiz

    while i <= sayı1 and i <=sayı2: # i'nin bu döngüye girmesi için küçük olması lazım çünkü ikisini de bölen bir sayı arıyoruz
        if sayı1 % i == 0 and sayı2 % i == 0:
            ebob = i #ebob 'i'ye eşit oldu çünkü her ikisini de aynı anda bölünebiliyor...
        i += 1 # i'yi 1 arttırıyoruz çünkü aynı anda bölen en büyük ortak katı arıyoruz dikkat et...
    return ebob

sayı1 = int(input("Lütfen birinci sayıyı giriniz : "))
sayı2 = int(input("Lütfen ikinci sayıyı giriniz : "))

print("EBOB : ",ebob_fonk(sayı1,sayı2))