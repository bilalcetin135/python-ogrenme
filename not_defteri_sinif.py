from datetime import datetime

class Not:

    def __init__(self, baslik, icerik):
        self.baslik = baslik
        self.icerik = icerik
        self.tarih = datetime.now().strftime("%d.%m.%Y")
        
    def __str__(self):
        return f"{self.baslik} ({self.tarih})"



class NotDefteri:
    def __init__(self):
        self.notlar = []

    def not_ekle(self,baslik,icerik):
        yeni_not = Not(baslik, icerik)
        self.notlar.append(yeni_not)


    def notlari_listele(self):
        if len(self.notlar) == 0:
            print("Henüz not yok")
        else:
            for numara, n in enumerate(self.notlar, start=1):
                print(f"{numara}. {n}")
            
    def not_sil(self, numara):
        if 1 <= numara <= len(self.notlar):
            self.notlar.pop(numara - 1)
            print("Not silindi")
        else:
            print( "Böyle bir numara yok")
            

defter = NotDefteri()

while True:
    print("\n1. Not ekle")
    print("2. Notları listele")
    print("3. Not Sil")
    print("4. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        baslik = input("Not başlığı: ")
        icerik = input("Not içeriği: ")
        defter.not_ekle(baslik, icerik)
        print("Not eklendi")
    elif secim == "2":
        defter.notlari_listele()
    elif secim == "3":
        defter.notlari_listele()
        try:
            numara = int (input("Silinecek not numarası: "))
            defter.not_sil(numara)
        except ValueError:
            print("Lütfen sayı giriniz")
    elif secim == "4":
        print("GÜLE GÜLE")
        break
    else:
        print("Geçersiz seçim")
    