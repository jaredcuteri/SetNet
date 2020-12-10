from . import Track

class Setlist:
    def __init__(self,
                 tracklist,
                 dj,
                 date = 'YYYYMMDD',
                 location = ['Club','City','Country']):
        self._tracklist = tracklist
        self._dj = dj
        self._date = date
        self._location = location
        self._tracks = []
        self.PopulateTracks()

    @property
    def tracks(self):
        return self._tracks
    
    def PopulateTracks(self):
        self._tracks = []
        for track in self._tracklist:
            self._tracks.append(Track(*track))


    def __eq__(self, other):
        return type(self) is type(other) \
           and self._dj == other._dj \
           and self._date == other._date \
           and self._location == other._location
