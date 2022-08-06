# midiutil docs: https://readthedocs.org/projects/midiutil/downloads/pdf/latest/
from midiutil import MIDIFile
from song import Song


class MidiGenerator():
    def __init__(self, song):
        self.song = song
