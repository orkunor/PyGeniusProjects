"""
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik.
Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları
bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz.
Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur.
Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.


İpucu: Basit düşünmeye çalışın.
"""

print("""
***********************************************
  ==> ÇİFT SAYILARI LİSTEYE ATMA PROGRAMI <==
***********************************************
""")
liste1 = range(1,100)
liste2 = list()

liste2 = [i for i in liste1 if i%2==0] #if bloğunu for döngüsünden sonra koymamız gerek ki işlemleri yapabilsin...

print(liste2)