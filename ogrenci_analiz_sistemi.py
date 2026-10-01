# Tarih: 24.09.2026
# bugünkü bilgim: listeler, iç içe listeler, max/min

ogr1 = ["bilal","cetin",22,95]
ogr2 = ["havva","düden",21,44]
ogr3 = ["hüseyin","celik",23,52]
ogr4 = ["barış","kara",22,75]
ogr5 = ["ayşe","tosun",21,66]
ogr6 = ["furkan","karabıçak",21,74]


ogrenciler =[ogr1,ogr2,ogr3,ogr4,ogr5,ogr6]


print("Ad:",ogrenciler[0][0], ogrenciler[0][1], "- Yaş:",ogrenciler[0][2]," Not:",ogrenciler[0][3])
print("Ad:",ogrenciler[1][0], ogrenciler[1][1], "- Yaş:",ogrenciler[1][2]," Not:",ogrenciler[1][3])
print("Ad:",ogrenciler[2][0], ogrenciler[2][1], "- Yaş:",ogrenciler[2][2]," Not:",ogrenciler[2][3])
print("Ad:",ogrenciler[3][0], ogrenciler[3][1], "- Yaş:",ogrenciler[3][2]," Not:",ogrenciler[3][3])
print("Ad:",ogrenciler[4][0], ogrenciler[4][1], "- Yaş:",ogrenciler[4][2]," Not:",ogrenciler[4][3])
print("Ad:",ogrenciler[5][0], ogrenciler[5][1], "- Yaş:",ogrenciler[5][2]," Not:",ogrenciler[5][3])


not1 = ogrenciler[0][3]
not2 = ogrenciler[1][3]
not3 = ogrenciler[2][3]
not4 = ogrenciler[3][3]
not5 = ogrenciler[4][3]
not6 = ogrenciler[5][3]

notlar = [not1,not2,not3,not4,not5,not6]

en_yuksek = max(notlar)
en_dusuk = min(notlar)

print("En Yüksek Not: ",en_yuksek)
print("En Düşük Not: ",en_dusuk)

ortalama = (not1 + not2 + not3 + not4 + not5 + not6) / 6
print("Sınıf Ortalaması:",ortalama)