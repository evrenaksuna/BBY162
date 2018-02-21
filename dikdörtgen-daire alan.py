#dikdörtgen alan
def dortgen_alan_hesapla_vl(a,b):
    alan = a*b
    print("alan=", alan)
a = int(input("Dikdörtgenin kısa kenarı:"))
b = int(input("Dikdörtgenin uzun kenarı:"))
dortgen_alan_hesapla_vl(a,b)


#daire alan
yaricap = int(input("Dairenin yarıçapı="))
r = yaricap
pisayisi = 3.14
alan = pisayisi*(r**2)
print("Dairenin alanı=", alan)
