print("ax^2 + bx + c denkleminin köklerini bulan program :  ")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("X1 : {}\nX2 : {}\n".format(x1,x2))