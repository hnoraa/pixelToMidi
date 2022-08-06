# midiutil docs: https://readthedocs.org/projects/midiutil/downloads/pdf/latest/
from midiutil import MIDIFile
from track import Track

class MIDI():
    """
    MIDI wrapper class
    """
    def __init__(self, duration, tempo, volume, volumeLowLim, 
            numTracks, fileName, imageData):
        # longa = 4, double whole note = 2, whole note = 1, half = 1/2, 
        # quarter = 1/4, eighth = 1/8, sixteenth = 1/16, thirty-second = 1/32, 
        # sixty-fourth = 1/64, hundred twenty-eighth = 1/128
        self.noteDurations = [
            4, 2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125
        ]
        self.numTracks = numTracks
        self.tracks = []
        self.ticksPerQuarterNote = 960
        self.programs = [x for x in range(0, 127)]
        self.channel = 0
        self.time = 0
        self.duration = duration
        self.tempo = tempo
        self.volume = volume
        self.volumeLowLim = volumeLowLim
        self.midiFile = MIDIFile(numTracks=numTracks, removeDuplicates=True)
        self.mifiFileName = fileName
        self.imageData = imageData

    def createTracks(self, program):
        for i in range(self.numTracks):
            self.tracks.append(Track(i, i, program, ""))

    def listTracks(self):
        for i in range(len(self.tracks)):
            print(f"Track: {self.tracks[i].trackIdx}\n\t" 
                + f"Channel: {self.tracks[i].channel}, "
                + f"Program: {self.tracks[i].program}\n")

    def addTempo(self):
        self.midiFile.addTempo(self.numTracks, self.time, self.tempo)

    def writeMidi(self):
        with open(self.mifiFileName, "wb") as f:
            self.midiFile.writeFile(f)

    def populate(self):
        """
            (R,G,B)
            0-255 values
            MIDI notes are from 0-127

            structure:
            pitch = (pixel[i]/2) if greater than 127 else pixel[i] val
            duration = pixel[i] % 10 (length of self.noteDurations)
            volume = 100 if greater than 100, else pixel[i] val
        """
        for i in self.tracks:
            x = i.trackIdx

            self.midiFile.addProgramChange(x, i.channel, self.time, i.program)
            self.midiFile.addTempo(x, self.time, self.tempo)

            for idx, row in enumerate(self.imageData.pixel_array):
                for jIdx, pixel in enumerate(row):
                    durationIndex = pixel[x] % len(self.noteDurations)
                    self.duration = self.noteDurations[durationIndex]

                    pitch = int(pixel[x]//2) \
                        if int(pixel[x]) > 127 else int(pixel[x])

                    self.midiFile.addNote(x, i.channel, pitch, self.time, 
                        float(self.duration), self.volume)

                    self.time += 1
            self.time = 0
        # for i in range(len(self.tracks)):
        #     self.midiFile.
        # for i in range(len(self.track)):
        #     durationIndex = pixel[i] % len(self.noteDurations)
        #     self.duration = self.noteDurations[durationIndex]
        #     vol = self.volumeLowLim if int(pixel[i]) > self.volumeLowLim else int(pixel[i])
        #     pitch = int(pixel[i]//2) if int(pixel[i]) > 127 else int(pixel[i])
        #     # self.midiFile.addTempo(i, self.time, self.tempo)
        #     self.midiFile.addNote(self.track[i], self.channel, pitch, self.time, float(self.duration), vol)

