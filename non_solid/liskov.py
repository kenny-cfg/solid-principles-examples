class Album:

    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)


class BestOfCompilation(Album):
    def __init__(self, artist, songs):
        super().__init__("Best of", artist, songs)


if __name__ == '__main__':
    compilation = BestOfCompilation('Queen', [])
    compilation.add_song('Bohemian Rhapsody')
    pass