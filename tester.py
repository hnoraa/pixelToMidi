from imageData import ImageData
from midiutil import MIDIFile

if __name__ == '__main__':
    i = ImageData('t_dirt_02.png')

    track = 0
    channel = 0
    time = 0        # in beats
    duration = 4    # in beats
    tempo = 60      # BPM
    volume = 100    # 0 - 127 (MIDI standard)

    # create a 1 track midi file
    # one track, defaults to format 1 (tempo track is created automatically)
    midiFile = MIDIFile(1)
    midiFile.addTempo(track, time, tempo)

    for idx, row in enumerate(i.pixel_array):
        for jIdx, pixel in enumerate(row):
            """
                (R,G,B)
                0-255 values
                MIDI notes are from 0-127
                structure:
                R - pitch (R/2)
                G - duration
                B - volume (B/2)
            """
            midiFile.addNote(track, channel, int(pixel[0]//2), time+idx+jIdx, duration, volume)

    with open("tester.mid", "wb") as f:
        midiFile.writeFile(f)