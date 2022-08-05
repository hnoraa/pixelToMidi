from midiutil import MIDIFile

class Test:
    def __init__(self, numTracks):
        self.tracks = numTracks
        self.noteDurations = [4, 2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125]
        self.degrees = [60, 62, 64, 65, 67, 69, 71, 72]
        self.degrees2 = [70, 72, 74, 75, 77, 79, 81, 82]
        self.programs = [x for x in range(0, 127)]
        self.channel = 0
        self.time = 0
        self.duration = 4
        self.tempo = 120
        self.volume = 100
        self.volumeLowLim = 75
        self.midiFile = MIDIFile(numTracks=numTracks, removeDuplicates=True, ticks_per_quarternote=960)
        self.midiFileName = 'tester.midi'
        #self.imageData = imageData

    def loopTracks(self):
        for i in range(self.tracks):
            print(i)

    def createMidi(self):
        for i in range(self.tracks):
            self.midiFile.addProgramChange(i, i, self.time, i+3)
            self.midiFile.addTempo(i, self.time, self.tempo)

            if i % 2 == 0:
                for pitch in range(len(self.degrees2), -1, -1):
                    self.midiFile.addNote(i, i, self.degrees2[i], self.time, self.duration, self.volume)
                    self.time += 1
            else:
                for pitch in self.degrees:
                    self.midiFile.addNote(i, i, pitch, self.time, self.duration, self.volume)
                    self.time += 1
            self.time = 0
            
        with open(self.midiFileName, "wb") as f:
            self.midiFile.writeFile(f)


if __name__ == '__main__':
    t = Test(3)

    #t.loopTracks()
    t.createMidi()