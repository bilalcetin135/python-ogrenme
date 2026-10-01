 
# Tarih: 24.09.2026
# Bugünkü bilgim: input, int(), if / elif, karşılaştırma operatörleri, and


a = int(input("1.sayı     :"))
b = int(input("2.sayı     :"))
c = int(input("3.sayı     :"))

if (a >= b) and (a >= c):
    print("a en büyük sayı", a)
elif(b >= a) and (b >= c):
    print("b en büyük sayı", b)
elif (c >= a) and (c >= b):
    print("c en büyük sayı", c)