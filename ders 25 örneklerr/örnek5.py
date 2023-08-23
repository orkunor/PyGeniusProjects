"""

Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

a = int(input("Birinci sayıyı giriniz : "))
b = int(input("İkinci sayıyı giriniz : "))

a,b = b,a # bu kodla sayıların yerleri değişiyor...

print("{}\n{}".format(a,b))