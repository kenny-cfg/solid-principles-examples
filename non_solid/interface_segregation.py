class PlaySongs:

    def __init__(self, title: str):
        self.title = title

    def get_upper_case_title(self):
        return self.title.upper()

    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")

    def sing_lyrics(self):
        print("We will, we will rock you!")


if __name__ == '__main__':
    rock_songs = PlaySongs('We will rock you')
    rock_songs.sing_lyrics()
    print(rock_songs.get_upper_case_title())
