def dortgen_alan_hesapla_vl(a,b):
    alan = a*b
    print("alan=", alan)
a = int(input("Dikdörtgenin kısa kenarı:"))
b = int(input("Dikdörtgenin uzun kenarı:"))
dortgen_alan_hesapla_vl(a,b)

def daire_alan_hesapla_v1(pisayisi,r):
    alan = pisayisi*(r**2)
    print("alan=", alan)
pisayisi= 3.14
r= int(input("Dairenin yarıçapı="))
daire_alan_hesapla_v1(pisayisi,r)

def dortgen_alan_hesapla_v2(a,b):
    alan = a**2 * b**2
    print("alan=", alan)
a = int(input("Dikdörtgenin kısa kenarı:"))
b = int(input("Dikdörtgenin uzun kenarı:"))
dortgen_alan_hesapla_v2(a,b)

def daire_alan_hesapla_v2(pisayisi,r):
    alan = pisayisi * (r**2)**2
    print("Dairenin alanı=", alan)
pisayisi = 3.14
r = int(input("Dairenin yarıçapı="))
daire_alan_hesapla_v2(pisayisi,r)
