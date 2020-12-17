bgColor = '#121212'
fgColor = '#ffffff'

import tkinter as tk
root = tk.Tk()
root.geometry('1000x550')
root.configure(bg = bgColor)
root.title('festival0156n NEWS App')

def displayNews(data):
    imgLbl.destroy()
    t.destroy()
    from tkinter import font
    hed = tk.Text(root, bg = bgColor, fg = fgColor, bd = 2, height = 1, pady = 20,
                  font = font.Font(family = 'times new roman', size = 30))
    hed.tag_configure("center", justify='center')
    hed.insert(tk.END, 'Top Technology Headlines in India')
    hed.tag_add("center", "1.0", "end")
    hed.pack(fill = tk.X)
    txt = tk.Text(root, bg = bgColor, fg = fgColor, bd = 0, padx = 10, pady = 10,
                  font = font.Font(family = 'arial', size = 14))
    sb = tk.Scrollbar(root, command = txt.yview)
    txt.configure(yscrollcommand = sb.set)
    sb.pack(side = tk.RIGHT, fill = tk.Y)
    for i in data['articles']:
        txt.insert(tk.END, i['title'] + '\n\n')
    txt.pack(fill = tk.X)

def loadNews():
    try:
        url = 'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=5286afcbe52e4e65ab101cce7af5182b'
        import urllib.request as urlr
        raw = urlr.urlopen(url)
        content = __import__('json').loads(raw.read())
        if content['status']!='ok':
            raise Exception('data[\'status\'] = ' + data['status'])
        else:
            displayNews(content)
    except Exception as exc:
        exs = str(exc)
        imgLbl.destroy()
        t.destroy()
        txt = tk.Text(root, bg = bgColor, fg = fgColor, bd = 0)
        from tkinter import font
        txt['font'] = font.Font(family = 'consolas', size = 30)
        txt.insert(tk.END, 'Error getting news data rn.\n\nTry checking your internet connection.')
        txt.configure(state = 'disabled')
        txt.place(relx = 0.08, rely = 0.4, anchor = 'nw')
        img = tk.Label(root, bd = 0)
        img.image = tk.PhotoImage(file = 'PinClipart.com_attention-clip-art_941509.gif', format = 'gif')
        img.configure(image = img.image)
        img.place(relx = 0.5, rely = 0.2, anchor = 'center')
        btnFont = font.Font(family = 'consolas', size = 15)
        exitBtn = tk.Button(root, text = 'Exit', command = root.destroy, font = btnFont, bg = bgColor, fg = fgColor)
        exitBtn.place(relx = 0.2, rely = 0.8, anchor = 'center')
        trAgBtn = tk.Button(root, text = 'Try Again', font = btnFont, bg = bgColor, fg = fgColor,
                            command = lambda: __import__('os').execv(__import__('sys').executable, ['python', __file__]))
        trAgBtn.place(relx = 0.5, rely = 0.8, anchor = 'center')
        from tkinter import messagebox
        sExIBtn = tk.Button(root, text = 'Show Exception Info', font = btnFont, bg = bgColor, fg = fgColor,
                            command = lambda: messagebox.showerror(title = 'Exception Info', message = exs))
        sExIBtn.place(relx = 0.8, rely = 0.8, anchor = 'center')

loadingFrames = [tk.PhotoImage(file = 'Spinner-1s-200px.gif', format = 'gif -index ' + str(i)) for i in range(31)]
def update(ind):
    try:
        currentFrame = loadingFrames[ind]
        ind += 1
        imgLbl.configure(image = currentFrame)
        root.after(20, update, ind%31)
    except:
        pass
imgLbl = tk.Label(root)
imgLbl['bd'] = 0
imgLbl.place(relx = 0.5, rely = 0.3, anchor = 'center')
t = tk.Text(root, bg = bgColor, fg = fgColor, bd = 0)
from tkinter import font
t['font'] = font.Font(family = 'consolas', size = 30)
t.insert(tk.END, 'Fetching news data ...')
t.configure(state = 'disabled')
t.place(relx = 0.25, rely = 0.58, anchor = 'nw')
root.after(0, update, 0)
root.after(0, __import__('_thread').start_new_thread, loadNews, ())
root.mainloop()
