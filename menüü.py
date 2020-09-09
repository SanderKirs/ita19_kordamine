#Importime teistest failidest vajalikud klassid
from laulu_fail import Laul
from albumi_fail import Album
from laulja import Laulja

#Testime objekti loomist
laul1 = Laul ("laul 1", "Nublu")
print (laul1.pealkiri,"-",laul1.laulja)

laul2 = Laul ("laul 2", "Nublu")
print (laul2.pealkiri,"-",laul2.laulja)

laul3 = Laul ("laul 3", "Nublu")
print (laul3.pealkiri,"-",laul3.laulja)

laul4 = Laul ("laul 4", "Nublu")
print (laul4.pealkiri,"-",laul4.laulja)

#Testime albumi loomist
album1 = Album ("Uus album", "2019", "Nublu")

album2 = Album ("Vana album", "2018", "Nublu")

#Lisame laulud albumisse
album1.lisa_laul(laul1)
album1.lisa_laul(laul2)
album2.lisa_laul(laul3)
album2.lisa_laul(laul4)

#Testime for tsükli abil laulu printimist albumist
for laul in album1.laulud:
    print (laul.laulja, "-",laul.pealkiri)
for laul in album2.laulud:
    print (laul.laulja, "-",laul.pealkiri)

#Testime Laulja klassi ja funktsiooni lisa_album
laulja = Laulja ("Nublu")
laulja.lisa_album(album1)
laulja.lisa_album(album2)

#Testime albumite sisu
for album in laulja.albumid:
    print(album.pealkiri)
    for laul in album.laulud:
        print(laul.laulja, laul.pealkiri)

#Loeme albumite failist laulud,albumid ja nende aastad
järk = []
with open("albumid", "rt") as f:
    for line in f:
        järk.append(line)
        print(järk[-1])