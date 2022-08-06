class Track():
    """
    Represents a MIDI track (singular)
    """
    def __init__(self, id, channel, program, name):
        self.id = id
        self.channel = channel
        self.program = program
        self.name = name

    def __str__(self):
        return f"{self.id}-  Name: {self.name}, Channel: {self.id}, " \
                f"Program: {self.program}"