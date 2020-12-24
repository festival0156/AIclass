import tkinter as tk
from tkinter import font
style = {
    'bgColor': '#121212',
    'fgColor': 'white',
    'root': {
        'title': 'Music App',
        'geometry': '1000x550'
    }
    'openScreen': {
        'openButton': {
            'text': 'Open File(s)',
            'font': lambda: font.Font(family = 'tahoma', size = 20),
            'padx': 100,
            'pady': 20
        }
    }
}

root = tk.Tk()
root.configure(bg = style['bgColor'])
root.title(style['root']['title'])
root.geometry(style['root']['geometry'])
root.resizable(False, False)

class OpenScreen:
    def cmd():
        from tkinter import filedialog
        files = filedialog.askopenfilenames(mode = 'rb', parent = root, title = 'Open ...')
    def draw(this):
        this.opnBtn = tk.Button(root, text = style['openScreen']['openButton']['text'], bg = style['bgColor'], fg = style['fgColor'],
                                font = style['openScreen']['openButton']['font'](), padx = style['openScreen']['openButton']['padx'],
                                pady = style['openScreen']['openButton']['pady'], command = None)
        this.opnBtn.place(anchor = 'center', relx = 0.5, rely = 0.5)
    def destroy(this):
        this.opnBtn.destroy()

opnScrn = OpenScreen()
opnScrn.draw()
root.mainloop()
