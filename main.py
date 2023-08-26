from PIL import Image
from numpy import asarray
from midiutil import MIDIFile

class ImageImport():
    def __init__(self, image_path) -> None:
        self.image_path = image_path

    def import_image(self):
        self.img = Image.open(self.image_path)
        self.map = asarray(self.img)

class MidiProcessor():
    def __init__(self, midi_file_name, image_import) -> None:
        self.midi_file_name = midi_file_name
        self.image_import = image_import

        self.track = 0
        self.channel = 0
        self.time = 0                # in beats
        self.duration = 4            # in beats
        self.tempo = 120             # BPM
        self.volume = 100            # 0 - 127 (MIDI standard)
        self.volume_low_lim = 75     # low limit for volume

        self.midi_file = MIDIFile(1)
        self.midi_file.addTempo(self.track, self.time, self.tempo)

    def create_midi(self):
        for idx, row in enumerate(self.image_import.map):
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

        with open(self.midi_file_name, 'wb') as f:
            self.midi_file.writeFile(f)

class Main():
    def __init__(self, midi_file_name, image_path) -> None:
        self.i = ImageImport(image_path)
        self.m = MidiProcessor(midi_file_name, self.i)

    def execute(self):
        self.i.import_image()
        self.m.create_midi()

if __name__ == '__main__':
    m = Main('song.midi', '.\\images\\tester.bmp')
    m.execute()