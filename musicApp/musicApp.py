import tkinter as tk
from tkinter import font
from style import style

root = tk.Tk()
root.configure(bg = style['bgColor'])
root.title(style['root']['title'])
root.geometry(style['root']['geometry'])
root.resizable(False, False)

class OpeningScreen:
    def draw(this):
        this.opnBtn = tk.Button(root, text = style['openScreen']['openButton']['text'], bg = style['bgColor'], fg = style['fgColor'],
                                font = style['openScreen']['openButton']['font'](), padx = style['openScreen']['openButton']['padx'],
                                pady = style['openScreen']['openButton']['pady'], command = OpeningScreen.cmd)
        this.opnBtn.place(anchor = 'center', relx = 0.5, rely = 0.5)
    def destroy(this):
        this.opnBtn.destroy()
    def cmd(): # executed when open button pressed
        from tkinter import filedialog
        fs = filedialog.askopenfilenames(parent = root, title = style['openScreen']['filedialog']['title'])
        if fs:
            global opnScrn, playScrn, player
            opnScrn.destroy()
            player = Player(fs)
            playScrn = PlayScreen(player)
            playScrn.draw()

class PlayScreen:
    def __init__(this, player):
        this.player = player
        this.draw()
    def draw(this):
        this.tnoLbl = tk.Label(root, text = f'Playing track {player.nowplaying+1} of {len(player.playlist)}:\n{__import__("os").path.split(player.playlist[player.nowplaying])[1].replace(".mp3", "")}',
                               fg = style['fgColor'], bg = style['bgColor'], font = style['playScreen']['trackNoLabel']['font']())
        this.tnoLbl.place(anchor = 'center', relx = 0.5, rely = 0.2)
        
    def destroy(this):
        this.tnoLbl.destroy()

class ErrorScreen:
    def draw(this):
        pass
    def destroy(this):
        pass

class Player:
    def __init__(this, playlist):
        this.playlist = list(playlist)
        try:
            from pygame import mixer
        except:
            from tkinter import messagebox
            messagebox.showerror(message = 'This environment does not meet the minimum requirements to run this program.\n\nMinumum System Requirements:\n    Python 3\n    Tkinter 8.6\n    Pygame 1.9\n\nRecommended System Requirements:\n    Python 3\n    Tkinter 8.6\n    Pygame 2.0\n    CPU: Core i3 2.4 GHz\n    GPU: AMD Rodeon HD 7870')
            root.destroy()
        mixer.init()
        this.nowplaying = -1
        mixer.music.load(this.playlist[0])
        mixer.music.play()
        this.music = mixer.music
    def play(this):
        this.music.unpause()
    def pause(this):
        this.music.pause()
    def previous(this):
        this.nowplaying -= 1
        this.reload()
    def next(this):
        this.nowplaying += 1
        this.reload()
    def volume(this, set2):
        this.set_volume(set2)
    def reload(this):
        try:
            this.music.unload()
        except AttributeError:
            from tkinter import messagebox
            from pygame.version import ver
            messagebox.showwarning(title = 'Version Warning!!', message = f'You are using pygame version {ver}; however, you should consider upgrading to at least version 2')
        this.music.load(this.playlist[this.nowplaying])
        this.music.play()
    def seek(this, time):
        pass

opnScrn = OpeningScreen()
plyScrn = None
player = None
opnScrn.draw()
root.mainloop()
