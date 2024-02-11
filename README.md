# pixelToMidi - A MIDI generator

Create a midi file from an array of pixels. 

**NOTE:** Right now, this works best with small **.bmp** or **.png** images. 16 x 16 seems to create a file around 2 minutes in duration.

**NOTE:** There seems to be an issue with it only working with 32-bit .bmps

## Running it
`python main.py <config_file.json> <debug: t|f>`

### Arguments

- `<config_file.json>` - the path to the config file

### Sample config file

``` json
{
    "song": "song name",
    "tempo": 120,
    "outputFilename": "song.midi",
    "tracks": [
        {
            "name": "track 1",
            "program": 1
        },
        {
            "name": "track 2",
            "program": 2
        },
        {
            "name": "track 3",
            "program": 4
        },
        {
            "name": "track 4",
            "program": 5
        }
    ]
}
```

## Requirements
### Major requirements

- Python 3.11.0 +
- Pip 23.2.1 +

### From requirements.txt

- MIDIUtil >= 1.2.1
- Pillow >= 9.1.0

## TODO

- [ ] Error handling
    - [ ] Check for empty images
    - [ ] Check for directories and paths
    - [ ] Check that the midi file was created
    - [ ] Determine acceptable file extensions for images
    - [ ] Image resolution warnings
- [x] Note durations
- [ ] Tempo
- [x] Multiple tracks
- [ ] Choosing instruments
- [ ] Song "structure" aka config
- [ ] User interface
- [x] Issues with getting rgb values for pixels on some images
- [x] Figure out how to work with multiple image types
- [ ] Add in a triplet modifier

## Notes
### PIL (Pillow)

Open image: `im = Image.open('image.bmp', 'r')`

Getting an array of (RGB|RGBA) tuples (aka the pixels):

`pixel_array = list(im.getdata())`

### MIDIUtil
#### Overview of `MIDIFile -> __init__()`:

``` python
def __init__(self,
          numTracks=1,
          removeDuplicates=True,
          deinterleave=True,
          adjust_origin=False,
          file_format=1,
          ticks_per_quarternote=TICKSPERQUARTERNOTE,
          eventtime_is_ticks=False):
```

- numTracks = Number of tracks
- removeDuplicates = Remove duplicate notes (notes that occur at the same time and have equal pitch and midi channel)
- deinterleave = Remove interleaved notes (notes that are ambiguously similar)
- adjust_origin = Finds the earliest event and shifts all events so that earliest event is t=0
- file_format = Can be two formats (0, 1)
    - 0 (format 1) > addTempo() and addTimeSignature() are ignored
    - 1 (format 2) > addTempo() and addTimeSignature() are interpreted literally
- ticks_per_quarternote = MIDI ticks per quarternote. Default is 960
    - common values: 120, 240,384, 480 & 960
- eventtime_is_ticks = If True, all times passed into the event creation functions should be specified in ticks. If False, they are specified in quarter notes

#### Add Notes

`MIDIFile.addNote(track, channel, pitch, time, duration, volume, annotation=None)`

This is the main function being used

- track = Track the note is added to
- channel = MIDI channel [0-15]
- pitch = Note value [0-127]
- time = The time at which the note sounds. Can be either quarter notes (Float) or ticks (Int). See `__init__()` above
- duration = The duration of the note. Can be either quarter notes (Float) or ticks (Int)
- volume = The volume (velocity)
- annotation = Metadata

#### Add Tempo

`MIDIFile.addTempo(track, time, tempo)`

Each track can have it's own tempo

- track = The track to add a tempo event
- time = Where to add the tempo event in the track
- temp = The tempo to add

#### Add a Program Change Event

`MIDIFile.addProgramChange(tracknum, channel, time, program)`

This can be used to change the "instrument" of the track. Aka the sound

- tracknum = The track to change the program on
- channel = The MIDI channel to assign the event to
- time = The time (in beats), this is a Float value
- program = The program number [0-127]

### GM MIDI Programs

``` json
{
    "soundSet":"GM MIDI 1",
    "references": [
        "https://www.midi.org/specifications-old/item/gm-level-1-sound-set",
        "https://www.midi.org/specifications/midi1-specifications/general-midi-specifications/general-midi-1"
    ],
    "programs":[
        {"id": 0, "name":"Acoustic Grand Piano"},
        {"id": 1, "name":"Bright Acoustic Piano"},
        {"id": 2, "name":"Electric Grand Piano"},
        {"id": 3, "name":"Honky-tonk Piano"},
        {"id": 4, "name":"Electric Piano 1"},
        {"id": 5, "name":"Electric Piano 2"},
        {"id": 6, "name":"Harpsichord"},
        {"id": 7, "name":"Clavi"},
        {"id": 8, "name":"Celesta"},
        {"id": 9, "name":"Glockenspiel"},
        {"id": 10, "name":"Music Box"},
        {"id": 11, "name":"Vibraphone"},
        {"id": 12, "name":"Marimba"},
        {"id": 13, "name":"Xylophone"},
        {"id": 14, "name":"Tubular Bells"},
        {"id": 15, "name":"Dulcimer"},
        {"id": 16, "name":"Drawbar Organ"},
        {"id": 17, "name":"Percussive Organ"},
        {"id": 18, "name":"Rock Organ"},
        {"id": 19, "name":"Church Organ"},
        {"id": 20, "name":"Reed Organ"},
        {"id": 21, "name":"Accordion"},
        {"id": 22, "name":"Harmonica"},
        {"id": 23, "name":"Tango Accordion"},
        {"id": 24, "name":"Acoustic Guitar (nylon)"},
        {"id": 25, "name":"Acoustic Guitar (steel)"},
        {"id": 26, "name":"Electric Guitar (jazz)"},
        {"id": 27, "name":"Electric Guitar (clean)"},
        {"id": 28, "name":"Electric Guitar (muted)"},
        {"id": 29, "name":"Overdriven Guitar"},
        {"id": 30, "name":"Distortion Guitar"},
        {"id": 31, "name":"Guitar harmonics"},
        {"id": 32, "name":"Acoustic Bass"},
        {"id": 33, "name":"Electric Bass (finger)"},
        {"id": 34, "name":"Electric Bass (pick)"},
        {"id": 35, "name":"Fretless Bass"},
        {"id": 36, "name":"Slap Bass 1"},
        {"id": 37, "name":"Slap Bass 2"},
        {"id": 38, "name":"Synth Bass 1"},
        {"id": 39, "name":"Synth Bass 2"},
        {"id": 40, "name":"Violin"},
        {"id": 41, "name":"Viola"},
        {"id": 42, "name":"Cello"},
        {"id": 43, "name":"Contrabass"},
        {"id": 44, "name":"Tremolo Strings"},
        {"id": 45, "name":"Pizzicato Strings"},
        {"id": 46, "name":"Orchestral Harp"},
        {"id": 47, "name":"Timpani"},
        {"id": 48, "name":"String Ensemble 1"},
        {"id": 49, "name":"String Ensemble 2"},
        {"id": 50, "name":"SynthStrings 1"},
        {"id": 51, "name":"SynthStrings 2"},
        {"id": 52, "name":"Choir Aahs"},
        {"id": 53, "name":"Voice Oohs"},
        {"id": 54, "name":"Synth Voice"},
        {"id": 55, "name":"Orchestra Hit"},
        {"id": 56, "name":"Trumpet"},
        {"id": 57, "name":"Trombone"},
        {"id": 58, "name":"Tuba"},
        {"id": 59, "name":"Muted Trumpet"},
        {"id": 60, "name":"French Horn"},
        {"id": 61, "name":"Brass Section"},
        {"id": 62, "name":"SynthBrass 1"},
        {"id": 63, "name":"SynthBrass 2"},
        {"id": 64, "name":"Soprano Sax"},
        {"id": 65, "name":"Alto Sax"},
        {"id": 66, "name":"Tenor Sax"},
        {"id": 67, "name":"Baritone Sax"},
        {"id": 68, "name":"Oboe"},
        {"id": 69, "name":"English Horn"},
        {"id": 70, "name":"Bassoon"},
        {"id": 71, "name":"Clarinet"},
        {"id": 72, "name":"Piccolo"},
        {"id": 73, "name":"Flute"},
        {"id": 74, "name":"Recorder"},
        {"id": 75, "name":"Pan Flute"},
        {"id": 76, "name":"Blown Bottle"},
        {"id": 77, "name":"Shakuhachi"},
        {"id": 78, "name":"Whistle"},
        {"id": 79, "name":"Ocarina"},
        {"id": 80, "name":"Lead 1 (square)"},
        {"id": 81, "name":"Lead 2 (sawtooth)"},
        {"id": 82, "name":"Lead 3 (calliope)"},
        {"id": 83, "name":"Lead 4 (chiff)"},
        {"id": 84, "name":"Lead 5 (charang)"},
        {"id": 85, "name":"Lead 6 (voice)"},
        {"id": 86, "name":"Lead 7 (fifths)"},
        {"id": 87, "name":"Lead 8 (bass + lead)"},
        {"id": 88, "name":"Pad 1 (new age)"},
        {"id": 89, "name":"Pad 2 (warm)"},
        {"id": 90, "name":"Pad 3 (polysynth)"},
        {"id": 91, "name":"Pad 4 (choir)"},
        {"id": 92, "name":"Pad 5 (bowed)"},
        {"id": 93, "name":"Pad 6 (metallic)"},
        {"id": 94, "name":"Pad 7 (halo)"},
        {"id": 95, "name":"Pad 8 (sweep)"},
        {"id": 96, "name":"FX 1 (rain)"},
        {"id": 97, "name":"FX 2 (soundtrack)"},
        {"id": 98, "name":"FX 3 (crystal)"},
        {"id": 99, "name":"FX 4 (atmosphere)"},
        {"id": 100, "name":"FX 5 (brightness)"},
        {"id": 101, "name":"FX 6 (goblins)"},
        {"id": 102, "name":"FX 7 (echoes)"},
        {"id": 103, "name":"FX 8 (sci-fi)"},
        {"id": 104, "name":"Sitar"},
        {"id": 105, "name":"Banjo"},
        {"id": 106, "name":"Shamisen"},
        {"id": 107, "name":"Koto"},
        {"id": 108, "name":"Kalimba"},
        {"id": 109, "name":"Bag pipe"},
        {"id": 110, "name":"Fiddle"},
        {"id": 111, "name":"Shanai"},
        {"id": 112, "name":"Tinkle Bell"},
        {"id": 113, "name":"Agogo"},
        {"id": 114, "name":"Steel Drums"},
        {"id": 115, "name":"Woodblock"},
        {"id": 116, "name":"Taiko Drum"},
        {"id": 117, "name":"Melodic Tom"},
        {"id": 118, "name":"Synth Drum"},
        {"id": 119, "name":"Reverse Cymbal"},
        {"id": 120, "name":"Guitar Fret Noise"},
        {"id": 121, "name":"Breath Noise"},
        {"id": 122, "name":"Seashore"},
        {"id": 123, "name":"Bird Tweet"},
        {"id": 124, "name":"Telephone Ring"},
        {"id": 125, "name":"Helicopter"},
        {"id": 126, "name":"Applause"},
        {"id": 127, "name":"Gunshot"}
    ]
}
```

## Pixel to Midi Algorithm

1. Load image
2. For each pixel in image (RGB or RGBA)
    - Pixel values are 0-255
    - MIDI notes are 0-127
    1. Take the R value
        - R is pitch
        1. If R > 127
            - pitch = R/2
        2. Else
            - pitch = R
    2. Take the G value
        - G is note duration
        - The noteDurations array has 9 items
        1. Get the remainder of G % length of noteDurations array
        2. Apply that to the noteDurations to get the duration
    3. Take the B value
        - B is volume
        1. If B > 100
            - volume = 100
        2. Else
            - volume = B
    4. Take the A value
        - This may be missing in a bmp or png
        - Optional parameter
        - Might be useful for multiple tracks?
        - Could be tracks[A % len(tracks)] 
3. Save midi file

## More MIDI Miscellany

If using quarter note based time parameters, this is the float array starting at longa. This was found on Wikipedia...

|Note Name                     |Duration|Duration as float   |
|------------------------------|--------|--------------------|
|Longa                         |4       |4.0                 |
|Double whole note             |2       |2.0                 |
|Whole note                    |1       |1.0                 |
|Half note                     |1/2     |0.5                 |
|Quarter note                  |1/4     |0.25                |
|Eight note                    |1/8     |0.125               |
|Sixteenth note                |1/16    |0.0625              |
|Thirty-Second note            |1/32    |0.03125             |
|Sixty-Fourth note             |1/64    |0.015625            |
|One Hundred Twenty-Eighth note|1/128   |0.0078125           |

<sub>**Note:** Most of these may not be used but are here anyways</sub>


``` python
# longa = 4, double whole note = 2, whole note = 1, half = 1/2, 
# quarter = 1/4, eighth = 1/8, sixteenth = 1/16, thirty-second = 1/32, 
# sixty-fourth = 1/64, hundred twenty-eighth = 1/128
self.noteDurations = [
    4, 2, 1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125
]
```

## Getting set up
### Install Pillow

[https://pillow.readthedocs.io/en/latest/installation.html]

`python -m pip install --upgrade pip`

`python -m pip install --upgrade Pillow`

### Create virtual enviroment

`python -m venv env`

### Run virtual environment

<sub>Using Powershell</sub>

`.\env\Scripts\Activate.ps1`

### Install requirements

`pip install --upgrade pip`

`pip install -r requirements.txt`