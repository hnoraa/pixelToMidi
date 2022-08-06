from imageData import ImageData
from song import Song


class PixelToMidi():
    """
    Command line constructor
    """
    def __init__(self, configFile):
        self.song = Song(configFile)
        self.__init__(self.song.imageName, self.song.fileName)

    """
    UI constructor
    """
    def __init__(self, imagePath, outputFile):
        self.outputFile = outputFile
        self.imageData = ImageData(imagePath)
        # self.midi = MIDI(4, 120, 100, 75, 3, self.outputFile, self.imageData)

    # def createMIDI(self):
    #     # self.midi.createTracks(30)
        
    #     # self.midi.addTempo()

    #     # self.midi.populate()

    #     # self.midi.writeMidi()
    #     pass
