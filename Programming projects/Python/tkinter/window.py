import tkinter
from cipher import (LETTERS,KEY,encrypt,decrypt)

### SETUP ###
window = tkinter.Tk()
window.title("Cool cipher")

### ENCRYPTION SETUP ###
title_encrypt = tkinter.Label(
    window,
    text = "encrypt",
    padx = 5,
    pady = 5
)

title_encrypt.place(
    anchor = "nw"
)

input_encrypt = tkinter.Text(
    window,
    height = 4,
    width = 32
)

input_encrypt.place(
    window,
    anchor = "ne"
)
window.mainloop()

