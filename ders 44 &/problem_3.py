"""
1'den 10'a kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin
"""
print("""****************************
   ==> ÇARPIM TABLOSU <==    
****************************
""")
for i in range(1,11):
    for j in range(1,11):
        print("{} x {} = ".format(i,j),i*j)