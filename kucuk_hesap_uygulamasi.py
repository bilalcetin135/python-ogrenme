
# Tarih: 09.10.2026
# Bugünkü bilgim: sınıflar (class), __init__, self, metotlar, __str__


class Hesap:

    def __init__(self, sahip, bakiye):

        self.sahip = sahip
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        self.bakiye += miktar


    def para_cek(self,miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            print("Para Çekme İşleminiz tamamlandı")
        else:
            print("Hesap Bakiyeniz Yetersiz" )

    def __str__(self):
        return (f"{self.sahip}'in bakiyesi: {self.bakiye} TL")
    
hesap1 = Hesap("bilal",1000)
hesap1.para_yatir(500)
hesap1.para_cek(200)
hesap1.para_cek(5000)
print(hesap1)      
        
