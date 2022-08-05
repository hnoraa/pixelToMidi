# create an array of pixels
# convert that to a midi file
# RGB -> Pitch, Duration, ?
from tkinter import Tk
from ui import Window
from pixelToMidi import PixelToMidi

graphical = False

def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = Window()
    root.mainloop()

if __name__ == '__main__':
    image = 'images/tester.png'
    midiPath = 'out.midi'
    ptm = PixelToMidi(image, midiPath)

    if graphical:
        main()
    else:
        print("creating MIDI")
        ptm.createMIDI()
        ptm.midi.listTracks()
