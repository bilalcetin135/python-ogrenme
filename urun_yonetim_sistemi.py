
# Tarih: 25.09.2026
# Bugünkü bilgim: sözlük, iç içe sözlük, liste, küme (set), add()

urunler ={
    100 : {
        "ad": "monitor",
        "kategori": "elektronik",
        "fiyatlar": [800, 944],
        "etiketler": {"kampanya", "yeni"}
    },
    101 : {
            "ad": "ssd",
            "kategori": "elektronik",
            "fiyatlar": [1500, 1770],
            "etiketler": {"hızlı", "stok"}
        },
    102 : {
            "ad": "klavye",
            "kategori": "aksesuar",
            "fiyatlar": [300, 354],
            "etiketler": {"yeni"}
        }    
}


# g1 = urunler[100]["fiyatlar"][1]
# g2 = urunler[101]["fiyatlar"][1]
# g3 = urunler[102]["fiyatlar"][1]

# en_buyuk = max(g1,g2,g3)

# print(en_buyuk)

urunler[102]["etiketler"].add("kampanya")
print(urunler[102]["etiketler"])



