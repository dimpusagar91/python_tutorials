#!/usr/bin/python

# Simple button demo.
from Tkinter import *
import socket

# A better way is to create our fancy button by extending the Button class.
class HostnameLabel(Label):
    '''A Label widget which knows about an associated Entry widget, and can
       look up the host name it contains and display the corresponding IP'''

    # Look up host name in the assocated entry widget source, and display
    # in ourselves.
    def show(self):
        hn = self.source.get().strip()
        if hn == '':
            ip = ''
        else:
            try:
                ip = socket.gethostbyname(hn)
            except:
                ip = '[unknown]'
        self.configure(text=ip)

    # Show for event (just discards arg 2)
    def eshow(self, event):
        self.show()

    def __init__(self, root, entry):
        Label.__init__(self, root, text="", width=15)
        self.source = entry
        entry.bind('<Return>', self.eshow)
        

# Here are the colors.  These are just ordinary variables, and I need to
# remember to send them to all relevant widgets.  
bgcolor = '#AAAAFF'
actbgcolor = '#CCCCFF'
fgcolor = '#884400'

# Root and backing frame.
root = Tk()
root.title('Host Conversion')
fr = Frame(root, background=bgcolor)
fr.pack()

# Title label
tit = Label(fr, text="Host Name Conversion", background=bgcolor,
            foreground=fgcolor, relief='groove')
tit.grid(row=0, column=0, columnspan=2, sticky='news')

# Name entry.
entr = Entry(fr, width=25, background=bgcolor, foreground=fgcolor)
entr.grid(row=1, column=0, columnspan=2, sticky='news')
def clearem(e):
    entr.delete(0,END)
    dislab.configure(text='')
entr.bind('<Button-1>', clearem)

# Reporting label.
dislab = HostnameLabel(fr, entr)
dislab.configure(background=bgcolor, foreground=fgcolor)
dislab.grid(row=2, column=0, sticky='news')

# Go button.
but = Button(fr, text="Find", background=bgcolor, activebackground=actbgcolor,
             foreground=fgcolor, command=dislab.show)
but.grid(row=2, column=1, sticky='news')

root.mainloop()