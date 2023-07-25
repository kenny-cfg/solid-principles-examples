class Album:

    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    # breaks the SRP !!!
    def search_album_by_artist(self):
        """ Searching the database for other albums by same artist """
        pass