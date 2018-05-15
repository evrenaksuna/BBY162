import random
from tkinter import Tk, Label, Button

class felsefe:
    def __init__(self, anaSayfa):
        self.anaSayfa= anaSayfa
        anaSayfa.title=("Felsefi Sözler")

        self.label= Label(anaSayfa, text="--Felsefi Sözler--\nMerhaba!",font=("Arial",12),bg="light blue")
        self.label.pack()

        self.fel_butonu= Button(anaSayfa, text="Bilgiyi Görmek İçin Tıkla",font=("arial",11),command=self.gunun_bilgisi,bg="pink")
        self.fel_butonu.pack()

        self.kapat=Button(anaSayfa, text="Kapat",font=("arial",11),command= anaSayfa.quit,bg="brown")
        self.kapat.pack()

    def bilgi(self):
        print("Merhabalar!!!")

    def gunun_bilgisi(self):
        bilgiler=("Ben ışık olmaya, gecelerin susuzluğunu çekmeye ve yalnız olmaya mecburum. Friedrich Nietzsche","İnsanın ԁostu yoktur, saaԁetin dostu vardır. Napoléon Bonaparte", "Fayԁasız bir hayat erken bir ölümԁür. Johann Wolfgang von Goethe", "Yok etme ihtiyacının kesin nedeni, insan olmaktır, çünkü insan olmak nesne olmayı aşmak anlamına gelir. E. Fromm","Beni korkutan kötülerin baskısı değil iyilerin kayıtsızlığı. Martin Luther King")
        secilenBilgi=random.choice(bilgiler)
        self.bilgiler= Label(self.anaSayfa, text=secilenBilgi)
        self.bilgiler.pack()

root=Tk()
my_gui=felsefe(root)
root.mainloop()
