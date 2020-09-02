class Laul:
    #Klass  mis kijeldab laulu

    #Omadused ja atribuudid:
        #pealkiri(Str) = Laulu peakiri
        #laulja (Str) = Laulu artist

    def __init__(self, pealkiri, laulja):
        self.pealkiri = pealkiri
        self.laulja = laulja
laul1 = Laul ("Für oksana", "Nublu")
print (laul1.pealkiri,"-",laul1.laulja)
