print("""
***********************************
-----GEOMETRİK ŞEKİL HESAPLAMA-----
***********************************
""")
veri = input("ÜÇGEN mi yoksa DÖRTGEN mi istediğinizi giriniz : ")

if veri == "üçgen":
    print("üçgenin kenarlarını giriniz : ")
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    if a == b == c:
        print("EŞKENAR ÜÇGEN")
    elif a == b or b == c or a == c:
        print("İKİZKENAR ÜÇGEN")
    else:
        print("SIRADAN ÜÇGEN")
elif veri == "dörtgen":
    print("dörtgenin kenarlarını giriniz : ")
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    d = int(input("d:"))
    if a == b == c == d:
        print("KARE")
    elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        print("DİKDÖRTGEN")
    else:
        print("NORMAL DÖRTGEN")
else:
    print("Girilen veri yanlış")