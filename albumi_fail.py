from laulu_fail import Laul

class Album:
    def __init__(self, pealkiri, aasta, artist):
        self.pealkiri = pealkiri
        self.aasta = aasta
        self.artist = artist
        self.laulud = []

    def lisa_laul(self,laul):
        self.laulud.append(laul)


