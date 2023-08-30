from PIL import Image
from midiutil import MIDIFile

class ImageImport():
    def __init__(self, image_path) -> None:
        self.image_path = image_path
        self.img = None
        self.img_map = None

    def import_image(self):
        self.img = Image.open(self.image_path, 'r')
        self.img_map = list(self.img.getdata())

    def describe(self):
        if self.img is not None:
            print(f'{self.image_path} details:')
            print(f'Image size (w, h):\t{self.img.width} x {self.img.height}')
            print(f'Image format:\t\t{self.img.format}\n')

    def test_image_array(self):
        if self.img is not None:
            # this might be useful...
            # this gets the image array (no numpy)
            self.test_array = list(self.img.getdata())

            # this gets a flat version of the array
            # ex: if I have [(255, 210, 123, 55), (90, 190, 200, 100)] in the array
            # this flattens to [255 ,210, 123, 55, 90, 190, 200, 100]
            self.test_array_flat = [x for sets in self.test_array for x in sets]

            print(f'Length before flattening: {len(self.test_array)}')
            print(f'Flattened length: {len(self.test_array_flat)}\n')

    def split_image_array_test(self, num_tracks=1):
        if self.img_map is not None:
            track_split = len(self.img_map) // num_tracks

            self.track_map = []
            for i in range(0, len(self.img_map)):
                sub_split = i % track_split

                if sub_split == 0:
                    new_list = []
                    for j in range(i, i + track_split):
                        new_list.append(self.img_map[j])
                    self.track_map.append(new_list)

            print(f'New map of length {len(self.track_map)} with {num_tracks} lists of length {track_split}')
            for i in range(0, len(self.track_map)):
                print(self.track_map[i])

    def split_image_array(self, num_tracks=1):
        if self.img_map is not None:
            track_split = len(self.img_map) // num_tracks

            self.track_map = []
            for i in range(0, len(self.img_map)):
                sub_split = i % track_split

                if sub_split == 0:
                    new_list = []
                    for j in range(i, i + track_split):
                        new_list.append(self.img_map[j])
                    self.track_map.append(new_list)


class MidiProcessor():
    def __init__(self, midi_file_name, num_tracks=1) -> None:
        self.midi_file_name = midi_file_name

        self.track = 0
        self.channel = 0
        self.time = 0                # in beats
        self.duration = 4            # in beats
        self.tempo = 120             # BPM
        self.volume = 100            # 0 - 127 (MIDI standard)
        self.volume_low_lim = 75     # low limit for volume

        # longa = 4, double whole note = 2, whole note = 1, half = 1/2, 
        # quarter = 1/4, eighth = 1/8, sixteenth = 1/16, thirty-second = 1/32, 
        # sixty-fourth = 1/64, hundred twenty-eighth = 1/128
        self.noteDurations = [
            4, 2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125
        ]

        self.midi_file = MIDIFile(num_tracks)
        self.midi_file.addTempo(self.track, self.time, self.tempo)

    def create_midi(self, pixel_map):
        for idx, row in enumerate(pixel_map):
            """
                (R,G,B) or (R,G,B,A)
                0-255 values
                MIDI notes are from 0-127
                structure:
                R - pitch (R/2) if greater than 127 else R val
                G - duration somehow this needs get from 0-255 to 0-9 for the noteDurations
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

    def create_midi_multi_track(self, track_map, tracks):
        for i, track in enumerate(tracks):
            self.midi_file.addProgramChange(i, i, 0, track['program'])
            for idx, row in enumerate(track_map[i]):
                pitch = int(row[0]//2) if int(row[0]) > 127 else int(row[0])
                if len(row) > 1:
                    self.volume = self.volume_low_lim if int(row[2]) > self.volume_low_lim else int(row[2])
                    self.duration = self.noteDurations[row[1] % 9]
                self.midi_file.addNote(i, i, pitch, self.time+idx+self.duration, self.duration, self.volume)

        with open(self.midi_file_name, 'wb') as f:
            self.midi_file.writeFile(f)

class Main():
    def __init__(self, midi_file_name, image_path, tracks) -> None:
        self.tracks = tracks

        self.i = ImageImport(image_path)
        self.m = MidiProcessor(midi_file_name, len(self.tracks))

    def execute(self, debug=False):
        self.i.import_image()

        if debug:
            m.i.describe()
            m.i.test_image_array()
            m.i.split_image_array_test(2)
        else:
            m.i.split_image_array(len(self.tracks))
            self.m.create_midi_multi_track(m.i.track_map, self.tracks)

if __name__ == '__main__':
    tracks = [
        { 'name': 'Track 1', 'program': 1},
        { 'name': 'Track 2', 'program': 19},
        { 'name': 'Track 3', 'program': 49},
        { 'name': 'Track 4', 'program': 47},
    ]

    m = Main('song.midi', '.\\images\\tester.bmp', tracks)
    m.execute(debug=False)
    