# ikinci dereceden bir bilenmeyenli denklemin kökleri nasıl bulunur görelim ?
#delteyı hesaplamak için kullanıcıdan a,b,c değerlerini tek tek isteyerek ilerleyelim

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c"))

delta = b*b - 4*a*c

x1 = (- b - delta**(1/2) ) / (2 * a)
x2 = (- b + delta**(1/2)) / (2*a)

print("<== Denklemimizin kökleri ==>\n1. kök : {}\n2. kök : {}".format(x1,x2))






