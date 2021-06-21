from string import ascii_uppercase
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import random
from PIL import ImageTk, Image
from tkinter import ttk
import time


window = tk.Tk()
window.title("Stu(dying)")
window.geometry('600x600')
window.config(bg = '#FFFFFF')

polish_letters = ('ąęśćóźżłś')
imported_alphabet = ascii_uppercase
alphabet ="".join(polish_letters)
alphabet2="".join(ascii_uppercase)
numberOfGuesses = 0


word_list = ['EGOCENTRIC','FLAMBOYANT','AMBIGUOUS','AMBIVALENT','STOIC',
'EQUITY','BENEVOLENT','CHARISMA']


noc_przed_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\noc_przed.png'))
bez_spiny_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\3455.png'))
choose_your_fighter_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\kategorieimg.png'))
logo_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\logokurde2.png'))
win_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\win2.png'))

photos = [ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hang0.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman1.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman2.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman3.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman4.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman5.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman6.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman7.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman8.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman9.png')),
ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\hangman10.png'))]


def strona1():


    #DRUGA STRONA GRY
    def strona2():
        global label2, drop, button3
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
        clicked = tk.StringVar()
        clicked.set(options[0])


        drop =  OptionMenu(window, clicked, *options)
        drop.pack(pady=20)

        button3 = Button(window, text = "OK", command = lambda: strona3())
        button3.pack(pady=10)

        #TUTAJ BĘDZIE TRZECIA STRONA GRY - GRA WŁAŚCIWA
        def strona3():
            def newGame():

                global label2,  button3, drop
                global the_word_withSpaces
                global numberOfGuesses

                label2.destroy()
                button2.destroy()
                label1.destroy()
                button1.destroy()
                button3.destroy()
                drop.destroy()
                numberOfGuesses=0
                imgLabel.config(image=photos[0])
                the_word=random.choice(word_list)
                the_word_withSpaces=" ".join(the_word)
                lblWord.set(" ".join("_"*len(the_word)))

            def guess(letter):
                global the_word_withSpaces
                global numberOfGuesses
                if numberOfGuesses<10:
                    txt=list(the_word_withSpaces)
                    guessed=list(lblWord.get())
                if the_word_withSpaces.count(letter)>0:
                    for c in range(len(txt)):
                        if txt[c]==letter:
                            guessed[c]=letter
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                      messagebox.showinfo("Hangman","You guessed it!")

                else:
                    numberOfGuesses+=1
                    imgLabel.config(image=photos[numberOfGuesses])
                    if numberOfGuesses==10:
                      messagebox.showwarning("Stu(dying)","Przegrałeś/łaś z sesją! :(")
                      time.sleep(10)
                      return False

            imgLabel = Label(window)
            imgLabel.pack()
            imgLabel.config(image=photos[0])

            lblWord=StringVar()
            Label(window, textvariable=lblWord,
            font=("Consolas 24 bold")).pack()

            n = 0
            for c in alphabet:
                Button(window, text=c, command= lambda c=c:
                guess(c), font= ("Comic Sans MS", 10),
                width=3).pack()
                n+=1
            for d in alphabet2:
                Button(window, text=d, command= lambda d=d:
                guess(d), font= ("Comic Sans MS", 10),
                width=3).pack()
                n+=1



            newGame()


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
