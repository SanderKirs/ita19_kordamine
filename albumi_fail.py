from laulu_fail import Laul

class Album:
    def __init__(self, nimetus, aasta, artist, laulud):
        self.nimetus = nimetus
        self.aasta = aasta
        self.artist = artist
        self.laulud = laulud
album1 = Album("Thrash Zone", "1989", "D.R.I", Laul("Thrasher", "D.R.I"))
print(album1.nimetus,album1.aasta,album1.artist,album1.laulud)
