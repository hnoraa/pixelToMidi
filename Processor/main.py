import os
import sys
import json
from PIL import Image
from midiutil import MIDIFile

class ImageImport():
    def __init__(self, image_path) -> None:
        self.image_path = image_path
        self.img = None
        self.img_map = None

    def import_image(self):
        self.img = Image.open(self.image_path, 'r').convert('RGB')
        self.img_map = list(self.img.getdata())

    def describe(self):
        if self.img is not None:
            print(f'Printing {self.image_path} details:')
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
        self.note_durations = [
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
                G - duration (G % len(note_durations))
                B - volume 100 if greater than 100, else B val
                A - (optional) I think this could be useful for multi-tracking
                    Ex: say you have 4 tracks, A value is 100, the current track could be tracks[A % len(tracks)]
            """
            pitch = int(row[0]//2) if int(row[0]) > 127 else int(row[0])
            if len(row) > 1:
                self.volume = self.volume_low_lim if int(row[2]) > self.volume_low_lim else int(row[2])
                self.duration = self.note_durations[row[1] % len(self.note_durations)]
            self.midi_file.addNote(self.track, self.channel, pitch, self.time+idx+self.duration, self.duration, self.volume)

        with open(self.midi_file_name, 'wb') as f:
            self.midi_file.writeFile(f)

    def create_midi_multi_track(self, track_map, tracks):
        """
            (R,G,B) or (R,G,B,A)
            0-255 values
            MIDI notes are from 0-127
            structure:
            R - pitch (R/2) if greater than 127 else R val
            G - duration (G % len(note_durations))
            B - volume 100 if greater than 100, else B val
            A - (optional) I think this could be useful for multi-tracking
                Ex: say you have 4 tracks, A value is 100, the current track could be tracks[A % len(tracks)]
        """
        
        for i, track in enumerate(tracks):
            self.midi_file.addProgramChange(i, i, 0, track['program'])
            for idx, row in enumerate(track_map[i]):
                pitch = int(row[0]//2) if int(row[0]) >= 128 else int(row[0])
                if len(row) > 1:
                    self.volume = self.volume_low_lim if int(row[2]) > self.volume_low_lim else int(row[2])
                    self.duration = self.note_durations[row[1] % len(self.note_durations)]
                self.midi_file.addNote(i, i, pitch, self.time+idx+self.duration, self.duration, self.volume)

        with open(self.midi_file_name, 'wb') as f:
            self.midi_file.writeFile(f)

class Main():
    def __init__(self) -> None:
        #self.tracks = tracks
        self.config = {}

        self.i = None #ImageImport(image_path)
        self.m = None #MidiProcessor(midi_file_name, len(self.tracks))

    def load_config(self, config_file):
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)

            if not self.validate_config():
                raise Exception('Error: Configuration not in the expected format. Please consult documentation')
        except FileNotFoundError:
            print(f'Error: Cannot find the config file: {config_file}')
            sys.exit(1)
        except json.JSONDecodeError:
            print(f'Error: Config is not in json format ({config_file})')
            sys.exit(1)
        except Exception as ex:
            print(ex)
            sys.exit(1)

    def validate_config(self):
        # empty check
        if self.empty_config():
            return False
        
        # set up the expected values
        required_keys = ['song', 'outputFilename', 'tempo', 'image', 'tracks']
        required_track_keys = ['name', 'program']

        # validate top level properties
        if not all(key in self.config for key in required_keys):
            return False
        
        # validate track level properties
        if not (isinstance(self.config['tracks'], list) and
                all(isinstance(track, dict) and all(track_key in track for track_key in required_track_keys)
                     for track in self.config['tracks'])):
            return False

        return True

    def print_config(self):
        print('Config file')
        print(self.config)

    def empty_config(self):
        return not bool(self.config)
    
    def set_up(self):
        try:
            if self.empty_config:
                print('Config file is empty')
            else:
                if not os.path.exists(image_file):
                    raise Exception(f'Error: Image {self.config.get("image")} not found')
                self.i = ImageImport(self.config.get('image'))
                self.m = MidiProcessor(self.config.get('song'), len(self.tracks))
        except Exception as ex:
            print(ex)
            sys.exit(1)

    def execute(self, debug=False):
        if self.empty_config:
            print('Config file is empty')
        else:
            self.i.import_image()

            if debug:
                m.i.describe()
                m.i.test_image_array()
                m.i.split_image_array_test(2)
            else:
                m.i.split_image_array(len(self.tracks))
                self.m.create_midi_multi_track(m.i.track_map, self.tracks)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: main.py <config_file.json>')
        sys.exit(1)

    # load the config
    

    tracks = [
        { 'name': 'Track 1', 'program': 1},
        { 'name': 'Track 2', 'program': 19},
        { 'name': 'Track 3', 'program': 49},
        { 'name': 'Track 4', 'program': 47},
    ]

    midi_file = sys.argv[1]
    image_file = sys.argv[2]
    is_debug = False

    if len(sys.argv) == 4:
        is_debug = True if sys.argv[3].lower() == 't' else  False

    if os.path.exists(image_file):
        print(f'Creating MIDI file {midi_file} from {image_file} (Debug: {is_debug})')
        m = Main(midi_file, image_file, tracks)
        m.execute(debug=is_debug)
    else:
        print(f'Error: Image {image_file} not found')
        
    