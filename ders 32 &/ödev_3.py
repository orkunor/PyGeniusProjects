"""
Kullanıcının girdiği vize1,vize2,final notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""

print("""
*************************************************
===> VİZE NOTU HESAPLAMA PROGRAMI <===
*************************************************
""")

vize1 = int(input("Lütfen birinci vize notunuzu giriniz : "))
vize2 = int(input("Lütfen ikinci vize notunuzu giriniz : "))
final = int(input("lütfen final notunuzu giriniz : "))

toplam_not = vize1*0.3 + vize2*0.3 + final*0.4

if toplam_not >= 90:
    print("NOTUNUZU : AA")
elif 90 > toplam_not >= 85:
    print("NOTUNUZ : BA")
elif 85 > toplam_not >= 80:
    print("NOTUNUZ : BB")
elif 80 > toplam_not >= 75:
    print("NOTUNUZ : BC")
elif 75 > toplam_not >= 70:
    print("NOTUNUZ : CC")
elif 70 > toplam_not >= 65:
    print("NOTUNUZ : DC")
elif 65 > toplam_not >= 60:
    print("NOTUNUZ : DD")
elif toplam_not < 60 :
    print("NOTUNUZ : DD")
else :
    print("Girmiş olduğunuz notlar geçersizdir...")
print("program sonlandırılıyor")