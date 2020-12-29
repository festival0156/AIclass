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
            'font': lambda: font.Font(family = 'tahoma', size = 23),
            'padx': 160,
            'pady': 17
        },
        'filedialog': {
            'title': 'Open ...'
        }
    },
    'messages': {
        'pygameError': {
            'title': '',
            'message':
'''This environment does not meet the minimum requirements to run this program.

Minumum System Requirements:
    Python 3
    Tkinter 8.6
    Pygame 1.9

Recommended System Requirements:
    Python 3
    Tkinter 8.6
    Pygame 2.0
    CPU: Core i3 2.4 GHz
    GPU: AMD Rodeon HD 7870'''
        },
        'pygameWarning': {
            'title': 'Version Warning!!',
            'message': f'You are using pygame version {__import__("pygame").version.ver}; however, you should consider upgrading to at least version 2'
        },
        'python2warning': {
        	'title': 'Version Warning!!',
        	'message': f'You are using python version {__import__("sys").version}; however, you should consider upgrading to at least python 3'
        }
    },
    'playScreen': {
        'trackNoLabel': {
            'font': lambda: font.Font(family = 'times new roman', size = 20),
        }
    }
}
