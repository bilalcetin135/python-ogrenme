
# Tarih: 30.09.2026
# Bugünkü bilgim: aritmetik işlemler, ağırlıklı ortalama, if / elif, and

vize1 =int(input("vize 1:  "))
vize2 =int(input("vize 2:  "))
final =int(input("final:  "))

ortalama = (final*0.4) + (vize1*0.3) + (vize2*0.3)
ortalama = round(ortalama, 2)

if (ortalama>=90):
    print("Harf Notunuz: AA",ortalama)
elif (ortalama >=85 ) and (ortalama < 90):                                
    print("Harf Notunuz: BA",ortalama)                                                             
elif (ortalama >=80 ) and (ortalama < 85):
    print("Harf Notunuz: BB",ortalama)
elif (ortalama >=75 ) and (ortalama < 80):                                     
    print("Harf Notunuz: CB",ortalama)
elif (ortalama >=70 ) and (ortalama < 75):
    print("Harf Notunuz: CC",ortalama)                                                                          
elif (ortalama >=65 ) and (ortalama < 70):
    print("Harf Notunuz: DC",ortalama)
elif (ortalama >=60 ) and (ortalama < 65):
    print("Harf Notunuz: DD",ortalama)                                                                          
elif (ortalama >=50 ) and (ortalama < 60):
    print("Harf Notunuz: FD",ortalama)
elif (ortalama < 50 ):
    print("Harf Notunuz: FF",ortalama)


# Toplam Not >=  90 -----> AA                                                                       
# Toplam Not >=  85 -----> BA
# Toplam Not >=  80 -----> BB                                                                         
# Toplam Not >=  75 -----> CB
# Toplam Not >=  70 -----> CC                                                                         
# Toplam Not >=  65 -----> DC
# Toplam Not >=  60 -----> DD                                                                          
# Toplam Not >=  50 -----> FD
# Toplam Not <  50 -----> FF                                                                          
