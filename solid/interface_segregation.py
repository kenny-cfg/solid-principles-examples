from abc import abstractmethod


class PlaySongsLyrics:

    @abstractmethod
    def sing_lyrics(self):
        pass


class PlaySongsMusic:

    @abstractmethod
    def play_guitar(self):
        pass

    @abstractmethod
    def play_drums(self):
        pass


class PlayInstrumentalSong(PlaySongsMusic):

    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")


class PlayRockSong(PlaySongsMusic, PlaySongsLyrics):
    def __init__(self, title: str):
        self.title = title

    def get_upper_case_title(self):
        return self.title.upper()

    def play_guitar(self):
        print("Heavy metal guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you")

    def play_drums(self):
        print("Bum-bum-bum")


if __name__ == '__main__':
    rock_songs = PlayRockSong('We will rock you')
    rock_songs.sing_lyrics()
    print(rock_songs.get_upper_case_title())