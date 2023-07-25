class AlbumShop:
    albums = []

    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))


class ViewRockAlbums:

    def __init__(self, album_shop):
        for album in album_shop.albums:
            if album[2] == "Rock":
                print("We have {} in our shop.".format(album[0]))