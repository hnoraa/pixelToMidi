from song import Song
from imageMatrixGenerator import ImageMatrixGenerator
from midiGenerator import MidiGenerator
import json


class PixelToMidi():
    def __init__(self, configFile):
        self.song = Song(configFile)

    def pToM(self):
        with open("MIDI_programs.json") as p:
            self.programs = json.load(p)
        self.midi = MidiGenerator(self.song, self.programs['programs'])

        self.midi.createSong()
