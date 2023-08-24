class Song:

    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # increment count each time we create a new song
        Song.count += 1
        # add artist, genres to set
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        # now add to count
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

    

    


song1 = Song('song1', 'Beyonce', 'pop')
song2 = Song('song2', 'Beyonce', 'pop')
song3 = Song('song3', 'Jay-Z', 'rap')

import ipdb; ipdb.set_trace()