from tkinter import *
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from tkinter import messagebox

pencere = Tk()
pencere.geometry("900x600+150+50")
pencere.title("Fotoğraf Albümü")
pencere.configure(background="maroon")
hosgeldin = Label(text="\n\n\t\t Fotoğraf Albümüne Hoşgeldin! \t\t\n\n", font="Times 18 bold",
                  fg="black", bg="maroon")
hosgeldin.pack()


def ekranaYaz():
    pencere1 = Tk()
    pencere1.geometry("900x600+200+150")
    baslik1 = pencere1.title("Tool")
    pencere1.configure(background="gray")


buton1 = Button(text="Tool", command=ekranaYaz, font="times 15 bold", fg="red", bg="black")
buton1.pack()


def ekranaYaz():
    pencere2 = Tk()
    pencere2.geometry("900x600+200+150")
    baslik2 = pencere2.title("Witchcraft")
    pencere2.configure(background="gray")


buton2 = Button(text="Witchcraft", command=ekranaYaz, font="Times 15 bold", fg="red", bg="black")
buton2.pack()
mainloop()
