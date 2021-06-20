from string import ascii_lowercase
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import random

window = tk.Tk()
window.title("Hangman")
window.resizable(0, 0)


polish_letters = ('ąęśćóźż')
imported_alphabet = ascii_lowercase
alphabet ="".join(polish_letters)
alphabet2="".join(ascii_lowercase)

n = 0
for c in alphabet:
  Button(window, text=c, command= lambda c=c:
  guess(c), font= ("Comic Sans MS", 18),
  width=4).grid(row=1+n//9, column=n%9)
  n+=1
for d in alphabet2:
  Button(window, text=d, command= lambda d=d:
  guess(d), font= ("Comic Sans MS", 18),
  width=4).grid(row=1+n//9, column=n%9)
  n+=1


window.mainloop()
