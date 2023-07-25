class AlbumBrowser:


    def search_album_by_artist(self, albums, artist):
        return [album for album in albums if album.artist == artist]


    def search_album_by_genre(self, albums, genre):
        return [album for album in albums if album.genre == genre]


    def search_album_by_title(self, albums, title):
        return [album for album in albums if album.title == title]

    # etc.

    # Now what happens if we want to search by artist or by genre?
    # What if we add release year?
    # We will have to write a new function every time modifying the class!
