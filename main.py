# create an array of pixels
# convert that to a midi file
# RGB -> Pitch, Duration, ?
from tkinter import Tk
from ui import Window
from pixelToMidi import PixelToMidi
from song import Song

graphical = False

def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = Window()
    root.mainloop()

if __name__ == '__main__':
    ptm = PixelToMidi('song.json')

    if graphical:
        main()
    else:
        print("creating MIDI")
        ptm.pToM()
