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
    'playScreen': {
        'trackNoLabel': {
            'font': lambda: font.Font(family = 'times new roman', size = 20),
        }
    }
}