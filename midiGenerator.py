# midiutil docs: https://readthedocs.org/projects/midiutil/downloads/pdf/latest/
from midiutil import MIDIFile
from song import Song
from imageMatrixGenerator import ImageMatrixGenerator


class MidiGenerator():
    def __init__(self, song, midiProgram):
        self.song = song
        # longa = 4, double whole note = 2, whole note = 1, half = 1/2, 
        # quarter = 1/4, eighth = 1/8, sixteenth = 1/16, thirty-second = 1/32, 
        # sixty-fourth = 1/64, hundred twenty-eighth = 1/128
        self.noteDurations = [
            4, 2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125
        ]
        self.midiProgram = midiProgram
        self.img = ImageMatrixGenerator(self.song.imageName)
        self.midiFile = MIDIFile(numTracks=len(self.song.tracks), 
            removeDuplicates=True)
        self.time = 0

    def __writeMidiFile(self):
        with open(self.song.fileName, "wb") as f:
            self.midiFile.writeFile(f)

    def __addTempo(self, trackNum):
        self.midiFile.addTempo(trackNum, self.time, self.song.tempo)

    def __addProgramChange(self, trackNum, channel, program):
        self.midiFile.addProgramChange(trackNum, channel, self.time, program)

    def __addNote(self, trackNum, channel, pitch):
        self.midiFile.addNote(trackNum, channel, pitch, 
            self.time, float(self.song.duration), 100)

    def __pitch(self, pixel):
        return int(pixel//2) if int(pixel) > 127 else int(pixel)

    def createSong(self):
        for tr in self.song.tracks:
            # set up the track
            self.__addProgramChange(tr.id, tr.channel, tr.program)
            self.__addTempo(tr.id)

            # create track notes from image data
            for i, r in enumerate(self.img.imageMatrix):
                for j, p in enumerate(r):
                    durationIdx = p[tr.id] % len(self.noteDurations)
                    self.song.duration = self.noteDurations[durationIdx]
                    self.__addNote(tr.id, tr.channel, self.__pitch(p[tr.id]))
                    self.time += 1
            self.time = 0

        self.__writeMidiFile()
