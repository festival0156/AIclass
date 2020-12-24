import tkinter as tk
from tkinter import font
style = {
    'bgColor': '#121212',
    'fgColor': 'white',
    'root': {
        'title': 'Music App',
        'geometry': '1000x550' # size of window
    },
    'openScreen': { # opening screen
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
    def draw(this):
        this.opnBtn = tk.Button(root, text = style['openScreen']['openButton']['text'], bg = style['bgColor'], fg = style['fgColor'],
                                font = style['openScreen']['openButton']['font'](), padx = style['openScreen']['openButton']['padx'],
                                pady = style['openScreen']['openButton']['pady'], command = OpenScreen.cmd)
        this.opnBtn.place(anchor = 'center', relx = 0.5, rely = 0.5)
    def destroy(this):
        this.opnBtn.destroy()
    def cmd(): # executed when open button pressed
        from tkinter import filedialog
        fs = filedialog.askopenfilenames(parent = root, title = 'Open ...')
        global opnScrn, playScrn, player
        opnScrn.destroy()
        player = Player(fs)
        playScrn = PlayScreen(player)

class PlayScreen:
    def __init__(this, player):
        this.player = player
        this.draw()
    def draw(this):
        pass
    def destroy():
        pass

class Player:
    def __init__(this, playlist):
        this.playlist = list(playlist)
        this.i = 0
    def play(this):
        pass
    def previous(this):
        pass
    def next(this):
        pass
    def volume(this, increaseBy):
        pass
    def seek(this, time):
        pass

opnScrn = OpenScreen()
plyScrn = None
player = None
opnScrn.draw()
root.mainloop()
