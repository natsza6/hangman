from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image

#główne okienko gry
window = Tk()
window.geometry('600x600')
window.title('Stu(dying)')
window.config(bg = '#FFFFFF')

#wczytanie grafik
noc_przed_img = ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/noc_przed.png'))
bez_spiny_img = ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/bez_spiny.png'))
choose_your_fighter_img = ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/choose_your_fighter.png'))
logo_img = ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/logo.png'))

#PIERWSZA STRONA GRY
def strona1():

    #DRUGA STRONA GRY
    def strona2():
        label1.destroy()
        button1.destroy()
        button2.destroy()
        label2 = tk.Label(window, image = choose_your_fighter_img,
        borderwidth=0,compound="center",
        highlightthickness = 0,padx=0,pady=0)
        label2.pack(pady=10)
        options = ["Kategorie do wyboru",
        "Wrogowie Studentów",
        "Paliwo Studenta",
        "Energetyki"]
        clicked = StringVar()
        clicked.set(options[0])

        drop =  OptionMenu(window, clicked, *options)
        drop.pack(pady=20)

        button3 = Button(window, text = "OK")
        button3.pack(pady=10)

        #TUTAJ BĘDZIE TRZECIA STRONA GRY - GRA WŁAŚCIWA
        def strona3():
            label2.destroy()
            button2.destroy()
            label1.destroy()
            button1.destroy()
            strona1()

    #CZĘŚĆ DALSZA PIERWSZEJ STRONY GRY
    label1 = tk.Label(window, image=logo_img,
    borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    label1.pack(pady=10)

    button1 = tk.Button(window, image = noc_przed_img,
    command=strona2,borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    button1.pack(pady=10)

    button2 = tk.Button(window, image = bez_spiny_img,
    command=strona2,borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    button2.pack(pady=10)


strona1()
window.mainloop()
