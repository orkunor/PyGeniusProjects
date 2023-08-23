print("""
************************************************************
KULLANICIDAN ALINAN SAYININ FAKTORİYELİNİ HESAPLAYAN PROGRAM
************************************************************
""")

#bir sayının faktoriyeli hesaplamak için bir listenin içerisinde dolaşıp bunları sırayla çarpmalıyız!!!

sayı = int(input("FAKTORİYELİNİ BULMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ : "))
faktoriyel = 1
for i in range(2,sayı+1):
    faktoriyel *= i
print("FAKTORİYEL:",faktoriyel)