from tkinter import *
from tkinter.ttk import *


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title('Pixel To MIDI')
        self.geometry('600x600')
        self.statusLblTxt = StringVar()

        self.__statusBar()
        self.__menu()
        self.__tabs()

        self.config(menu=self.mainMenu)

    def __menu(self):
        self.mainMenu = Menu(self)
        fM = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='File', menu=fM)
        fM.add_command(label='New', command=self.__menuNew)
        fM.add_command(label='Open', command=self.__menuOpen)
        fM.add_separator()
        fM.add_command(label='Save', command=self.__menuSave)
        fM.add_command(label='Save As', command=self.__menuSaveAs)
        fM.add_separator()
        fM.add_command(label='Exit', command=self.destroy)

    def __statusBar(self):
        self.statusBar = Label(
            self, 
            textvariable=self.statusLblTxt, 
            border=1,
            relief=SUNKEN, 
            anchor=W
        )
        self.statusBar.pack(side=BOTTOM, fill=X)

    def __tabs(self):
        self.tabControl = Notebook(self)
        self.tabSong = Frame(self.tabControl)
        self.tabTracks = Frame(self.tabControl)
        self.tabImage = Frame(self.tabControl)
        
        self.tabControl.add(self.tabSong, text='Song')
        self.tabControl.add(self.tabTracks, text='Tracks')
        self.tabControl.add(self.tabImage, text='Image')
        self.tabControl.pack(expand=1, fill='both')

    def __menuNew(self):
        self.statusLblTxt.set('New menu selected')

    def __menuOpen(self):
        self.statusLblTxt.set('Open menu selected')

    def __menuSave(self):
        self.statusLblTxt.set('Save menu selected')

    def __menuSaveAs(self):
        self.statusLblTxt.set('Save As menu selected')

if __name__ == '__main__':
    win = Window()
    win.mainloop()