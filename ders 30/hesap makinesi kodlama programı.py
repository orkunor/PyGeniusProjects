print("<============ HESAP MAKİNESİ PROGRAMI ============>")

a = input("Lütfen yapmak istediğiniz işlemin sembolünü giriniz : ")
b = int(input("Lütfen birinci sayıyı giriniz : "))
c = int(input("Lütfen ikinci sayıyı giriniz : "))


if a == "+":
    print("Yapmak istediğiniz işlem : TOPLAMA")
    print("",b+c)
elif a == "-":
    print("Yapmak istediğiniz işlem : ÇIKARTMA")
    print("", b - c)
elif a == "*":
    print("Yapmak istediğiniz işlem : ÇARPMA")
    print("", b * c)
elif a == "/":
    print("Yapmak istediğiniz işlem : BÖLME")
    print("", b / c)
else:
    print("Geçersiz işlem girdiniz....")

print("Bizi tercih ettiğiniz için teşekkür ederiz :)")









