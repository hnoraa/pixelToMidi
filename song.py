from track import Track
import datetime
import json


class Song():
    """
    Default constructor
    """
    def __init__(self):
        self.date = datetime.datetime.now()
        self.title = ""
        self.fileName = ""
        self.imageName = ""
        self.duration = 4
        self.tempo = 120
        self.tracks = []

    """
    Command line constructor
    """
    def __init__(self, configFile):
        self.__init__()
        self.configFile = configFile
        self.__loadConfig()

    """
    UI constructor
    """
    def __init__(self, title, fileName, imageName, duration, tempo, tracks):
        self.__init__()
        self.title = title
        self.fileName = fileName
        self.imageName = imageName
        self.duration = duration
        self.tempo = tempo
        for t in tracks:
            self.tracks.append(t)

    def __loadConfig(self):
        with open(self.configFile) as cfg:
            d = json.load(cfg)
            self.title = d['title']
            self.fileName = d['fileName']
            self.imageName = d['imageName']
            self.duration = d['duration']
            self.tempo = d['tempo']

            for i in range(len(d['tracks'])):
                self.tracks.append(Track(
                    d['tracks'][i]['id'],
                    d['tracks'][i]['channel'],
                    d['tracks'][i]['program'],
                    d['tracks'][i]['name']
                ))

    def __str__(self):
        d = "Song Information:" \
            f"\nName: {self.title}\n\tDate Created: {self.date}" \
            f"\n\tFile: {self.fileName}\n\tImage:{self.imageName}" \
            f"\n\tDuration: {self.duration}\n\tTempo: {self.tempo}" \
            f"\n\tTracks: {len(self.tracks)}"
        for t in self.tracks:
            d += f"\n\t\t{t}"
        d += f"\nConfig: {self.configFile}"
        return d
