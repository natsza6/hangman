win_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\win2.png'))
lose_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\lose_page.png'))
restart_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\wez_waruna.png'))
exit_img = ImageTk.PhotoImage(Image.open(r'C:\Users\ACER\Pictures\Screenshots\skoncz_ten_cyrk.png'))


def strona4_win():
    labelwin = tk.Label(window, image=win_img,
    borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    labelwin.pack(pady=10)

    button_restart = tk.Button(window, image = restart_img,
    command= lambda:strona1(),borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    button_restart.pack(pady=10)

    button_exit = tk.Button(window, image = exit_img,
    command=window.quit,borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    button_exit.pack(pady=10)

def strona4_lose():
    labelwin = tk.Label(window, image=lose_img,
    borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    labelwin.pack(pady=10)

    button_restart = tk.Button(window, image = restart_img,
    command= lambda:strona1(),borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    button_restart.pack(pady=10)

    button_exit = tk.Button(window, image = exit_img,
    command=window.quit,borderwidth=0,compound="center",
    highlightthickness = 0,padx=0,pady=0)
    button_exit.pack(pady=10)
