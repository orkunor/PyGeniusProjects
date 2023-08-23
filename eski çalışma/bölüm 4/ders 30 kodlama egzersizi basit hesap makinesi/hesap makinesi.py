print("""**********************************
HESAP MAKİNESİ PROGRAMI 

İşlemler : 

1. TOPLAMA işlemi 
2. ÇIKARTMA işlemi 
3. ÇARPMA işlemi 
4. BÖLME işlemi 
***********************************
""")

sayı1 = int(input("İlk sayıyı giriniz : "))
sayı2 = int(input("İkinci sayıyı giriniz : "))

işlem = input("Lütfen istediğiniz işlemi giriniz : ")

if işlem == "+":
    print("TOPLAMA işleminin sonucu = {}".format(sayı1+sayı2))
elif işlem == "-":
    print("ÇIKARTMA işleminin sonucu = {}".format(sayı1-sayı2))
elif işlem == "*":
    print("ÇARPMA işleminin sonucu = {}".format(sayı1*sayı2))
elif işlem == "/":
    print("BÖLME işleminin sonucu = {}".format(sayı1/sayı2))
else:
    print("GEÇERSİZ İŞLEM!!")

