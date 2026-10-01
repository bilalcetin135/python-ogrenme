
# Tarih: 30.09.2026
# Bugünkü bilgim: float(), .lower().strip(), iç içe if, and / or

tip = input("şekil tipi (üçgen,dörtgen): ").lower().strip()



if tip == "dörtgen":
    a = float(input("1.kenar: "))
    b = float(input("2.kenar: "))
    c = float(input("3.kenar: "))
    d = float(input("4.kenar: "))

    if (a == b == c == d):
        print("kare")
    elif (a ==c) and (b ==d):
        print("dikdörtgen")
    else:
        print("sıradan dörtgen")
elif tip == "üçgen":
    a = float(input("1.kenar: "))
    b = float(input("2.kenar: "))
    c = float(input("3.kenar: "))
    if (a < b + c) and (b < a + c) and (c < a + b):
        if (a == b == c):
            print("eşkenar üçgen")
        elif (a == b) or (b == c) or (a == c):
            print("ikizkenar üçgen")
        else:
            print("sıradan üçgen")
    else:
        print("üçgen belirtmiyor")
else:
    print("geçersiz giriş")
