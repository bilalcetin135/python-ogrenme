
# Tarih: 30.09.2026
# Bugünkü bilgim: float(), f-string, işlem önceliği (parantez), if / elif / else

print("MERHABA VUCUT KİTLE ENDEKSİ HESAPLAMAYA HOŞ GELDİNİZ")
print("\n")
print("UYARI!! : BOY BİLGİNİZİ GİRERKEN METRE CİNSİNDEN GİRİNİZ")

isim = input("adınız: ")
boy = float(input("boyunuz: "))
kilo = float(input("kilonuz: "))


bki = kilo / (boy * boy)

if (bki < 18.5):
    print(f"{isim} vucut kitle endeksin {bki:.2f} hesaplamalar sonucu zayıfsın")
elif (bki >= 18.5) and (bki <25):
    print(f"{isim} vucut kitle endeksin {bki:.2f} hesaplamalar sonucu normalsin")
elif (bki >= 25) and (bki <30):
    print(f"{isim} vucut kitle endeksin {bki:.2f} hesaplamalar sonucu fazla kilolusun")
else:
    print(f"{isim} vucut kitle endeksin {bki:.2f} hesaplamalar sonucu obezsin")