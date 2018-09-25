#ui

import tkinter

def piano_set_up():
    window = tkinter.Tk()

    for col in range(21):
        window.columnconfigure(col, minsize=25, weight=1)
    for row in range(2):
        window.rowconfigure(row, minsize=100, weight=1)

    C = tkinter.Button (master = window, text = "C")
    C.grid(row = 0, column = 0, rowspan = 2, columnspan=3)
    D = tkinter.Button (master = window, text = "D")
    D.grid(row = 0, column = 3, rowspan = 2, columnspan=3)
    E = tkinter.Button (master = window, text = "E")
    E.grid(row = 0, column = 6, rowspan = 2, columnspan=3)
    F = tkinter.Button (master = window, text = "F")
    F.grid(row = 0, column = 9, rowspan = 2, columnspan=3)
    G = tkinter.Button (master = window, text = "G")
    G.grid(row = 0, column = 12, rowspan = 2, columnspan=3)
    A = tkinter.Button (master = window, text = "A")
    A.grid(row = 0, column = 15, rowspan = 2, columnspan=3)
    B = tkinter.Button (master = window, text = "B")
    B.grid(row = 0, column = 18, rowspan = 2, columnspan=3)

    Cs = tkinter.Button (master = window, text = "C#")
    Cs.grid(row = 0, column = 2, rowspan = 1, columnspan=2)
    Ds = tkinter.Button (master = window, text = "D#")
    Ds.grid(row = 0, column = 5, rowspan = 1, columnspan=2)
    Fs = tkinter.Button (master = window, text = "F#")
    Fs.grid(row = 0, column = 11, rowspan = 1, columnspan=2)
    Gs = tkinter.Button (master = window, text = "G#")
    Gs.grid(row = 0, column = 14, rowspan = 1, columnspan=2)
    As = tkinter.Button (master = window, text = "A#")
    As.grid(row = 0, column = 17, rowspan = 1, columnspan=2)

    white_keys = [C, D, E, F, G, A, B]
    black_keys = [Cs, Ds, Fs, Gs, As]

    for key in white_keys + black_keys:
        key.grid(sticky = 'news')
        key.configure(activebackground = '#ff0000', anchor = 's', pady = 10, font = ('helvetica', 15))

    for key in white_keys:
        key.configure(bg = '#ffffff', fg = '#000000')

    for key in black_keys:
        key.configure(bg = '#000000', fg = '#ffffff')

    window.mainloop()
