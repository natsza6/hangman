from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image

#okienko gry
window = Tk()
window.geometry('600x600')
window.title('Stu(dying)')
window.config(bg = '#FFFFFF')

#logo
logo_img = ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/logo.png'))
logo = Label(window, image=logo_img)
logo.pack()

#wczytanie wszystkich grafik
noc_przed_img = ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/noc_przed.png'))
bez_spiny_img = ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/bez_spiny.png'))
choose_your_fighter_img = ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/choose_your_fighter.png'))

def Open_Menu():


    menu = Toplevel(window)
    menu.title("Stu(dying)")
    menu.geometry('600x600')
    logo = Label(menu, image=choose_your_fighter_img)
    logo.pack()

label = Label(window)
label.pack(pady=10)

#przyciski
button_noc_przed = Button(window, image=noc_przed_img, command=Open_Menu)
button_noc_przed.pack()

button_bez_spiny = Button(window, image=bez_spiny_img, command=Open_Menu)
button_bez_spiny.pack()




window.mainloop()

