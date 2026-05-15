class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)

    def remove_song(self,song):
        if song  in self.songs:
            self.songs.remove(song)
    
    def display(self):
        print(f"Playlist : {self.name}")
        for song in self.songs:
            print(f" - {song}")
        
p1 = Playlist("Favourite Songs")
p1.add_song("Konjum kili")
p1.add_song("Enna Solla Pogirai")
p1.display()