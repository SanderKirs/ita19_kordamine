class Laul:
    #Klass  mis kirjeldab laulu

    #Omadused ja atribuudid:
        #pealkiri(Str) = Laulu peakiri
        #laulja (Str) = Laulu artist

    def __init__(self, pealkiri, laulja):
        self.pealkiri = pealkiri
        self.laulja = laulja
laul1 = Laul ("Thrasher", "D.R.I")

