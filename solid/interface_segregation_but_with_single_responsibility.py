# No longer interface segregation
class Song:
    def __init__(self, title: str):
        self.title = title

    def get_upper_case_title(self):
        return self.title.upper()


class SongPlayer:
    def __init__(self, song: Song):
        self.song = song

    def play_drums(self):
        print("Bum-bum-bum")

    def play_guitar(self):
        print("Some guitar solo*")

    def sing_lyrics(self):
        print("Lalalalala")
