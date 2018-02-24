#saniyeyi dk,sa,gun vs çeviren
def timechanger(zaman):
    if zaman < 60:
         print("zaman :%d saniye"%(zaman))
    elif 60<=zaman<3600:
         dakika = zaman/60
         saniye = zaman%60
         print("zaman :%d dakika %d saniye"%(dakika ,saniye))
    elif  3600<=zaman<=86400:
        saat = zaman/3600
        zaman = zaman -saat*3600
        dakika = zaman/60
        saniye = zaman%60
        print("zaman :%d saat %d dakika %d saniye"%(saat,dakika ,saniye))
    elif 86400<=zaman<=604800:
        gun = zaman/86400
        saat = zaman/3600
        zaman = zaman -saat*3600
        saat = zaman%3600
        dakika = zaman/60
        saniye = zaman%60
        print("zaman :%d gun %d saat %d dakika %d saniye" % (gun, saat, dakika, saniye))
    elif 604800<=zaman<=2592000:
        hafta = zaman/ 604800
        gun = zaman/ 86400
        saat = zaman/ 3600
        zaman = zaman -saat * 3600
        gun=zaman%86400
        saat = zaman%3600
        dakika = zaman / 60
        saniye = zaman % 60
        print("zaman :%d hafta %d gun %d saat %d dakika %d saniye" % (hafta, gun, saat, dakika, saniye))
    elif 2592000<=zaman<=31556926:
        ay = zaman / 2592000
        hafta = zaman / 604800
        gun = zaman / 86400
        saat = zaman / 3600
        zaman = zaman - saat * 3600
        gun = zaman % 86400
        saat = zaman % 3600
        dakika = zaman / 60
        saniye = zaman % 60
        ay= zaman%2592000
        print("zaman :%d ay %d hafta %d gun %d saat %d dakika %d saniye" % (ay, hafta, gun, saat, dakika, saniye))

    else:
        print("geçerli bir zaman gir.")
while True:
    ten=input("dönüştürmek istediğin zamanı saniye cinsinden gir:")
    if ten.isdigit():
        break
ten=int(ten)
timechanger(ten)
