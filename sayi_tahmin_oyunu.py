
# Tarih: 28.09.2026
# Bugünkü bilgim: import random, for-else, break, f-string

import random

print("sayı tahmin oyununa hoşgeldiniz")
print("1 ile 100 arasında bir sayı tuttum bakalım bilecek misin")

tuttulan_sayi =random.randint(1,100)
tahmin_hakki = 5


for hak in range(tahmin_hakki):
    print(f'kalan tahmin hakkın : {tahmin_hakki - hak}')
    tahmin =int(input("TAHMİN: "))



    if (tahmin < tuttulan_sayi):
        print("daha yüksek bir sayı söylemelisin")
    elif (tahmin > tuttulan_sayi):
        print("daha küçük bir sayı söylemelisin")
    else:
        print("TEBRİKLER DOĞRU BİLDİN")
        print("OYUN BİTTİ")
        break
else:
    print(F'KAYBETTİN TAHMİN HAKKIN KALMADI : DOĞRU SAYI {tuttulan_sayi}')




