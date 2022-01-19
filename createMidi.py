import enum
from midiutil import MIDIFile

# scale degrees (C Major)
degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number

track = 0
channel = 0
time = 0        # in beats
duration = 1    # in beats
tempo = 60      # BPM
volume = 100    # 0 - 127 (MIDI standard)

# create a 1 track midi file
# one track, defaults to format 1 (tempo track is created automatically)
midiFile = MIDIFile(1)
midiFile.addTempo(track, time, tempo)

# write the note data
for i, pitch in enumerate(degrees):
    midiFile.addNote(track, channel, pitch, time+i, duration, volume)

with open("majorScale.mid", "wb") as f:
    midiFile.writeFile(f)