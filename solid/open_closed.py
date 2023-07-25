from abc import abstractmethod


class SearchBy: # Interface
    @abstractmethod
    def is_matched(self, album):
        pass


class SearchByGenre(SearchBy):
    def __init__(self, genre):
        self.genre = genre

    def is_matched(self, album):
        return album.genre == self.genre


class SearchByArtist(SearchBy):
    def __init__(self, artist):
        self.artist = artist

    def is_matched(self, album):
        return album.artist == self.artist


class SearchByTitle(SearchBy):
    def __init__(self, title):
        self.title = title

    def is_matched(self, album):
        return album.title == self.title


class AlbumBrowser:

    # Note we pass one of the classes as searchby arg
    def browse(self, albums, searchby: SearchBy):
        return [album for album in albums if searchby.is_matched(album)]
