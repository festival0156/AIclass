import tkinter as tk
from tkinter import font
style = {
    'bgColor': '#121212',
    'fgColor': 'white',
    'title': 'Music App',
    'buttonFont': lambda: font.Font(family = 'tahoma', size = 20)
}

root = tk.Tk()
root.configure(bg = style['bgColor'])
root.title(style['title'])
root.geometry('1000x550')
root.resizable(False, False)

class OpenScreen:
    def cmd():
        from tkinter import filedialog
        files = filedialog.askopenfilenames(mode = 'rb', parent = root, title = 'Open ...')
    def draw(this):
        this.opnBtn = tk.Button(root, text = 'Open File(s)', bg = style['bgColor'], fg = style['fgColor'],
                                font = style['buttonFont'](), padx = 90, pady = 20)
        this.opnBtn.place(anchor = 'center', relx = 0.5, rely = 0.5)
    def destroy(this):
        this.opnBtn.destroy()

opnScrn = OpenScreen()
root.mainloop()
