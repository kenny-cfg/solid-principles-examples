class PlaySongs:

    def __init__(self, title):
        self.title = title

    def get_upper_case_title(self):
        return self.title.upper()


class PlayRockSongs(PlaySongs):

    def play_guitar(self):
        print("Heavy metal guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you!")

    def play_drums(self):
        print("Bum-bum-bum")


if __name__ == '__main__':
    rock_songs = PlayRockSongs('We will rock you')
    rock_songs.sing_lyrics()
    print(rock_songs.get_upper_case_title())