class Track:

    def __init__(self,
                 name,
                 artist):
        self._name = name
        self._artist = artist

    @property
    def name(self):
        return self._name

    @property
    def artist(self):
        return self._artist
    