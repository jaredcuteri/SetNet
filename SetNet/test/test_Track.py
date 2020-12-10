import unittest
import SetNet.Track as Track
class TrackTests(unittest.TestCase):
    
    def test_TrackConstruction(self):
        trackName = 'TrackName'
        artistName = 'ArtistName'
        track = Track(trackName, artistName)
        self.assertEqual(track.name, trackName)
        self.assertEqual(track.artist, artistName)
