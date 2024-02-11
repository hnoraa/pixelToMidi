from track import Track
import datetime
import json


class Song():
    def __init__(self, configFile):
        self.date = datetime.datetime.now()
        self.configFile = configFile
        self.__loadConfig()

    def __loadConfig(self):
        with open(self.configFile) as cfg:
            d = json.load(cfg)
            self.title = d['title']
            self.fileName = d['fileName']
            self.imageName = d['imageName']
            self.duration = d['duration']
            self.tempo = d['tempo']
            self.tracks = []
            
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
