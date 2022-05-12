from tkinter import Tk, Text, BOTH, W, N, E, S, Canvas, Menu
from tkinter.ttk import Frame, Button, Label, Style


class Window(Frame):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.master.title("Pixel to MIDI")
        self.pack(fill=BOTH, expand=True)

        self.menubar = Menu(self)
        fM = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=fM)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        area = Canvas(self, bg="white")
        area.grid(row=1, column=0, columnspan=2, rowspan=4,
                  padx=5, sticky=E+W+S+N)

        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)
