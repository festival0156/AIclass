import tkinter as tk
from tkinter import font

root = tk.Tk()
root.geometry('1000x500')
root.configure(bg = '#121212')
root.title('ChatBot')

ttlLbl = tk.Label(root, text = 'Chat Bot', bg = '#121212', fg = 'white', bd = 2, pady = 0,
               padx = 0, justify = tk.CENTER, font = font.Font(family = '', size = 28))
ttlLbl.pack(side = tk.TOP, fill = tk.X)

cvnStv = tk.StringVar()
cvnLbl = tk.Label(root, bg = '#121212', fg = 'white', bd = 2, pady = 0, justify = tk.LEFT
                  padx = 0, font = font.Font(family = '', size = 14), textvariable = cvnStr)
cvnLbl.pack(side = tk.TOP, fill = tk.X)

def send():
    msg = inpStv.get()
    inpStv.set('')
    cvnStv.set(cvnStv.get() + '\n[<] ' + msg)
    msg = bot.get_response(msg).text
    cvnStv.set(cvnStv.get() + '\n[>] ' + msg)

inpStv = tk.StringVar()
inpFrm = tk.Frame(root, bg = 'white', bd = 2)
inpEnt = tk.Entry(inpFrm, textvariable = inpStv, bg = '#121212', fg = 'white', bd = 2, font = font.Font(family = '', size = 14), exportselection = False)
inpEnt.pack(side = tk.LEFT, fill = tk.X)
sndBtn = tk.Button(inpFrm, bg = '#121212', fg = 'white', bd = 0, font = font.Font(family = '', size = 14))
sndBtn.image = tk.PhotoImage(file = 'send.png')
sndBtn.configure(image = sndBtn.image)
sndBtn.pack(side = tk.RIGHT, fill = tk.X)
inpFrm.pack(side = tk.BOTTOM, fill = tk.X)

root.mainloop()
