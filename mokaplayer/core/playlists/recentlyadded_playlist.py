from mokaplayer.core.playlists import AbstractPlaylist
from mokaplayer.core.database import Song


class RecentlyAddedPlaylist(AbstractPlaylist):
    @property
    def name(self):
        return "Recently Added"

    def songs(self, order=AbstractPlaylist.OrderBy.DEFAULT, desc=False):
        field = [-Song.Added, Song.AlbumArtist, Song.Year, Song.Album, Song.Discnumber, Song.Tracknumber]
        if desc:
            field[0] = Song.Added

        return Song.select().order_by(*field).limit(150)