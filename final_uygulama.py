import tkinter as tk
import random
from tkinter import *
from tkinter import Tk, Label, Button
from PIL import ImageTk,Image


class merhaba:
    def __init__(self, anasayfa):
        self.anasayfa = anasayfa
        anasayfa.geometry("500x750+100+0")
        anasayfa.title("Simon Hafıza Oyunu")
        anasayfa.configure(background="maroon")
        self.foto = Image.open("C:\\Users\\casper\\Desktop\\final_snoopy.jpg")
        self.tkimage = ImageTk.PhotoImage(self.foto)
        self.resim = Label(root, image=self.tkimage)
        self.resim.pack()
        buton1=Button(anasayfa, text="Nasıl Oynanır?", bg="black", fg="white", command=self.yardim).pack()

    def yardim(self):
        yardim = Tk()
        yardim.title("Nasıl Oynanır?")
        yardim.geometry("300x200+260+195")
        yardim.resizable(width=FALSE, height=FALSE)
        Label(yardim, text="\n\n*Yanan renklere sırayla tıkla \nve bunu sonsuza kadar yap.\n*Her doğru cevap 5 puan.\n*Bakalım oyunun sonunda puanını da \nhatırlayacak mısın?:}\nBaşarılar!\n\n", font="Times 13 bold", fg="black", bg="darkgoldenrod").pack()

class Simon:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, height=400, width=400)
        self.canvas.pack()
        self.dark = {"k": "darkred", "s": "darkgoldenrod", "y": "darkgreen", "m": "darkblue"}
        self.light = {"k": "red", "s": "goldenrod", "y": "green", "m": "blue"}

        self.squares = {"k": self.canvas.create_rectangle(0, 0, 200, 200, fill="darkred", outline="darkred"),
                        "s": self.canvas.create_rectangle(200, 0, 400, 200, fill="darkgoldenrod",
                                                          outline="darkgoldenrod"),
                        "y": self.canvas.create_rectangle(0, 200, 200, 400, fill="darkgreen",
                                                          outline="darkgreen"),
                        "m": self.canvas.create_rectangle(200, 200, 400, 400, fill="darkblue",
                                                          outline="darkblue")}

        self.ids = {v: k for k, v in self.squares.items()}
        self.high_score = 0
        self.status = tk.Label(root, text="OYUN BAŞLADI!\nGöremediysen rastgele bir renge tıkla.", font="Times 15 bold", fg="black", bg="maroon")
        self.status.pack()
        self.parent.bind("<h>", self.score)
        self.draw_board()

    def draw_board(self):
        self.pattern = random.choice("ksym")
        self.selections = ""
        self.parent.after(1000, self.animate)

    def animate(self, idx=0):
        c = self.pattern[idx]
        self.canvas.itemconfig(self.squares[c], fill=self.light[c], outline=self.light[c])
        self.parent.after(500, lambda: self.canvas.itemconfig(self.squares[c], fill=self.dark[c],
                                                              outline=self.dark[c]))

        idx += 1
        if idx < len(self.pattern):
            self.parent.after(1000, lambda: self.animate(idx))
        else:
            self.canvas.bind("<1>", self.select)

    def select(self, event=None):
        id = self.canvas.find_withtag("current")[0]
        color = self.ids[id]
        self.selections += color
        self.canvas.itemconfig(id, fill=self.light[color], outline=self.light[color])
        self.parent.after(800,
                          lambda: self.canvas.itemconfig(id, fill=self.dark[color], outline=self.dark[color]))

        if self.pattern == self.selections:
            self.canvas.unbind("<1>")
            self.status.config(text="DOĞRU! +5")
            self.parent.after(2000, lambda: self.status.config(text=""))
            self.pattern += random.choice("ksym")
            self.selections = ""
            self.high_score = max(self.high_score, len(self.pattern))
            self.parent.after(2000, self.animate)
        elif self.pattern[len(self.selections) - 1] != color:  # yanlış şeye tıklayınca
            self.canvas.unbind("<1>")
            self.status.config(text="YANLIŞ. HADİ BAŞTAN!")
            self.parent.after(2000, lambda: self.status.config(text=""))
            self.parent.after(2000, self.draw_board)

    def score(self, event=None):
        self.status.config(text=self.high_score)
        self.parent.after(2000, lambda: self.status.config(text=""))


root = tk.Tk()
merhaba = merhaba(root)
simon = Simon(root)
root.mainloop()

