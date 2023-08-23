"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

"""
print("<=== Beden kitle indeksi bulma programı ===>")

a = int(input("Lütfen boyunuzu giriniz : "))
b = int(input("Lütfen kilonuzu giriniz : "))

print("Beden kitle endeksiniz : ",a / b**2)