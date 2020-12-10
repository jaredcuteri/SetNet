import unittest
import SetNet.Setlist as Setlist
import SetNet.Track as Track
class SetlistTests(unittest.TestCase):
    
    def test_SetlistConstruction(self):
        djName = 'DjName'
        date = '20200101'
        location = ['The Fox','Tucson','Arizona']
        trackName = 'TrackName'
        artistName = 'ArtistName'

        # Generate tracks for setlist
        tracklist = []
        trackObjs = []
        track_iter = range(3)
        for i in track_iter:
            trackArtistPair = [trackName+str(i),artistName+str(i)]
            trackObjs.append(Track(*trackArtistPair))
            tracklist.append(trackArtistPair)
        
        setlist = Setlist(tracklist, djName, date, location)

        # Verify all tracks have been added
        for i in track_iter:
            self.assertEqual(setlist.tracks[i],trackObjs[i])

        # Verify setlist attributes are set correctly
        self.assertEqual(setlist._dj, djName)
        self.assertEqual(setlist._date, date)
        self.assertEqual(setlist._location, location)
