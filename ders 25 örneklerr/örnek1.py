"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
 Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

"""
print("<== Please enter three numbers ==>")

a = int(input("first number :"))
b = int(input("Second number : "))
c = int(input("Third number : "))

sayilar = [a,b,c]

print("YOU FİRST NUMBER YOU ENTERED : {}\nSECOND NUMBER : {}\nTHIRD NUMBER : {} ".format(sayilar[0],sayilar[1],sayilar[2]))

y = a*b*c

i = [y]

print("Girmiş olduğunuz sayiların çarpımı : {}".format(i[0]))