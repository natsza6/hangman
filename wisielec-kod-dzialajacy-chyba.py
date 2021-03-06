from tkinter import messagebox
from tkinter import *
import random
from string import ascii_uppercase
import tkinter as tk
from PIL import ImageTk, Image


#Setting up the window
window = Tk()
window.title("Stu(dying)")
window.geometry('600x600')

#Words
word_list = ['EGOCENTRIC','FLAMBOYANT','AMBIGUOUS','AMBIVALENT','STOIC','EQUITY',
             'BENEVOLENT','CHARISMA']

photos = [ ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang0.png')), ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang1.png')),ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang2.png')),ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang3.png')),
          ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang4.png')),ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang5.png')),ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang6.png')),ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang7.png')),
          ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang8.png')),ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang9.png')),PhotoImage(file="/Users/mac/Desktop/images/hang10.png"),ImageTk.PhotoImage(Image.open('/Users/mac/Desktop/images/hang11.png'))]

def newGame():
  global the_word_withSpaces
  global numberOfGuesses
  numberOfGuesses=0
  imgLabel.config(image=photos[0])
  the_word=random.choice(word_list)
  the_word_withSpaces=" ".join(the_word)
  lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
  global numberOfGuesses
  if numberOfGuesses<11:
    txt=list(the_word_withSpaces)
    guessed=list(lblWord.get())
    if the_word_withSpaces.count(letter)>0:
      for c in range(len(txt)):
        if txt[c]==letter:
          guessed[c]=letter
        lblWord.set("".join(guessed))
        if lblWord.get()==the_word_withSpaces:
          messagebox.showinfo("Stu(dying)","Brawo, przetrwałeś/łaś sesję!")
          newGame()

    else:
        numberOfGuesses+=1
        imgLabel.config(image=photos[numberOfGuesses])
        if numberOfGuesses==11:
          messagebox.showwarning("Stu(dying)","Przegrałeś/łaś z sesją! :(")

imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady= 40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

n = 0
for c in ascii_uppercase:
  Button(window, text=c, command= lambda c=c: guess(c), font= ("Helvetica 18"),width=4).grid(row=1+n//12, column=n%12)
  n+=1

Button(window, text="Nowa\nGra", command=lambda:newGame(), font=("Helvetica 10 bold")).grid(row=3, column=2, sticky="NSWE")

newGame()
window.mainloop()
