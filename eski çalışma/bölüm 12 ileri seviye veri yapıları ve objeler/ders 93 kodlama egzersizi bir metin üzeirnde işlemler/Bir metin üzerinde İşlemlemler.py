class Dosya():

    def __init__(self):
        with open("metin.txt","r",encoding = "utf-8") as file:
            dosya_içeriği = file.read()

            kelimeler = dosya_içeriği.split()

            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)

    def tüm_kelimeler(self):
        kelimeler_kümesi = set()

        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)

        print("Tüm Kelimeler....")

        for i in kelimeler_kümesi:
            print(i)
            print("**********************************")
    def kelime_frekans(self):
        kelime_sözlük = dict()

        for i in self.sade_kelimeler:
            if i in kelime_sözlük:
                kelime_sözlük[i] += 1
            else:
                kelime_sözlük[i] = 1

        for kelime,sayı in kelime_sözlük.items():
            print("{} kelimesi {} kadar geçiyor....".format(kelime,sayı))

            print("<<<<<<<<=================================>>>>>>>>")





dosya = Dosya()

dosya.kelime_frekans()


































