from PIL import Image
from midiutil import MIDIFile

class ImageImport():
    def __init__(self, image_path) -> None:
        self.image_path = image_path

    def import_image(self):
        self.img = Image.open(self.image_path, 'r')
        self.img_map = list(self.img.getdata())

    def test_image_array(self):
        # this might be useful...
        # this gets the image array (no numpy)
        self.test_array = list(self.img.getdata())

        # this gets a flat version of the array
        # ex: if I have [(255, 210, 123, 55), (90, 190, 200, 100)] in the array
        # this flattens to [255 ,210, 123, 55, 90, 190, 200, 100]
        self.test_array_flat = [x for sets in self.test_array for x in sets]

        print(self.test_array)
        print(self.test_array_flat)

class MidiProcessor():
    def __init__(self, midi_file_name) -> None:
        self.midi_file_name = midi_file_name

        self.track = 0
        self.channel = 0
        self.time = 0                # in beats
        self.duration = 4            # in beats
        self.tempo = 120             # BPM
        self.volume = 100            # 0 - 127 (MIDI standard)
        self.volume_low_lim = 75     # low limit for volume

        self.midi_file = MIDIFile(1)
        self.midi_file.addTempo(self.track, self.time, self.tempo)

    def create_midi(self, pixel_map):
        for idx, row in enumerate(pixel_map):
            """
                (R,G,B) or (R,B,G,A)
                0-255 values
                MIDI notes are from 0-127
                structure:
                R - pitch (R/2) if greater than 127 else R val
                G - duration
                B - volume 100 if greater than 100, else B val
                A - (optional) I think this could be useful for multi-tracking
                    Ex: say you have 4 tracks, A value is 100, the current track could be tracks[A % len(tracks)]
            """
            pitch = int(row[0]//2) if int(row[0]) > 127 else int(row[0])
            if len(row) > 1:
                self.volume = self.volume_low_lim if int(row[2]) > self.volume_low_lim else int(row[2])
            self.midi_file.addNote(self.track, self.channel, pitch, self.time+idx+self.duration, self.duration, self.volume)

        with open(self.midi_file_name, 'wb') as f:
            self.midi_file.writeFile(f)

class Main():
    def __init__(self, midi_file_name, image_path) -> None:
        self.i = ImageImport(image_path)
        self.m = MidiProcessor(midi_file_name)

    def execute(self, debug=False):
        if debug:
            m.i.test_image_array()
        else:
            self.i.import_image()
            self.m.create_midi(self.i.img_map)

if __name__ == '__main__':
    m = Main('song.midi', '.\\images\\tester.bmp')
    m.execute()
    