"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
a = int(input("Lütfen birinci sayıyı giriniz : "))

b = int(input("Lütfen ikinci sayıyı giriniz : "))

c = int(input("Lütfen üçüncü sayıyı giriniz : "))

if a > b and a > c:
    print("EN BÜYÜK SAYI : ",a)
elif b > c and b > a:
    print("EN BÜYÜK SAYI : ",b)
elif c > b and c > a:
    print("EN BÜYÜK SAYI : ",c)
else:
    print("EN BÜYÜK SAYI YOK ")
print("program sonlandırılıyor")