from json import loads
bgColor = '#121212'
fgColor = '#ffffff'
headFont = 'Franklin Gothic Demi'
hed2Font = 'Courier New'
bodyFont = 'Tahoma'
with open('countryCode.json', 'r') as f:
    countries = loads(f.read())
categories = ('  Business', '  Entertainment', '  General', '  Health', '  Science', '  Sports', '  Technology')
def loadData(search, country, category):
    url = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey=5286afcbe52e4e65ab101cce7af5182b'.format(country, category)
    if search:
        url = url + '&q=' + search
    import urllib.request as urlr
    raw = urlr.urlopen(url)
    content = loads(raw.read())
    if content['status']=='error':
        raise Exception(content['message'])
    else:
        return content

import tkinter as tk
from tkinter import ttk, font
root = tk.Tk()
root.geometry('1036x570')
root.configure(bg = bgColor)
root.title('festival0156n NEWS App')

def displayNews(data):
    from tkinter import font
    if data['totalResults']==0:
        tk.Label(newsContentFrame, text = 'No articles match selectors.', fg = fgColor,
                 font = (hed2Font, 30), bg = bgColor).place(relx = 0.6, rely = 0.5, anchor = 'center')
    else:
        for i in data['articles']:
            frame = tk.Frame(newsContentFrame, bg = bgColor)
            '''tk.Label(frame, text = i['title'], fg = fgColor, wraplength = 2000, bd = 3, padx = 10,
                     font = (hed2Font, 10), justify = 'left', bg = bgColor).pack(side = tk.TOP, fill = tk.X, pady = 10)'''
            txt = tk.Text(frame, bg = bgColor, fg = fgColor, bd = 2, height = 2, pady = 10, padx = 10,
                          font = font.Font(family = bodyFont, size = 14))
            txt.insert(tk.END, i['title'])
            txt.configure(state = 'disabled')
            txt.pack(fill = tk.X)
            print(i['title'] + '\n')
            frame.pack(fill = tk.X)
            articles.append(txt)

def showError(exs):
    tk.Label(newsContentFrame, text = 'Error loading news data.', fg = fgColor,
             font = (hed2Font, 30), bg = bgColor).place(relx = 0.5, rely = 0.5, anchor = 'center')

def reload():
    for i in articles:
        i.destroy()
    cn = countries[countryS.current()]
    ct = categories[categoryS.current()].strip()
    hTxt.configure(text = 'Top{} Headlines from {}'.format('' if ct=='General' else ' ' + ct, cn[0]))

    loadingFrames = [tk.PhotoImage(file = 'Spinner-1s-200px.gif', format = 'gif -index ' + str(i)) for i in range(31)]
    def update(ind):
        try:
            currentFrame = loadingFrames[ind]
            ind += 1
            imgLbl.configure(image = currentFrame)
            root.after(20, update, ind%31)
        except:
            pass
    imgLbl = tk.Label(newsContentFrame, bd = 0)
    imgLbl.place(relx = 0.5, rely = 0.4, anchor = 'center')
    t = tk.Label(newsContentFrame, text = 'Fetching news data ...', fg = fgColor,
                 font = (hed2Font, 30), bg = bgColor)
    t.place(relx = 0.5, rely = 0.75, anchor = 'center')
    root.after(0, update, 0)
    def loadNews():
        try:
            data = loadData(sbox.get(), cn[1], ct)
        except Exception as exc:
            imgLbl.destroy()
            t.destroy()
            showError(str(exc))
        else:
            imgLbl.destroy()
            t.destroy()
            displayNews(data)
    __import__('threading').Thread(target = loadNews).start()
    

header = tk.Frame(root, bg = bgColor)
hTxt = tk.Label(header, fg = fgColor, font = (headFont, 30), bg = bgColor)
hTxt.pack(fill = tk.X, pady = 20)
tk.Label(header, text = 'Country: ', bg = bgColor, fg = fgColor, padx = 7).pack(side = tk.LEFT)
countryS = ttk.Combobox(header, width = 30, textvariable = tk.StringVar(),
                         values = ['  ' + i[0] for i in countries])
countryS.current(17)
countryS.configure(state = 'readonly')
countryS.pack(side = tk.LEFT)
tk.Label(header, text = 'Category: ', bg = bgColor, fg = fgColor, padx = 7).pack(side = tk.LEFT)
categoryS = ttk.Combobox(header, width = 30, textvariable = tk.StringVar(),
                          values = categories)
categoryS.current(6)
categoryS.configure(state = 'readonly')
categoryS.pack(side = tk.LEFT)
simg = tk.Label(header, bd = 0)
simg.image = tk.PhotoImage(file = 'ic_search_48px-512.gif', format = 'gif')
simg.configure(image = simg.image)
simg.place(x = 560, rely = 0.9, anchor = 'center')
sbox = tk.Entry(header)
sbox.place(relx = 0.77, rely = 0.9, relwidth = 0.38, anchor = 'center')
refreshButtonImage = tk.PhotoImage(file = '1024px-Refresh_icon.gif', format = 'gif')
rimg = tk.Button(header, image = refreshButtonImage, bd = 0, bg = bgColor,
                 command = reload)
rimg.place(relx = 0.987, rely = 0.9, anchor = 'center')
header.pack(fill = tk.X)

canvas = tk.Canvas(root, bd = 0, bg = bgColor, highlightthickness = 0)
newsContentFrame = tk.Frame(canvas, bg = bgColor, padx = 7, pady = 7, bd = 2)
newsContentFrame.place(relx = 0.5, rely = 0.5, anchor = 'center', relheight = 1, relwidth = 1)
canvas.place(y = 116, relwidth = 1, relheight = 0.7)
sb = tk.Scrollbar(root, orient = 'vertical', command = canvas.yview)
canvas.configure(yscrollcommand = sb.set)
sb.pack(side = tk.RIGHT, fill = tk.Y)
articles = list()

reload()
root.mainloop()
