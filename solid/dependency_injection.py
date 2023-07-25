from abc import abstractmethod


class GeneralAlbumShop:

    @abstractmethod
    def filter_by_genre(self, genre):
        pass


class MyAlbumShop(GeneralAlbumShop):
    albums = []

    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))

    def filter_by_genre(self, genre):
        for album in self.albums:
            if album[2] == genre:
                yield album[0]


    # Exactly the same as the above method
    def filter_by_genre_without_yield(self, genre):
        filtered_albums = []
        for album in self.albums:
            if album[2] == genre:
                filtered_albums.append(album[0])
        return filtered_albums


class ViewRockAlbums:
    def __init__(self, album_store):
        for album_name in album_store.filter_by_genre("Rock"):
            print("We have {} in our shop.".format(album_name))