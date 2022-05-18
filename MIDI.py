from midiutil import MIDIFile


class MIDI():
    def __init__(self, duration, tempo, volume, volumeLowLim, numTracks, fileName, imageData):
        # longa = 4, double whole note = 2, whole note = 1, half = 1/2, quarter = 1/4
        # eighth = 1/8, sixteenth = 1/16, thirty-second = 1/32, sixty-fourth = 1/64
        # hundred twenty-eighth = 1/128
        self.noteDurations = [4, 2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125]
        self.track = [x for x in range(numTracks)]
        self.channel = 0
        self.time = 0
        self.duration = duration
        self.tempo = tempo
        self.volume = volume
        self.volumeLowLim = volumeLowLim
        self.midiFile = MIDIFile(numTracks=numTracks, removeDuplicates=True)
        self.mifiFileName = fileName
        self.imageData = imageData

    def addTempo(self):
        self.midiFile.addTempo(self.track, self.time, self.tempo)

    def writeMidi(self):
        with open(self.mifiFileName, "wb") as f:
            self.midiFile.writeFile(f)

    def createTracks(self):
        for idx, row in enumerate(self.imageData.pixel_array):
            for jIdx, pixel in enumerate(row):
                """
                    (R,G,B)
                    0-255 values
                    MIDI notes are from 0-127

                    structure:
                    pitch = (pixel[i]/2) if greater than 127 else pixel[i] val
                    duration = pixel[i] % 10 (length of self.noteDurations)
                    volume = 100 if greater than 100, else pixel[i] val
                """
                for i in self.track:
                    self.duration = self.noteDurations[pixel[i] % len(self.noteDurations)]
                    vol = self.volumeLowLim if int(pixel[i]) > self.volumeLowLim else int(pixel[i])
                    pitch = int(pixel[i]//2) if int(pixel[i]) > 127 else int(pixel[i])

                    # self.midiFile.addTempo(i, self.time, self.tempo)
                    self.midiFile.addNote(i, self.channel, pitch, self.time, float(self.duration), vol)
