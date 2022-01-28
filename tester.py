from imageData import ImageData
from midiutil import MIDIFile

if __name__ == '__main__':
    i = ImageData('reds_lg.png')

    track = 0
    channel = 0
    time = 0            # in beats
    duration = 4        # in beats
    tempo = 120          # BPM
    volume = 100        # 0 - 127 (MIDI standard)
    volumeLowLim = 75 # low limit for volume

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
                R - pitch (R/2) if greater than 127 else R val
                G - duration
                B - volume 100 if greater than 100, else B val
            """
            pitch = int(pixel[0]//2) if int(pixel[0]) > 127 else int(pixel[0])
            if len(pixel) > 1:
                volume = volumeLowLim if int(pixel[2]) > volumeLowLim else int(pixel[2])
                # duration = (pixel[1] % 3) + 1
            midiFile.addNote(track, channel, pitch, time+idx+jIdx+duration, duration, volume)

    with open("tester.mid", "wb") as f:
        midiFile.writeFile(f)