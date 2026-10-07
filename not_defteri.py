
# Tarih: 07.10.2026
# Bugünkü bilgim: sözlük listesi, while True menü, enumerate, pop, try / except, datetime


from datetime import datetime
notlar = []


while True:
    print("\n1. Not ekle")
    print("2. Notları listele")
    print("3. not sil")
    print("4. çıkış")


    secim = input("Seçiminiz: ")


    if secim == "1":
        baslik = input("Not başlığı: ")
        icerik = input("Not içeriği: ")
        tarih = datetime.now().strftime("%d.%m.%Y")

        yeni_not = { "baslik": baslik,"icerik": icerik,"tarih": tarih}
        notlar.append(yeni_not)

        print("Not eklendi!")

    elif secim == "2":
        if len(notlar) == 0:
            print("Henüz not yok")
        else:
            for numara, n in enumerate(notlar,start=1):
                print(f"{numara}. {n['baslik']} ({n['tarih']})")
                print(f"   {n['icerik']}")
        
    elif secim == "3":
        if len(notlar) == 0:
            print("Silinecek not yok")
        else:
            for numara, n in enumerate(notlar, start=1):
                print(f"{numara}. {n['baslik']}")

            try:
                silinecek = int(input("Silinecek not numarası: "))
                if 1 <= silinecek <= len(notlar):
                    silinen = notlar.pop(silinecek - 1)
                    print(f"'{silinen['baslik']}' silindi!")
                else:
                    print("Böyle bir numara yok!")
            except ValueError:
                print("Lütfen sayı giriniz")
        
    elif secim == "4":
        print("GÜLE GÜLE!")
        break
    else:
        print("Geçersiz seçim")