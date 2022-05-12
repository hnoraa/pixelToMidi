from imageData import ImageData
from MIDI import MIDI


class PixelToMidi():
    def __init__(self, imagePath, outputFile):
        self.outputFile = outputFile
        self.imageData = ImageData(imagePath)
        self.midi = MIDI(4, 120, 100, 75, 3, self.outputFile, self.imageData)

    def createMIDI(self):
        self.midi.addTempo()

        self.midi.createTracks()

        self.midi.writeMidi()
