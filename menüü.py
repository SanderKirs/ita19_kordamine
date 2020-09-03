from laulu_fail import Laul
from albumi_fail import Album
#Testime objekti loomist
laul1 = Laul ("Für oksana", "Nublu")
print (laul1.pealkiri,"-",laul1.laulja)

laul2 = Laul ("laul 2", "Nublu")
print (laul2.pealkiri,"-",laul2.laulja)

#Testime albumi loomist
album = Album ("Uus album", "2019", "Nublu")

#Lisame laulud albumisse
album.laulud.append(laul1)
album.laulud.append(laul2)

for laul in album.laulud:
    print (laul.laulja, "-",laul.pealkiri)