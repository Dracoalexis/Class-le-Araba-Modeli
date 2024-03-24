class Araba:

    def __init__(self, araba_durumu="Kapalı", marka="", model="", renk="", araba_hızı=0):
        self.araba_durumu = araba_durumu
        self.marka = marka
        self.model = model
        self.renk = renk
        self.araba_hızı = araba_hızı

    def bilgileri_göster(self):
        print("""Arabanın bilgileri ve durumu:
              Markası: {}

              Modeli: {}

              Rengi: {}

              Anlık Durumu: {}

              Anlık Hız: {}
              """.format(self.marka, self.model, self.renk, self.araba_durumu, self.araba_hızı))

    def durum_değiştir(self):

        if self.araba_durumu == "Kapalı":
            print("Araba açılıyor...")
            self.araba_durumu = "Açık"

        else:
            if self.araba_hızı > 0:
                print("Araba hızı 0 olmadığı için kapatılamaz.")
            else:
                print("Araba kapatılıyor...")
                self.araba_durumu = "Kapalı"

    def hız_değştir(self):

        if self.araba_durumu == "Açık":

            hızlandırma = True

            while hızlandırma:
                sorgu = input(
                    "Arabanın hızını arttırmak için +, azaltmak için -'ye,hız değişimini bırakmak için q'ya basınız.")

                if sorgu == "+":
                    yeni_hız = int(input("Ne kadar hızlanmak istiyorsunuz ?"))
                    self.araba_hızı += yeni_hız
                    print("Anlık hızınız:{}".format(self.araba_hızı))

                elif sorgu == "-":
                    yeni_hız = int(input("Ne kadar yavaşlamak istiyorsunuz ?"))
                    self.araba_hızı -= yeni_hız

                    if self.araba_hızı <= 0:
                        print("Anlık Hız:{}".format(self.araba_hızı))
                        print("Hızınızı daha fazla düşüremezsiniz.")
                        self.araba_hızı = 0

                elif sorgu == "q":
                    hızlandırma = False
                else:
                    print("Geçersiz eylem girdiniz.")

        else:
            print("Araba kapalı olduğu için hızlanamaz.")


def main():
    print("Arabaya hoşgeldiniz. Lütfen gerekli bilgileri giriniz.")
    araba_markası = input("Arabanın markası:")
    araba_modeli = input("Arabanın modeli:")
    araba_rengi = input("Araba rengi:")

    araba1 = Araba("Kapalı", araba_markası, araba_modeli, araba_rengi, araba_hızı=0)

    while True:
        sorgu = input("""Yapmak istediğiniz işlemi seçiniz, çıkmak için q ya basınız(Araba hızı 0 değil ise q ya basamazsınız.):
            1- Bilgileri ve Durumu Göster:
            2- Arabayı Çalıştır/Kapat
            3- Hızı değiştir
            """)

        if sorgu == "1":
            araba1.bilgileri_göster()

        elif sorgu == "2":
            araba1.durum_değiştir()

        elif sorgu == "3":
            araba1.hız_değştir()

        elif sorgu == "q":
            if araba1.araba_hızı > 0:
                print("Arabanızın hızı 0 olmadığı için çıkış yapmazsınız.")

            else:
                print("Arabadan çıkış yapılıyor...İyi günler dileriz.")
                break

        else:
            print("Geçersiz eylem girdiniz...")
            return sorgu


main()



