from track import Track
import datetime


class Song():
    def __init__(self, configFile):
        self.configFile = configFile
        self.date = datetime.datetime.now()
        self.title = ""
        self.fileName = ""
        self.image = ""
        self.duration = 4
        self.tempo = 120
        self.tracks = []

    def __loadConfig(self):
        pass
    
    def __str__(self):
        d = "Song Information:" \
            f"\nName: {self.title} Date Created: {self.date}" \
            f"\n\tFile: {self.fileName} Image:{self.imageName}" \
            f"\n\tDuration: {self.duration} Tempo: {self.tempo}" \
            f"\n\tTracks: {len(self.tracks)}"
        for t in self.tracks:
            d += f"\n\t\t{t.id}-  Name: {t.name}, Channel: {t.id}, " \
                f"Program{t.program}"
        d += f"Config: {self.configFile}"
        return d
