import tkinter as tk
from tkinter import font

root = tk.Tk()
root.geometry('1000x500')
root.configure(bg = '#121212')
root.title('ChatBot')

name = '{name}'
l = ['chatterbot.logic.BestMatch', # logic adapters
     'chatterbot.logic.MathematicalEvaluation',
     'chatterbot.logic.TimeLogicAdapter']
c = ['chatterbot.corpus.english'] # corpora
bot = None

frm = tk.Frame(root, bg = '#121212', bd = 0)

class LoadingScreen:
    def draw(this):
        this.loadingFrames = [tk.PhotoImage(file = 'spinner1.gif', format = f'gif -index {i}') for i in range(31)]
        this.imgLbl = tk.Label(frm, bd = 0)
        this.imgLbl.place(relx = 0.5, rely = 0.4, anchor = 'center')
        root.after(20, updateGif, 0)
        this.strVar = tk.StringVar()
        this.txtLbl = tk.Label(frm, bg = '#121212', fg = 'white', bd = 2, pady = 0, justify = tk.LEFT,
                          padx = 0, font = font.Font(family = '', size = 14), textvariable = strVar)
        this.txtLbl.place(relx = 0.5, rely = 0.75, anchor = 'center')
    def load(this):
        this.strVar.set('Fetching Dependencies ...')
        from chatterbot import ChatBot
        from chatterbot.trainers import ChatterBotCorpusTrainer
        this.strVar.set('Initialising Bot Engine ...')
        global bot
        bot = ChatBot(name = name, logic_adapters = l)
        this.strVar.set('Training Bot. Please wait.')
        ctr = ChatterBotCorpusTrainer(bot)
        for i in c:
            ctr.train(i)

        this.frm.destroy()
        global chtScrn
        chtScrn = ChatScreen()
        chtScrn.draw()
    def updateGif(this, ind):
        this.imgLbl.configure(image = loadingFrames[ind])
        this.imgLbl.after(20, updateGif, (ind+1)%31)

class ChatScreen:
    def draw(this):
        this.cvnStv = tk.StringVar()
        this.cvnLbl = tk.Label(root, bg = '#121212', fg = 'white', bd = 2, pady = 0, justify = tk.LEFT,
                          padx = 0, font = font.Font(family = '', size = 14), textvariable = cvnStr)
        this.cvnLbl.pack(side = tk.TOP, fill = tk.X)
        this.inpFrm = tk.Frame(root, bg = 'white', bd = 2)
        this.inpStv = tk.StringVar()
        this.inpEnt = tk.Entry(inpFrm, textvariable = inpStv, bg = '#121212', fg = 'white', bd = 2,
            font = font.Font(family = '', size = 14), exportselection = False)
        this.inpEnt.pack(side = tk.LEFT, fill = tk.X)
        this.sndBtn = tk.Button(inpFrm, command = this.send, bg = '#121212', fg = 'white', bd = 0, font = font.Font(family = '', size = 14))
        this.sndBtn.image = tk.PhotoImage(file = 'send.png')
        this.sndBtn.configure(image = sndBtn.image)
        this.sndBtn.pack(side = tk.RIGHT, fill = tk.X)
        this.inpFrm.pack(side = tk.BOTTOM, fill = tk.X)

    def destroy(this):
        pass

    def send(this):
        msg = inpStv.get()
        inpStv.set('')
        cvnStv.set(cvnStv.get() + '\n[<] ' + msg)
        msg = bot.get_response(msg).text
        cvnStv.set(cvnStv.get() + '\n[>] ' + msg)

class ErrorScreen:
    def __init__(this, exc):
        exs = str(exc)

    def draw(this):
        pass
    def destroy(this):
        pass

def cls():
    global frm
    frm.destroy()
    frm = tk.Frame(root, bg = '#121212', bd = 0)
    frm.place(x = 0, y = 0, anchor = 'ne')

ldnScrn = LoadingScreen()
ldnScrn.draw()
try:
    from threading import Thread
    Thread(target = ldnScrn.load).start()
except Exception as exc:
    errScrn = ErrorScreen(exc)
    errScrn.draw()

root.mainloop()