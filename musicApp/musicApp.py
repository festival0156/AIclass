import tkinter as tk
from tkinter import font
style = {
  'bgColor': '#121212',
  'fgColor': 'white',
  'root': {
    'title': 'Music App',
    'geometry': '1200x400' # size of window
  },
  'openScreen': { # opening screen
    'openButton': {
      'text': 'Open File(s)',
      'font': lambda: font.Font(family = 'tahoma', size = 20),
      'padx': 100,
      'pady': 20
    },
    'filedialog': {
      'title': 'Open ...'
    }
  },
  'loadingScreen': {
    'label': {
      'font': lambda: font.Font(family = 'times new roman', size = 20),
    }
  }
}

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
        this.tnoLbl = tk.Label(root, text = 'Playing track {} of {}:'.format(player.nowplaying + 1, len(player.playlist), )
    def destroy():
        pass

class ErrorScreen:
    def draw(this):
        pass
    def destroy(this):
        pass

class Player:
    def __init__(this, playlist):
        this.playlist = list(playlist)
        from pygame import mixer
        mixer.init()
        this.nowplaying = 0
        mixer.music.load(this.playlist[0])
        mixer.music.play()
        this.music = mixer.music
    def play(this):
        this.music.unpause()
    def pause(this):
        this.music.pause()
    def previous(this):
        this.nowplaying -= 1
        this.music.unload()
        this.music.load(this.playlist[this.nowplaying])
        this.music.play()
    def next(this):
        this.nowplaying += 1
        this.music.unload()
        this.music.load(this.playlist[this.nowplaying])
        this.music.play()
    def volume(this, set2):
        this.set_volume(set2)
    def seek(this, time):
        pass

opnScrn = OpeningScreen()
plyScrn = None
player = None
opnScrn.draw()
root.mainloop()
