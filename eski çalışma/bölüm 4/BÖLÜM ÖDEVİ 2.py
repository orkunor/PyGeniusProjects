print("""
*****************************
-----BÜYÜK SAYIYI BULMA-----
*****************************
""")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a > b and a > c:
    print(" EN BÜYÜK : a")
elif b > a and b > c:
    print("EN BÜYÜK : b")
elif c > a and c > b:
    print("EN BÜYÜK : c")
else:
    print("HATALI VERİ... ")






