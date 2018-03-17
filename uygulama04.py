kim = input("Erkek ismi giriniz:")
kiminle = input("Kadın ismi giriniz:")
mısra = input("Mısra sayısı giriniz:")
sec = int(mısra)
boşluk = " "
nerede = open("nerede.txt", "r")
neyaptı = open("yüklem.txt", "r")
import random
def kelime1():
    secim = random.choice(nerede)
    nerede.remove(secim)
    return secim
def kelime2():
    secim = random.choice(neyaptı)
    neyaptı.remove(secim)
    return secim

a=(kim+boşluk+kiminle+boşluk+kelime1()+boşluk+kelime2()+"\n")
b=(kim+boşluk+kiminle+boşluk+kelime1()+boşluk+kelime2()+"\n")
c=(kim+boşluk+kiminle+boşluk+kelime1()+boşluk+kelime2()+"\n")
d=(kim+boşluk+kiminle+boşluk+kelime1()+boşluk+kelime2()+"\n")
e=("\n")
f=(kim+boşluk+kiminle+boşluk+kelime1()+boşluk+kelime2()+"\n")
g=(kim+boşluk+kiminle+boşluk+kelime1()+boşluk+kelime2()+"\n")
h=(kim+boşluk+kiminle+boşluk+kelime1()+boşluk+kelime2()+"\n")
ı=(kim+boşluk+kiminle+boşluk+kelime1()+boşluk+kelime2()+"\n")

while True:
    if sec==1:
        print(e,a)
        print
    elif sec==2:
        print(e,a,b)
        print
    elif sec==3:
        print(e,a,b,c)
        print
    elif sec==4:
        print(e,a,b,c,d)
        print
    elif sec==5:
        print(e,a,b,c,d,e,f)
        print
    elif sec==6:
        print(e,a,b,c,d,e,f,g)
        print
    elif sec==7:
        print(e,a,b,c,d,e,f,g,h)
        print
    elif sec==8:
        print(e,a,b,c,d,e,f,g,h,ı)
        print
    else:
        print("Maximum mısra sayısını aştınız..")
    break
