import tkinter as tk
from tkinter import font
style = {
    'bgColor': '#121212',
    'fgColor': 'white',
    'title': 'Music App',
    'buttonFont': {
        'family': 'tahoma',
        'size': 20
    }
}

root = tk.Tk()
root.configure(bg = style['bgColor'])
root.title(style['title'])
root.geometry('1000x550')
root.resizable(False, False)

def drawOpenScreen():
    opnBtn = tk.Button(root, text = 'Open File(s)', bg = style['bgColor'], fg = style['fgColor'],
                       font = font.Font(family = style['buttonFont']['family'], size = style['buttonFont']['size']),
                       padx = 90, pady = 20)
    opnBtn.place(anchor = 'center', relx = 0.5, rely = 0.5)

drawOpenScreen()
root.mainloop()
