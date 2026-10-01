
# Tarih: 29.09.2026
# Bugünkü bilgim: fonksiyonlar (def, return), sum/len, for + range, append, round


# def not_ortalamasi(a,b,c):
#     return (a + b + c) / 3


# sonuc = not_ortalamasi(45,8,66)

# if (sonuc<50):
#     print("KALDI")
# else:
#     print("GEÇTİ")


# print(sonuc)




# def not_ortalamasi(notlar):
#     return sum(notlar)/ len(notlar)

# sonuc = not_ortalamasi([44,88,77])

# if sonuc <50 :
#     print("KALDI")
# else:
#     print("GEÇTİ")


# print(int(sonuc))



# def not_ortalamasi(notlar):
#     return sum(notlar)/ len(notlar)

# sonuc = not_ortalamasi([44,88,77])

# if sonuc <50 :
#     print("KALDI")
# else:
#     print("GEÇTİ")


# print(int(sonuc))





def not_ortalamasi(notlar):
    return sum(notlar)/ len(notlar)

adet = int(input("Kaç Not Gireceksin? "))
notlar = []

for i in range(adet):
    not_degeri =int(input("Not gir: "))
    notlar.append(not_degeri)

sonuc = not_ortalamasi(notlar)
print("Ortalama:",round(sonuc,2))

if sonuc <50 :
    print("KALDI")
else:
    print("GEÇTİ")





