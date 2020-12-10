import re
import json

from lxml import html
import requests

def PlaylistFrom1001Tracklist(playlistURL):
    class RequestError(Exception):
        pass

    # Header is needed to make Website believe this request is coming from a browser
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
    
    response = requests.get(playlistURL, headers=headers)
    if response.status_code >= 300:
        raise RequestError("Failed to access webpage. Response Code: {0}".format(response.status_code))

    tree = html.fromstring(response.text)
    setlist_title = tree.xpath('//body/meta[@itemprop="name"]/@content')

    songs = tree.xpath('//div[@class="tlToogleData"][@itemprop="tracks"]/meta[@itemprop="name"]/@content')

    artists_tracks = [tuple((name) for name in song.split(' - ')) for song in songs]

    #Need to fix setlist title
    setlist_title = setlist_title[0]


HtmlParserDict = {
                '1001tracklists' : PlaylistFrom1001Tracklist
}

    
class SetlistWebsite:

    GetHostSite = lambda url: re.search('*www.(*).com*',url).group(1)

    def __init__(self,
                playlistURL):
        self._url = playlistURL
        self._hostsite = GetHostSite(self._url)
        self._set = self.ParserDispatch()

    def ParserDispatch(self):
        return HtmlParserDict[self._hostsite](self._url)