from PIL import Image
from numpy import asarray
from midiutil import MIDIFile

class Main():
    def __init__(self, output_file_name) -> None:
        self.track = 0
        self.channel = 0
        self.time = 0                # in beats
        self.duration = 4            # in beats
        self.tempo = 120             # BPM
        self.volume = 100            # 0 - 127 (MIDI standard)
        self.volume_low_lim = 75       # low limit for volume

        self.midi_file = MIDIFile(1)
        self.midi_file.addTempo(self.track, self.time, self.tempo)
        self.song_name = output_file_name

    def import_image(self, imagePath):
        self.img = Image.open(imagePath)
        self.map = asarray(self.img)

    def create_midi(self):
        for idx, row in enumerate(self.map):
            for jdx, pixel in enumerate(row):
                """
                    (R,G,B)
                    0-255 values
                    MIDI notes are from 0-127
                    structure:
                    R - pitch (R/2) if greater than 127 else R val
                    G - duration
                    B - volume 100 if greater than 100, else B val
                """
                pitch = int(pixel[0]//2) if int(pixel[0]) > 127 else int(pixel[0])
                if len(pixel) > 1:
                    self.volume = self.volume_low_lim if int(pixel[2]) > self.volume_low_lim else int(pixel[2])
                self.midi_file.addNote(self.track, self.channel, pitch, self.time+idx+jdx+self.duration, self.duration, self.volume)

        with open(self.song_name, 'wb') as f:
            self.midi_file.writeFile(f)

if __name__ == '__main__':
    m = Main('song.midi')
    m.import_image('.\\images\\tester.bmp')
    m.create_midi()