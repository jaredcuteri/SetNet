import Track

class Setlist:
    def __init__(self,
                 tracklist,
                 dj,
                 location = ['Club','City','Country']):
        self._tracklist = tracklist
        self._dj = dj
        self._location = location
        self._tracks = []
        self.PopulateTracks()

    def PopulateTracks(self):
        self._tracks = []
        for track in self._tracklist:
            self._tracks.extend(Track(track))

    

