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
def tab1():

    #DRUGA STRONA GRY
    def tab2():
        label1.destroy()
        button1.destroy()
        button2.destroy()
        label2 = Label(window, image = choose_your_fighter_img)
        label2.pack(pady=10)
        options = [
        "Wrogowie Studentów",
        "Paliwo Studenta",
        "Energetyki"
        ]
        clicked = StringVar()
        clicked.set(options[0])

        drop =  OptionMenu(window, clicked, *options)
        drop.pack(pady=20)

        button3 = Button(window, text = "OK")
        button3.pack(pady=10)


        def tab3():
            label2.destroy()
            button2.destroy()
            label1.destroy()
            button1.destroy()
            tab1()

    #CZĘŚĆ DALSZA PIERWSZEJ STRONY GRY
    label1 = Label(window, image=logo_img)
    label1.pack(pady=10)

    button1 = Button(window, image = noc_przed_img,command=tab2)
    button1.pack(pady=10)

    button2 = Button(window, image = bez_spiny_img,command=tab2)
    button2.pack(pady=10)


tab1()
window.mainloop()
