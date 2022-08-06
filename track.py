class Track():
    """
    Represents a MIDI track (singular)
    """
    def __init__(self, trackIdx, channel, program, name):
        self.trackIdx = trackIdx
        self.channel = channel
        self.program = program
        self.name = name