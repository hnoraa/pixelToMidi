from midiutil import MIDIFile


class MIDI():
    def __init__(self, duration, tempo, volume, volumeLowLim, numTracks, fileName, imageData):
        self.track = numTracks
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
                    R - pitch (R/2) if greater than 127 else R val
                    G - duration
                    B - volume 100 if greater than 100, else B val
                """
                self.time = idx+jIdx+self.duration
                
                # R track
                volumeR = self.volumeLowLim if int(pixel[0]) > self.volumeLowLim else int(pixel[0])
                pitchR = int(pixel[0]//2) if int(pixel[0]) > 127 else int(pixel[0])
                self.midiFile.addNote(0, self.channel, pitchR, self.time, self.duration, volumeR)

                if self.track > 1:
                    # G track
                    volumeG = self.volumeLowLim if int(pixel[1]) > self.volumeLowLim else int(pixel[1])
                    pitchG = int(pixel[1]//2) if int(pixel[1]) > 127 else int(pixel[1])
                    self.midiFile.addNote(1, self.channel, pitchG, self.time, self.duration, volumeG)

                    # B track
                    volumeB = self.volumeLowLim if int(pixel[2]) > self.volumeLowLim else int(pixel[2])
                    pitchB = int(pixel[2]//2) if int(pixel[2]) > 127 else int(pixel[2])
                    self.midiFile.addNote(2, self.channel, pitchB, self.time, self.duration, self.volume)
